#!/usr/bin/env python3
"""
INKFORGE Lite - Visual Canvas with HTTP API

A standalone visual canvas that any AI agent can interact with via HTTP.

Usage:
    python inkforge.py [--port PORT] [--no-window]

API Endpoints:
    GET  /snapshot  - Returns { current: b64, previous: b64 }
    GET  /changed   - Returns { changed: bool, regions: [...], timestamp: int }
    POST /draw      - Inject SVG: { svg: "..." }
    POST /clear     - Reset canvas
    POST /ack       - Acknowledge changes (reset changed flag)
"""

import argparse
import base64
import json
import threading
import time
from pathlib import Path

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

# State shared between Flask and pywebview
class CanvasState:
    def __init__(self):
        self.current = None      # Base64 PNG of current canvas
        self.previous = None     # Base64 PNG of previous state
        self.svg = None          # Last SVG to inject
        self.svg_version = 0     # Incremented when new SVG arrives
        self.changed = False     # Has canvas changed since last ack?
        self.regions = []        # List of {x, y, w, h} modified regions
        self.timestamp = 0       # Last change timestamp
        self.lock = threading.Lock()

    def update_snapshot(self, current_b64, previous_b64=None):
        with self.lock:
            if previous_b64:
                self.previous = previous_b64
            elif self.current:
                self.previous = self.current
            self.current = current_b64

    def add_region(self, x, y, w, h):
        with self.lock:
            self.changed = True
            self.timestamp = int(time.time() * 1000)
            # Merge overlapping regions or just append
            self.regions.append({"x": x, "y": y, "w": w, "h": h})

    def set_svg(self, svg):
        with self.lock:
            self.svg = svg
            self.svg_version += 1

    def get_svg(self):
        with self.lock:
            return self.svg, self.svg_version

    def acknowledge(self):
        with self.lock:
            self.changed = False
            self.regions = []

    def clear(self):
        with self.lock:
            self.current = None
            self.previous = None
            self.svg = None
            self.changed = False
            self.regions = []
            self.timestamp = 0

state = CanvasState()

# Flask app
app = Flask(__name__, static_folder='static')
CORS(app)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('static', path)

@app.route('/snapshot', methods=['GET', 'POST'])
def snapshot():
    """GET: Return snapshots. POST: Update current snapshot."""
    if request.method == 'POST':
        data = request.get_json()
        if data and 'current' in data:
            state.update_snapshot(data['current'], data.get('previous'))
            return jsonify({"ok": True})
        return jsonify({"error": "Missing 'current' in request body"}), 400

    # GET
    with state.lock:
        return jsonify({
            "current": state.current,
            "previous": state.previous,
            "timestamp": state.timestamp
        })

@app.route('/changed', methods=['GET'])
def changed():
    """Check if canvas has changed since last ack."""
    with state.lock:
        return jsonify({
            "changed": state.changed,
            "regions": state.regions.copy(),
            "timestamp": state.timestamp
        })

@app.route('/draw', methods=['POST'])
def draw():
    """Inject SVG into canvas."""
    data = request.get_json()
    if not data or 'svg' not in data:
        return jsonify({"error": "Missing 'svg' in request body"}), 400

    state.set_svg(data['svg'])
    return jsonify({"ok": True, "version": state.svg_version})

@app.route('/clear', methods=['POST'])
def clear():
    """Clear canvas and reset state."""
    state.clear()
    return jsonify({"ok": True})

@app.route('/ack', methods=['POST'])
def ack():
    """Acknowledge changes - reset changed flag and regions."""
    state.acknowledge()
    return jsonify({"ok": True})

@app.route('/region', methods=['POST'])
def add_region():
    """Add a modified region."""
    data = request.get_json()
    if data and all(k in data for k in ('x', 'y', 'w', 'h')):
        state.add_region(data['x'], data['y'], data['w'], data['h'])
        return jsonify({"ok": True})
    return jsonify({"error": "Missing x, y, w, h in request body"}), 400

