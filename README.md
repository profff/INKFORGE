# INKFORGE

> Visual Thinking with AI — a bidirectional visual dialogue loop between humans and LLMs.

You sketch, the AI responds visually. You iterate, it refines. No more text-only conversations for visual ideas.

```
     ┌──────────┐                      ┌──────────┐
     │  HUMAN   │ ────── sketch ─────► │    AI    │
     │          │ ◄───── sketch ────── │          │
     └──────────┘                      └──────────┘
           │                                │
           └──────────── ITERATE ───────────┘
```

## INKFORGE Lite

A lightweight, standalone visual canvas with an HTTP API. Any AI agent can see what you draw and respond with SVG — no vendor lock-in.

- **Draw** with mouse or stylus (freehand, erase, color picker)
- **HTTP API** at `localhost:8765` — simple REST endpoints
- **MCP Server** — integrates directly into Claude Code as a tool
- **Cross-platform** — runs on Windows, macOS, Linux (Python + HTML5)

### Quick Start

```bash
cd inkforge-lite
pip install -r requirements.txt
python inkforge.py
```

The canvas opens. An API is available at `http://127.0.0.1:8765`.

### With Claude Code (MCP)

```bash
cp .mcp.json.example .mcp.json
# Edit .mcp.json to point to your Python path if needed
```

Claude Code can then use `inkforge_open`, `inkforge_snapshot`, `inkforge_draw`, and other tools to interact with the canvas.

### API

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/status` | GET | Health check |
| `/snapshot` | GET | Canvas as base64 PNG |
| `/changed` | GET | Check for user modifications |
| `/draw` | POST | Inject SVG onto canvas |
| `/clear` | POST | Reset canvas |
| `/ack` | POST | Acknowledge changes |

See [inkforge-lite/README.md](inkforge-lite/README.md) for detailed API docs and examples.

## What's Next

The current canvas is a flat surface. The next step is to separate the visual loop into three independent layers:

```
  ┌─────────────────────────────────────────────┐
  │  FOND       what you're working on          │
  │             UML, wireframe, todolist, math   │
  ├─────────────────────────────────────────────┤
  │  FORME      how it's represented            │
  │             SVG, Mermaid, ASCII, code        │
  ├─────────────────────────────────────────────┤
  │  INTENTIONS what you want to do             │
  │             add, modify, delete, annotate    │
  └─────────────────────────────────────────────┘
```

This separation lets the AI understand *what* you're sketching, *how* to represent it, and *what action* you're requesting — instead of treating every stroke as raw pixels.

**Vector canvas** — Replace the raster canvas with SVG strokes (via `perfect-freehand`). A simplification slider lets you go from raw freehand to clean, simplified polylines. The AI receives vector data instead of pixels — lighter, more semantic, easier to reason about.

```
  raw strokes ──────────────────────── clean vectors
  ●∿∿∿∿∿●        simplify ──►         ●────────●
  (raster PNG)                         (SVG paths)
```

**Autonomous loop** — Today the user must tell the AI "I drew something". The goal is a fully reactive loop: the canvas detects when you stop drawing and triggers the AI automatically — no text prompt needed, pure visual dialogue.

See [INKFORGE.md](INKFORGE.md) for the full project vision.

## License

MIT
