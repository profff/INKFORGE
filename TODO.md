# INKFORGE - TODO

## En cours : POC Visual Loop

### Phase 1 : Setup
- [ ] Commander tablette Wacom (Intuos S ou M)
- [ ] Setup projet tldraw + React
- [ ] Configurer Claude API (Vision)

### Phase 2 : Premier loop
- [ ] Capturer le canvas tldraw → export PNG
- [ ] Envoyer à Claude Vision
- [ ] Afficher la réponse texte
- [ ] Claude génère SVG → render dans le canvas

### Phase 3 : Conversation
- [ ] Multi-turn (historique des échanges)
- [ ] Annotations sur les réponses de Claude
- [ ] Modes de conversation (brainstorm, design, archi)

---

## Backlog

### Hardware
- [ ] Intégration Wacom native (pressure/tilt)
- [ ] Test iPad + Apple Pencil (via web)
- [ ] Adapter pour reMarkable (optional)

### Features
- [ ] Templates de conversation
- [ ] Export sessions (PDF, PNG)
- [ ] Historique persistant

### Infra
- [ ] Décider : tldraw watermark vs licence vs custom canvas
- [ ] CI/CD si app desktop (Electron/Tauri)

### Auth & API (important UX)
- [ ] Détecter OAuth Claude Code existant (~/.claude/)
- [ ] Détecter ANTHROPIC_API_KEY dans l'environnement
- [ ] Support des clés API manuelles (fallback)
- [ ] Zéro friction : l'utilisateur ne devrait pas avoir à créer de compte supplémentaire

---

## Notes

**Pivot 2025-01** : Focus sur la boucle visuelle bidirectionnelle, hardware-agnostic. reMarkable devient un target optionnel, pas le centre du projet.
