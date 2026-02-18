#!/usr/bin/env python3
"""
INKFORGE MCP Server - Exposes INKFORGE Lite API to Claude Code

This MCP server wraps the HTTP API of INKFORGE Lite, allowing Claude Code
to interact with the visual canvas via MCP tools.

Environment Variables:
    INKFORGE_API: Base URL of INKFORGE Lite (default: http://127.0.0.1:8765)

Usage:
    python inkforge_mcp.py
"""

import os
import subprocess
import sys
import time
from pathlib import Path

import requests
from fastmcp import FastMCP

# API endpoint - configurable for remote instances
API = os.getenv("INKFORGE_API", "http://127.0.0.1:8765")

mcp = FastMCP("INKFORGE")


def is_local() -> bool:
    """Check if API is pointing to localhost."""
    return "127.0.0.1" in API or "localhost" in API


def api_get(endpoint: str, timeout: float = 5.0) -> dict:
    """Make a GET request to the INKFORGE API."""
    try:
        r = requests.get(f"{API}{endpoint}", timeout=timeout)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


def api_post(endpoint: str, data: dict = None, timeout: float = 5.0) -> dict:
    """Make a POST request to the INKFORGE API."""
    try:
        r = requests.post(f"{API}{endpoint}", json=data or {}, timeout=timeout)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}


@mcp.tool
def inkforge_status() -> dict:
    """Check if INKFORGE Lite is running and get its status.

    Returns:
        dict with status info or error if not running
    """
    result = api_get("/status", timeout=2.0)
    if "error" in result:
        return {"running": False, "error": result["error"]}
    return {"running": True, **result}


@mcp.tool
def inkforge_open() -> dict:
    """Launch INKFORGE Lite if not already running.

    Only works when API is configured for localhost.
    For remote instances, returns an error asking user to start manually.

    Returns:
        dict with success status or error
    """
    # Check if already running
    status = api_get("/status", timeout=1.0)
    if "error" not in status:
        return {"ok": True, "message": "INKFORGE Lite is already running"}

    # Can only launch locally
    if not is_local():
        return {
            "ok": False,
            "error": f"INKFORGE Lite is not running on {API}. Please start it manually on the remote device."
        }

    # Find inkforge.py relative to this script
    script_dir = Path(__file__).parent
    inkforge_py = script_dir / "inkforge.py"

    if not inkforge_py.exists():
        return {"ok": False, "error": f"inkforge.py not found at {inkforge_py}"}

    # Launch in background
    try:
        subprocess.Popen(
            [sys.executable, str(inkforge_py)],
            cwd=str(script_dir),
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            creationflags=subprocess.CREATE_NEW_PROCESS_GROUP if sys.platform == "win32" else 0
        )
    except Exception as e:
        return {"ok": False, "error": f"Failed to launch: {e}"}

    # Wait for server to be ready
    for _ in range(20):  # 10 seconds max
        time.sleep(0.5)
        status = api_get("/status", timeout=1.0)
        if "error" not in status:
            return {"ok": True, "message": "INKFORGE Lite started successfully"}

    return {"ok": False, "error": "INKFORGE Lite started but not responding after 10s"}


@mcp.tool
def inkforge_snapshot() -> dict:
    """Get the current canvas as a base64 PNG image.

    Returns:
        dict with 'current' (base64 PNG), 'previous' (base64 PNG), and 'timestamp'
    """
    return api_get("/snapshot")


@mcp.tool
def inkforge_draw(svg: str) -> dict:
    """Inject SVG into the INKFORGE canvas.

    The SVG will be rendered and displayed on the canvas.

    Args:
        svg: SVG string to display (can include <svg> tag or just content)

    Returns:
        dict with 'ok' and 'version' on success, or 'error'
    """
    return api_post("/draw", {"svg": svg})


@mcp.tool
def inkforge_changed() -> dict:
    """Check if the canvas has been modified since the last acknowledgment.

    Returns:
        dict with 'changed' (bool), 'regions' (list of modified areas), 'timestamp'
    """
    return api_get("/changed")


@mcp.tool
def inkforge_clear() -> dict:
    """Clear the canvas and reset all state.

    Returns:
        dict with 'ok' on success
    """
    return api_post("/clear")


@mcp.tool
def inkforge_ack() -> dict:
    """Acknowledge changes - reset the changed flag and regions list.

    Call this after processing user's drawing to reset the change detection.

    Returns:
        dict with 'ok' on success
    """
    return api_post("/ack")


@mcp.tool
def inkforge_watch(interval_seconds: int = 3, timeout_seconds: int = 60) -> dict:
    """Wait for the user to draw something on the canvas.

    Polls the canvas for changes and returns when the user has drawn something
    or when the timeout is reached.

    Args:
        interval_seconds: How often to check for changes (default: 3)
        timeout_seconds: Maximum time to wait (default: 60)

    Returns:
        dict with snapshot if user drew something, or timeout message
    """
    start = time.time()

    # First, acknowledge any existing changes to start fresh
    api_post("/ack")

    while time.time() - start < timeout_seconds:
        result = api_get("/changed", timeout=2.0)

        if "error" in result:
            return {"ok": False, "error": result["error"]}

        if result.get("changed"):
            # User drew something - get the snapshot
            snapshot = api_get("/snapshot")
            return {
                "ok": True,
                "changed": True,
                "snapshot": snapshot,
                "regions": result.get("regions", [])
            }

        time.sleep(interval_seconds)

    return {
        "ok": True,
        "changed": False,
        "message": f"No changes detected after {timeout_seconds} seconds"
    }


if __name__ == "__main__":
    mcp.run()
