# INKFORGE

> Visual Thinking with AI - La boucle de dialogue visuel humain-IA

## Vision

**INKFORGE** est une plateforme de dialogue visuel bidirectionnel avec l'IA. Le concept central : une **conversation continue par le croquis** où l'humain et l'IA échangent visuellement.

```
┌─────────────────────────────────────────────────────────────┐
│                      THE LOOP                               │
│                                                             │
│     ┌──────────┐                      ┌──────────┐         │
│     │  HUMAN   │ ────── sketch ─────► │    AI    │         │
│     │          │ ◄───── sketch ────── │          │         │
│     └──────────┘                      └──────────┘         │
│          │                                  │               │
│          ▼                                  ▼               │
│    Tu griffonnes                    Claude répond           │
│    une idée vague          ───►     avec un diagramme      │
│                                     structuré               │
│          │                                  │               │
│          └──────────── ITERATE ─────────────┘               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Ce qui existe vs. ce qui manque

| Catégorie | Outils existants | Limitation |
|-----------|------------------|------------|
| Sketch → Code | tldraw "Make Real", Visily | Unidirectionnel |
| AI → Diagram | DiagramGPT, Miro AI, Whimsical | Unidirectionnel |
| Whiteboards | Excalidraw, tldraw, Miro | Pas de loop AI natif |
| Smart pens | XNote, Flowtica Scribe | Hardware propriétaire |

**Le gap** : Personne n'a fait la **boucle complète** - une conversation visuelle continue où l'humain et l'IA itèrent ensemble sur des idées.

## Architecture

```
INKFORGE
├── Core: Visual Loop Engine
│   ├── Stroke capture → Claude Vision
│   ├── Claude response → SVG/Mermaid render
│   └── State management (conversation history)
│
├── Inputs (hardware-agnostic)
│   ├── Wacom tablet (recommandé pour desktop)
│   ├── tldraw canvas (web, souris/touch)
│   ├── iPad + Apple Pencil
│   ├── reMarkable (e-ink, portable)
│   └── Any stylus-enabled device
│
└── Outputs
    ├── SVG (scalable, editable)
    ├── Mermaid (flowcharts, sequence, ERD)
    ├── PNG (for display)
    └── Code (quand pertinent)
```

## Cas d'usage

### La Boucle en action

| Tu dessines... | Claude répond avec... | Tu itères... |
|----------------|----------------------|--------------|
| Idée vague en bullets | Mind map structurée (SVG) | Tu annotes, il affine |
| Wireframe rough | Version propre + suggestions UX | Tu corriges, il génère le code |
| Architecture floue | Diagramme technique + questions | Tu précises, il détaille |
| Flowchart incomplet | Version complète + edge cases | Tu valides, il implémente |
| Équation griffonnée | Visualisation + code NumPy | Tu ajustes les params |

### Modes de conversation

1. **Brainstorm** - Idées brutes → structuration progressive
2. **Design** - Wireframes → UI components
3. **Architecture** - Schémas → Infrastructure as Code
4. **Debug** - Croquis du problème → analyse + solution
5. **Documentation** - Concepts → diagrammes techniques

## Stack technique

### Option A : tldraw-based (web)

```yaml
Frontend:
  - tldraw SDK (React)
  - Canvas interception des strokes
  - Render SVG/Mermaid inline

Backend:
  - Claude API (Vision + Text)
  - WebSocket pour real-time
  - State: conversation + canvas history

Integration:
  - npm: @tldraw/tldraw
  - License: watermark ou commercial
```

### Option B : Desktop app (Wacom native)

```yaml
App:
  - Electron ou Tauri
  - Wacom SDK pour pressure/tilt
  - Canvas custom ou tldraw embedded

AI:
  - Claude API direct
  - Local processing pour latence

Avantages:
  - Meilleure intégration stylus
  - Pas de watermark
  - Mode offline possible
```

### Option C : Hybrid

```yaml
Web canvas (tldraw) + Desktop bridge pour Wacom
- tldraw pour le rendering
- Driver Wacom natif pour l'input
- Best of both worlds
```

## Roadmap

### Phase 1 : POC
- [ ] tldraw + Claude Vision basique
- [ ] Capture canvas → envoi à Claude → affichage réponse
- [ ] Test avec souris (en attendant tablette)

### Phase 2 : Loop
- [ ] Conversation history (multi-turn)
- [ ] Claude génère SVG inline dans le canvas
- [ ] Annotations sur la réponse de Claude

### Phase 3 : Hardware
- [ ] Intégration Wacom (pressure, tilt)
- [ ] Optimisation latence
- [ ] Mode "drawing area" mappé sur le canvas

### Phase 4 : Polish
- [ ] Templates de conversation (brainstorm, design, archi)
- [ ] Export (PDF, PNG, code)
- [ ] Historique des sessions

## Capacités de Claude (référence)

### Ce que Claude sait générer

| Format | Usage | Qualité |
|--------|-------|---------|
| SVG | Diagrammes, icônes, formes | Excellent pour l'abstrait |
| Mermaid | Flowcharts, séquence, ERD, Gantt | Très bon |
| ASCII | Schémas textuels | Bon |
| Code | React components, algorithmes | Excellent |

### Limitations

- Pas de photoréalisme
- Objets du monde réel approximatifs
- Esthétique géométrique/technique

## Références

### Outils de référence
- [tldraw](https://www.tldraw.com/) - Whiteboard SDK, "Make Real" demo
- [Excalidraw](https://excalidraw.com/) - Whiteboard collaboratif
- [DiagramGPT](https://www.eraser.io/diagramgpt) - AI diagram generation
- [Miro AI](https://miro.com/ai/) - Whiteboard + AI
- [Whimsical AI](https://whimsical.com/ai) - Diagrams from text

### Recherche
- [Code Shaping (CHI 2025)](https://uwaterloo.ca/computer-science/news/new-ai-system-turns-sketches-code) - Sketch-to-code research

### Hardware
- [Wacom](https://www.wacom.com/) - Tablettes graphiques de référence
- [reMarkable](https://remarkable.com/) - E-ink tablet (portable option)

---

## Annexe : reMarkable (optional target)

Si tu veux cibler reMarkable comme device portable :

### Avantages
- E-ink (confort visuel, outdoor)
- Distraction-free
- Sensation papier

### Contraintes
- Écosystème fermé
- Refresh rate lent
- Dev natif complexe (rmkit, SDK Yocto)

### Ressources
- [rM-docker](https://github.com/timower/rM-docker) - Émulateur
- [rmkit](https://rmkit.dev/) - Framework apps
- [remarkable.guide](https://remarkable.guide/) - Community guide

Le support reMarkable peut être ajouté comme "output adapter" une fois le core loop fonctionnel.
