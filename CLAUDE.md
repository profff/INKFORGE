# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**INKFORGE** is an ecosystem for AI-assisted development centered around the reMarkable tablet. The project has 5 axes:

1. **INPUT** - Transform reMarkable sketches (UML, flowcharts, wireframes) into code using Claude Vision
2. **APPS** - Develop native applications that run on reMarkable (rmkit, Qt, Rust, etc.)
3. **OUTPUT** - Claude generates SVG/diagrams to display on reMarkable
4. **THINKING** - Use reMarkable as a brainstorming surface with AI assistance
5. **HUB** - Mobile project management hub to supervise multiple Claude Code instances

## Project Status

Early stage - mostly documentation and planning.

## Quick Commands

```bash
# Initialize submodule (first time)
git submodule update --init --recursive

# Build base emulator image
docker build --tag rm-docker https://github.com/timower/rM-docker.git

# Build custom image with SSH (get key first: cat docker/ssh/rm-emulator.pub | base64 -w0)
docker build --build-arg "SSH_PUBLIC_KEY_B64=<base64_key>" -t rm-docker-ssh docker/

# Run emulator with X11 display (start XLaunch first with "Disable access control")
docker run --rm -d --name rm-emulator -v rm-data:/opt/root -p 2222:22 -e DISPLAY=host.docker.internal:0.0 rm-docker-ssh

# Run emulator SSH-only (headless)
docker run --rm -d --name rm-emulator -v rm-data:/opt/root -p 2222:22 rm-docker-ssh

# SSH into emulator
ssh rm-emu

# Stop emulator
docker stop rm-emulator
```

## Development Environment

### SSH Config Required

Add to `~/.ssh/config`:
```
Host rm-emu
    HostName localhost
    Port 2222
    User root
    IdentityFile C:/Users/o.gaste/.ssh/rm-emulator
    IdentitiesOnly yes
    StrictHostKeyChecking no
```

SSH key (no passphrase): `docker/ssh/rm-emulator`

### Key Frameworks for reMarkable Development

| Framework | Language | Use Case |
|-----------|----------|----------|
| rmkit | C++ | Main framework, native refresh support |
| libreMarkable | Rust | Rust apps with native refresh |
| Qt (SDK) | C++ | Official SDK framework |
| Carta | Python | Python development |

## Key Files

- `INKFORGE.md` - Complete project vision and architecture documentation
- `TODO.md` - Current tasks and backlog

## External Resources

- [rM-docker](https://github.com/timower/rM-docker) - reMarkable emulator
- [rmkit](https://rmkit.dev/) - Primary app development framework
- [reMarkable SDK](https://developer.remarkable.com/documentation/sdk) - Official SDK
- [remarkable.guide](https://remarkable.guide/) - Community development guide
