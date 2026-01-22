# INKFORGE - TODO

## En cours : INKFORGE Lite

### Phase 5 : Standalone Canvas ✅
- [x] Canvas standalone avec API HTTP (Flask + pywebview)
- [x] Interface frameless minimaliste
- [x] 3 LEDs status (connecté, modifié, zones toggle)
- [x] Dessin : clic gauche/droit, molette pour taille
- [x] Auto-inject SVG depuis API /draw
- [x] Visual loop bidirectionnelle fonctionnelle
- [x] Window drag sur titlebar custom

### Phase 6 : Intégration Claude Code 🔜
- [ ] MCP server pour exposer les endpoints à Claude
- [ ] Commande `/sketch` pour ouvrir INKFORGE Lite
- [ ] Claude peut voir le canvas et répondre en SVG
- [ ] Workflow : sketch → analyse → code generation

---

## Historique POC

### Phase 1-3 : Visual Loop POC ✅
- Setup canvas HTML5 + Claude Vision
- Capture → envoi → réponse SVG
- Multi-turn, conventions, intentions
- UI 3 panneaux

### Phase 4 : Architecture & Concepts 🔜
- [ ] **Séparer les couches conceptuelles :**
  - Sujet de fond (le domaine : UML, todolist, wireframe...)
  - Forme (la représentation : SVG, texte, Mermaid...)
  - Méthode de travail (comment on itère : focus, comparaison...)
  - Actions/Intentions (ajouter, modifier, supprimer, annoter...)
- [ ] Définir une architecture modulaire pour ces concepts
- [ ] Agent dédié "intent detector" vs agent "content generator" ?

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
