# INKFORGE Lite

A standalone visual canvas with HTTP API that any AI agent can interact with.

## Features

- **Drawing Canvas**: Freehand drawing with adjustable brush size
- **Region Tracking**: Tracks modified regions for smart diffing
- **HTTP API**: Any agent (Claude Code, HIVE, scripts) can interact
- **SVG Injection**: Agents can send SVG to display on canvas
- **Standalone App**: pywebview window, no browser needed

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### GUI Mode (default)
```bash
python inkforge.py
```

### Server-only Mode (no window)
```bash
python inkforge.py --no-window
```

### Options
```
--port PORT     HTTP API port (default: 8765)
--no-window     Run without GUI window
--debug         Enable debug mode
```

## HTTP API

Default: `http://127.0.0.1:8765`

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/snapshot` | GET | Get canvas images as base64 PNG |
| `/changed` | GET | Check if canvas changed since last ack |
| `/draw` | POST | Inject SVG into canvas |
| `/clear` | POST | Reset canvas |
| `/ack` | POST | Acknowledge changes |
| `/status` | GET | Health check |

### Examples

#### Check for changes
```bash
curl http://127.0.0.1:8765/changed
# {"changed": true, "regions": [{"x": 10, "y": 20, "w": 100, "h": 50}], "timestamp": 1234567890}
```

#### Get canvas snapshot
```bash
curl http://127.0.0.1:8765/snapshot
# {"current": "base64...", "previous": "base64...", "timestamp": 1234567890}
```

#### Inject SVG
```bash
curl -X POST http://127.0.0.1:8765/draw \
  -H "Content-Type: application/json" \
  -d '{"svg": "<svg viewBox=\"0 0 100 100\"><circle cx=\"50\" cy=\"50\" r=\"40\" fill=\"red\"/></svg>"}'
```

#### Acknowledge changes
```bash
curl -X POST http://127.0.0.1:8765/ack
```

## Integration with Claude Code

Use with a skill that:
1. Calls `GET /changed` to detect user input
2. Calls `GET /snapshot` to get images
3. Sends images to Claude Vision
4. Generates SVG response
5. Calls `POST /draw` to display result
6. Calls `POST /ack` to reset change flag

## Architecture

```
┌─────────────────────────────────────────────────────┐
│  pywebview window                                   │
│  ┌─────────────────────────────────────────────┐   │
│  │  Canvas (HTML5 + Vanilla JS)                  │   │
│  │  - Drawing                                   │   │
│  │  - Region tracking                           │   │
│  │  - SVG display                               │   │
│  └─────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────┘
         ▲                              │
         │ pywebview.api               │
         ▼                              ▼
┌─────────────────────────────────────────────────────┐
│  Python Backend                                     │
│  - Shared state (thread-safe)                       │
│  - Flask HTTP server (:8765)                        │
└─────────────────────────────────────────────────────┘
         ▲
         │ HTTP
         │
    Any AI Agent
```
