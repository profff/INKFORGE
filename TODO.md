# InkForge - TODO

## En cours : Environnement de dev reMarkable

### Simulateur Docker rM2
- [ ] Builder l'image Docker rM-docker
- [ ] Tester le lancement de l'émulateur
- [ ] Valider l'affichage via rm2fb-emu

### Commandes

**Build complet (avec affichage rm2fb) :**
```bash
docker build --tag rm-docker https://github.com/timower/rM-docker.git
```

**Build minimal (si échec) :**
```bash
docker build --target qemu-base --tag rm-docker https://github.com/timower/rM-docker.git
```

**Lancer l'émulateur :**
```bash
docker run --rm -v rm-data:/opt/root -p 2222:22 -p 8888:8888 -it rm-docker
```

**Connexion SSH :**
```bash
ssh root@localhost -p 2222
# pas de mot de passe
```

### Ressources
- [rM-docker](https://github.com/timower/rM-docker) - Émulateur utilisé
- [remarkable-simulation](https://github.com/monsterstreet/remarkable-simulation) - Alternative minimale
- [rmkit](https://rmkit.dev/) - Framework pour dev apps rM

---

## Backlog

### Axe 1 : INPUT (Croquis → Code)
- [ ] Intégrer Claude Vision pour analyser les dessins
- [ ] Créer les prompts pour UML → Code, Wireframe → UI, etc.

### Axe 2 : APPS (Dev pour rM)
- [ ] Tester rmkit sur l'émulateur
- [ ] Créer une app hello world

### Axe 3 : OUTPUT (Claude → SVG)
- [ ] Pipeline SVG → PNG/PDF → reMarkable

### Axe 4 : THINKING (Réflexion assistée)
- [ ] Workflow capture notes → Claude → retour annoté

### Axe 5 : HUB (Supervision multi-instances)
- [ ] Architecture broker WebSocket
- [ ] Client reMarkable
- [ ] Client Android