@app.route('/status', methods=['GET'])
def status():
    """Health check endpoint."""
    return jsonify({
        "status": "running",
        "has_snapshot": state.current is not None,
        "has_svg": state.svg is not None,
        "changed": state.changed
    })

@app.route('/svg', methods=['GET'])
def get_svg():
    """Get current SVG to display."""
    svg, version = state.get_svg()
    return jsonify({
        "svg": svg,
        "version": version
    })


# pywebview API exposed to JavaScript
class Api:
    def __init__(self):
        self._window = None

    def set_window(self, window):
        """Set the window reference for control methods."""
        self._window = window

    def save_snapshot(self, current_b64, previous_b64=None):
        """Called by JS when canvas state changes."""
        state.update_snapshot(current_b64, previous_b64)
        return True

    def add_modified_region(self, x, y, w, h):
        """Called by JS when user draws in a region."""
        state.add_region(x, y, w, h)
        return True

    def get_svg(self):
        """Called by JS to check for new SVG to render."""
        svg, version = state.get_svg()
        return {"svg": svg, "version": version}

    def clear_state(self):
        """Called by JS when canvas is cleared."""
        state.clear()
        return True

    def minimize(self):
        """Minimize the window."""
        if self._window:
            self._window.minimize()

    def maximize(self):
        """Toggle maximize/restore the window."""
        if self._window:
            self._window.toggle_fullscreen()

    def close(self):
        """Close the window."""
        if self._window:
            self._window.destroy()

    def move_window(self, dx, dy):
        """Move window by delta."""
        if self._window:
            self._window.move(self._window.x + dx, self._window.y + dy)

    def save_file(self, base64_data):
        """Open save dialog and save PNG."""
        import webview
        if self._window:
            result = self._window.create_file_dialog(
                webview.SAVE_DIALOG,
                save_filename='inkforge-sketch.png',
                file_types=('PNG Files (*.png)',)
            )
            if result:
                import base64
                filepath = result if isinstance(result, str) else result[0]
                with open(filepath, 'wb') as f:
                    f.write(base64.b64decode(base64_data))
                return True
        return False


def run_flask(port):
    """Run Flask server in a thread."""
    app.run(host='127.0.0.1', port=port, threaded=True, use_reloader=False)


def main():
    parser = argparse.ArgumentParser(description='INKFORGE Lite - Visual Canvas')
    parser.add_argument('--port', type=int, default=8765, help='HTTP API port (default: 8765)')
    parser.add_argument('--no-window', action='store_true', help='Run without GUI (server only)')
    parser.add_argument('--debug', action='store_true', help='Enable Flask debug mode')
    args = parser.parse_args()

    print(f"""
=============================================================
  INKFORGE Lite - Visual Canvas with HTTP API
=============================================================
  API: http://127.0.0.1:{args.port}

  Endpoints:
    GET  /snapshot  - Get canvas images (base64)
    GET  /changed   - Check for changes
    POST /draw      - Inject SVG
    POST /clear     - Reset canvas
    POST /ack       - Acknowledge changes
=============================================================
""")

    if args.no_window:
        # Server only mode
        app.run(host='127.0.0.1', port=args.port, threaded=True, debug=args.debug)
    else:
        # GUI mode with pywebview
        try:
            import webview
        except ImportError:
            print("ERROR: pywebview not installed. Run: pip install pywebview")
            print("       Or use --no-window for server-only mode")
            return 1

        # Start Flask in background thread
        flask_thread = threading.Thread(target=run_flask, args=(args.port,), daemon=True)
        flask_thread.start()

        # Give Flask time to start
        time.sleep(0.5)

        # Create pywebview window (frameless for clean look)
        api = Api()
        window = webview.create_window(
            'INKFORGE Lite',
            f'http://127.0.0.1:{args.port}',
            js_api=api,
            width=808,
            height=648,
            min_size=(808, 648),
            frameless=True,
            easy_drag=False  # We'll handle drag ourselves
        )

        # Set window reference for API controls
        api.set_window(window)

        webview.start(debug=args.debug)

    return 0


if __name__ == '__main__':
    exit(main())
