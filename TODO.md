# INKFORGE - TODO

## En cours : POC Visual Loop

### Phase 1 : Setup ✅
- [x] Setup canvas HTML5 (sans tldraw pour l'instant)
- [x] Configurer Claude API (Vision)
- [ ] Commander tablette Wacom (Intuos S ou M)

### Phase 2 : Premier loop ✅
- [x] Capturer le canvas → export PNG
- [x] Envoyer à Claude Vision
- [x] Afficher la réponse texte
- [x] Claude génère SVG → render dans le canvas
- [x] Auto-send avec debounce
- [x] Position tracking + injection positionnée

### Phase 3 : Conversation ✅
- [x] Multi-turn (historique des échanges)
- [x] Apprentissage des conventions utilisateur
- [x] Sélecteur d'intention (ajouter/modifier/supprimer/expliquer)
- [x] UI 3 panneaux (prompt envoyé, analyse, chat)

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
