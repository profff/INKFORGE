# InkForge

> Du croquis au code - Transforme tes dessins reMarkable en code avec Claude

## Vision

**InkForge** est un écosystème de développement centré sur la tablette reMarkable avec trois axes :

### 1. 🎨 Coder PAR le croquis (Input)
Utiliser Claude Code avec des schémas et croquis manuscrits comme input pour générer du code.

### 2. 📱 Coder POUR reMarkable (Apps)
Développer des applications natives et des outils qui tournent directement sur la tablette reMarkable.

### 3. ✏️ Claude DESSINE pour toi (Output)
Claude génère des croquis, diagrammes et visualisations SVG directement affichables sur la reMarkable.

### 4. 🧠 reMarkable comme Espace de Réflexion (Thinking)
Utiliser la reMarkable comme surface de brainstorming où Claude t'aide à clarifier, structurer et développer tes idées.

### 5. 📂 Hub de Projets Mobile (Projects)
Accéder à tous tes projets de développement depuis la reMarkable, même sans terminal ni VSCode. Un tableau de bord portable pour gérer, visualiser et interagir avec ton code.

```
                              ┌─────────────────────────────────────┐
                              │            INKFORGE                 │
                              └─────────────────────────────────────┘
                                              │
    ┌──────────────┬──────────────┬───────────┴───────────┬──────────────┬──────────────┐
    │              │              │                       │              │              │
    ▼              ▼              ▼                       ▼              ▼              ▼
┌────────┐   ┌────────┐   ┌────────────┐   ┌────────────┐   ┌────────┐   ┌────────────┐
│📥 INPUT│   │📱 APPS │   │ 📤 OUTPUT  │   │🧠 THINKING │   │📂 HUB  │   │  🔄 LOOP   │
│Croquis→│   │Dev pour│   │ Claude →   │   │ Réflexion  │   │Projets │   │  Dialogue  │
│Code    │   │  rM    │   │ Croquis    │   │ Assistée   │   │ Mobile │   │  Continu   │
└────────┘   └────────┘   └────────────┘   └────────────┘   └────────┘   └────────────┘
     │            │              │                │              │              │
     ▼            ▼              ▼                ▼              ▼              ▼
Tu dessines  Apps rmkit    Claude génère    Brainstorm +   Accès repos   Itération
UML/Flow     Qt, Rust      SVG/Diagrams     Structuration  TODOs, PRs    permanente
→ Code       .NET, Go      → reMarkable     Clarification  Issues, Code  rM ↔ Claude
```

## Cas d'Usage

| Tu dessines...           | Claude génère...                          |
|--------------------------|-------------------------------------------|
| Diagramme de classes UML | Classes TypeScript/Python avec relations  |
| Flowchart algorithme     | Fonction avec la logique correspondante   |
| Wireframe UI             | Composants React/Vue                      |
| Schéma d'architecture    | Infrastructure as Code (Terraform)        |
| Équations mathématiques  | Code NumPy/algorithme                     |
| Schéma BDD (ERD)         | Migrations SQL / Prisma schema            |

## Architecture Technique

### Composants

```
inkforge/
├── mcp-server/
│   ├── remarkable_connector.py   # SSH ou Cloud API
│   ├── vision_processor.py       # OCR + interprétation diagrammes
│   └── claude_bridge.py          # Envoi à Claude Code
├── prompts/
│   ├── diagram_to_code.md        # Prompts pour UML → Code
│   ├── wireframe_to_ui.md        # Croquis → React/HTML
│   └── flowchart_to_logic.md     # Flowchart → Algorithme
└── templates/
    └── remarkable_templates/     # Templates pour dessiner
```

### Capture depuis reMarkable

| Méthode         | Avantage                              |
|-----------------|---------------------------------------|
| SSH direct      | Temps réel, pas d'abonnement Connect  |
| remarkable-mcp  | Déjà conçu pour intégration IA        |
| Export PDF/PNG  | Simple, compatible avec l'OCR         |

### Interprétation des Croquis

- **Google Cloud Vision** - Excellent pour le manuscrit
- **Gemini Vision / Claude Vision** - Comprend les diagrammes et schémas
- **Code Shaping (CHI 2025)** - Recherche sur annotations manuscrites → code

### Workflow

1. **Sur reMarkable** : Dessiner un diagramme de classes, flowchart, ou wireframe UI
2. **Synchronisation** : Détection des changements (SSH watch ou webhook)
3. **Analyse** : Claude Vision interprète le croquis
4. **Génération** : Claude Code génère le code correspondant
5. **Feedback** : Code renvoyé en PDF annoté sur la reMarkable

## APIs & Ressources reMarkable

### API Cloud Officielle

- REST + JSON
- Authentification via code à usage unique → Device Token
- Documentation : https://developer.remarkable.com/

### Accès SSH

La tablette tourne sous Linux avec SSH actif par défaut. Le mot de passe root est accessible dans les paramètres.

### Bibliothèques Disponibles

| Langage    | Outil                  | Description                    |
|------------|------------------------|--------------------------------|
| Node.js    | remarkable-tablet-api  | Upload/download via le cloud   |
| Python     | reMarkable-layers      | Lecture/écriture format Lines  |
| TypeScript | reMarkable-typescript  | API pour reMarkable Cloud      |
| C++        | lines-are-beautiful    | API fichiers                   |
| Rust       | lines-are-rusty        | API fichiers                   |
| Go         | rmapi                  | CLI populaire                  |

### Projets Connexes

- **remarkable-mcp** : Serveur MCP pour accès IA aux documents
- **RMfuse** : Système de fichiers FUSE pour le cloud
- **rmfakecloud** : Cloud auto-hébergé alternatif
- **google-drive-remarkable-sync** : Sync Google Drive → reMarkable

## Outils IA à Intégrer

| Outil              | Rôle                                |
|--------------------|-------------------------------------|
| remarkable-mcp     | Serveur MCP pour accès aux documents|
| Visily             | Sketch → Wireframe interactif       |
| DiagramGPT (Eraser)| Génération de diagrammes techniques |
| Google Stitch      | Sketch → HTML/CSS                   |
| Claude Vision      | Interprétation multimodale          |

---

## Axe 2 : Développer POUR reMarkable

### Environnement de Développement

La reMarkable est une tablette Linux avec SSH activé par défaut. Elle supporte le développement d'applications natives.

### SDK Officiel

reMarkable fournit un SDK basé sur Yocto contenant :
- Cross-compiler toolchain
- Bibliothèques partagées
- Headers pour compilation croisée

📖 Documentation : https://developer.remarkable.com/documentation/sdk

> **Note** : Le "Developer Mode" est requis pour reMarkable Paper Pro. Pas nécessaire pour rM1/rM2.

### Frameworks de Développement

| Framework | Langage | Description |
|-----------|---------|-------------|
| **[rmkit](https://rmkit.dev/)** | C++ | Framework principal, batteries-included, refresh natif |
| **libreMarkable** | Rust | Framework avec support refresh natif |
| **Qt (SDK officiel)** | C++ | Framework officiel via le SDK |
| **ReMarkable.NET** | C#/.NET | Pour les développeurs .NET |
| **Liboxide** | C++ | Alternative à rmkit |
| **Carta** | Python | Développement en Python |
| **Simple App Script (SAS)** | Node.js | Scripts simples |
| **Go Simple** | Go | Applications en Go |

### Installation d'Apps

```bash
# Installer Toltec (gestionnaire de paquets communautaire)
# https://toltec-dev.org/

# Puis utiliser opkg
opkg install <nom-app>
```

### Ressources Dev

- [remarkable.guide](https://remarkable.guide/devel/index.html) - Guide de développement
- [rmkit.dev](https://rmkit.dev/) - Documentation rmkit
- [Oxide Application Tutorial](https://eeems.website/writing-a-simple-oxide-application/) - Tutoriel app simple
- [remarkablewiki.com/devel](https://remarkablewiki.com/devel/start) - Wiki développeurs

---

## Axe 3 : Claude Génère des Croquis

### Capacités de Claude

Claude peut générer des visualisations via :
- **SVG** : Formes géométriques, icônes, diagrammes techniques
- **Mermaid** : Flowcharts, diagrammes de séquence, ERD
- **ASCII Art** : Schémas textuels

### Points Forts

- Excellent pour les diagrammes géométriques/abstraits
- Haute précision dans l'expression de l'information
- Support des animations SVG
- Génération de flowcharts et workflows

### Limitations

- Pas de génération d'images photoréalistes
- Difficultés avec certains objets du monde réel
- Esthétique basique (formes géométriques)

### Pipeline Claude → reMarkable

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│    Claude    │────▶│  SVG/PNG     │────▶│  reMarkable  │
│  génère SVG  │     │  conversion  │     │  affichage   │
└──────────────┘     └──────────────┘     └──────────────┘
```

### Cas d'Usage Output

| Tu demandes à Claude...        | Il génère...                    |
|--------------------------------|---------------------------------|
| "Schéma architecture microservices" | Diagramme SVG des services |
| "Flowchart de cet algorithme"  | Mermaid/SVG du flow            |
| "Wireframe page login"         | SVG du wireframe               |
| "Diagramme de classes"         | UML en SVG                     |
| "Visualise cette structure de données" | Représentation graphique |

---

## Axe 4 : Espace de Réflexion Assistée

### Concept

La reMarkable devient un **second cerveau visuel** où tu peux :
- Griffonner des idées brutes
- Laisser Claude les analyser, structurer et enrichir
- Recevoir des clarifications, questions, et suggestions
- Itérer visuellement sur tes concepts

### Workflow de Réflexion

```
┌──────────────────────────────────────────────────────────────────────────┐
│                        BOUCLE DE RÉFLEXION                               │
└──────────────────────────────────────────────────────────────────────────┘

    ┌─────────┐         ┌─────────┐         ┌─────────┐         ┌─────────┐
    │ 1. NOTE │   ───▶  │ 2. SCAN │   ───▶  │ 3. IA   │   ───▶  │ 4. PUSH │
    │ Brouillon│        │ Capture │         │ Analyse │         │ Retour  │
    │ manuscrit│        │ + OCR   │         │ Claude  │         │ rM      │
    └─────────┘         └─────────┘         └─────────┘         └─────────┘
         │                                                            │
         │                                                            │
         └──────────────────────  ITÉRATION  ◀────────────────────────┘
```

### Cas d'Usage Réflexion

| Tu griffonnes...                | Claude répond...                              |
|---------------------------------|-----------------------------------------------|
| Idée vague en bullet points     | Structure en plan détaillé                    |
| Question ouverte                | Analyse multi-perspective + pour/contre       |
| Problème mal défini             | Reformulation claire + questions de clarification |
| Brainstorm chaotique            | Mind map structurée (SVG)                     |
| Notes de réunion                | Compte-rendu formaté + action items           |
| Croquis d'architecture          | Critique + suggestions d'amélioration         |
| Liste de features               | Priorisation + estimation de complexité       |

### Fonctionnalités de l'Assistant Réflexion

1. **Clarification** : "Tu mentionnes X, peux-tu préciser ce que tu entends par..."
2. **Structuration** : Transforme le chaos en hiérarchie claire
3. **Expansion** : "As-tu pensé à ces aspects : ..."
4. **Critique constructive** : Points forts/faibles de l'idée
5. **Connexions** : Liens avec tes notes précédentes
6. **Visualisation** : Génère des diagrammes pour clarifier
7. **Questions socratiques** : Pousse la réflexion plus loin

### Format de Réponse sur reMarkable

Claude peut renvoyer ses réflexions sous forme de :
- **PDF annoté** : Commentaires en marge de tes notes
- **Nouvelle page** : Synthèse structurée
- **Diagramme SVG** : Visualisation des concepts
- **Template rempli** : Mind map, canvas, matrices

### Intégration avec les Autres Axes

```
   🧠 THINKING                    📥 INPUT                     📤 OUTPUT
   ───────────                    ────────                     ─────────

   Idée brute          ───▶      Schéma validé       ───▶     Code généré
        │                              │                            │
        │                              │                            │
        └──────── Itération ◀──────────┴──────── Feedback ◀─────────┘
```

L'axe Thinking s'intègre naturellement :
- **Avant le code** : Clarifier l'architecture avant de dessiner l'UML
- **Pendant le dev** : Réfléchir aux edge cases, à la structure
- **Après le code** : Documenter, expliquer les décisions

---

## Axe 5 : Hub de Projets Mobile & Supervision Multi-Instances

### Le Problème

Tu as plusieurs projets en parallèle, des instances Claude Code qui tournent sur différentes machines (PC local, serveurs SSH), et tu veux pouvoir :
- Accéder à tout depuis ta reMarkable ou ton Android
- Superviser les agents Claude en cours d'exécution
- Interagir avec tes projets sans ouvrir VSCode/terminal

### Architecture Distribuée

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           INKFORGE CONTROL CENTER                               │
└─────────────────────────────────────────────────────────────────────────────────┘

                              ┌───────────────────┐
                              │   📱 HUB CENTRAL  │
                              │  (Android / rM)   │
                              │                   │
                              │  • Dashboard      │
                              │  • Notifications  │
                              │  • Quick Actions  │
                              └─────────┬─────────┘
                                        │
                    ┌───────────────────┼───────────────────┐
                    │                   │                   │
                    ▼                   ▼                   ▼
          ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
          │  🖥️ PC LOCAL    │ │  🌐 SERVEUR SSH │ │  ☁️ CLOUD VM    │
          │                 │ │                 │ │                 │
          │ Claude Code #1  │ │ Claude Code #2  │ │ Claude Code #3  │
          │ Projet: InkForge│ │ Projet: API-X   │ │ Projet: ML-Pipe │
          │ Status: Running │ │ Status: Waiting │ │ Status: Done    │
          └─────────────────┘ └─────────────────┘ └─────────────────┘
```

### Fonctionnalités du Hub Central

#### Sur reMarkable
| Fonction | Description |
|----------|-------------|
| **Dashboard Projets** | Vue d'ensemble de tous tes repos/projets |
| **Status Agents** | Voir les instances Claude actives et leur progression |
| **Quick Notes** | Griffonner une instruction → envoyée à un agent |
| **Review PRs** | Lire et annoter les PRs manuscritement |
| **TODOs Sync** | Tous tes TODOs de tous les projets |
| **Notifications** | Alertes quand un agent a besoin d'input |

#### Sur Android (App Companion)
| Fonction | Description |
|----------|-------------|
| **Push Notifications** | Agent terminé, erreur, besoin d'approbation |
| **Voice Commands** | "Claude, sur le projet X, ajoute une feature Y" |
| **Quick Approve** | Valider les PRs, les changements proposés |
| **Live Logs** | Voir ce que fait Claude en temps réel |
| **Remote Control** | Start/Stop/Pause des agents |

### Protocole de Communication

```
┌────────────┐     WebSocket/     ┌────────────┐     SSH/API      ┌────────────┐
│   Client   │ ◄──────────────► │   Broker   │ ◄───────────────► │   Agent    │
│  rM / 📱   │    Bidirectionnel  │  (Central) │   Tunnel sécurisé │  Claude    │
└────────────┘                    └────────────┘                   └────────────┘

Messages:
  → "agent:status" - Demande le status de tous les agents
  ← "agent:update" - Push du status d'un agent
  → "agent:command" - Envoyer une commande à un agent
  → "agent:input" - Répondre à une question d'un agent
  ← "agent:output" - Résultat d'une tâche
```

### Stack Technique Proposée

```yaml
Hub Central (Broker):
  - Runtime: Node.js / Go
  - Protocol: WebSocket + REST API
  - Auth: JWT + Device tokens
  - Storage: SQLite / PostgreSQL
  - Queue: Redis (pour les messages)

Client reMarkable:
  - Framework: rmkit (C++)
  - Comm: WebSocket client
  - Render: SVG/PDF pour les dashboards

Client Android:
  - Framework: Kotlin / Flutter
  - Notifications: Firebase Cloud Messaging
  - Background: WorkManager pour sync

Agent Claude (sur chaque machine):
  - Claude Code CLI avec hooks
  - Daemon de reporting (heartbeat + status)
  - API locale pour recevoir les commandes
```

### Workflow Multi-Projets

```
Matin sur reMarkable:
┌────────────────────────────────────────────────────────────────┐
│  📊 INKFORGE DASHBOARD              🔔 3 notifications         │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  PROJETS ACTIFS                                               │
│  ─────────────                                                │
│  [██████████] InkForge      ✅ PR ready for review            │
│  [████░░░░░░] API-Gateway   🔄 Claude working on auth...      │
│  [██████████] ML-Pipeline   ⏸️ Waiting for your input         │
│                                                                │
│  ACTIONS RAPIDES                                              │
│  ───────────────                                              │
│  [📝 Note → Agent]  [✓ Approve PR]  [👁️ View Logs]           │
│                                                                │
│  ✏️ Zone de croquis pour instructions...                      │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

### Sync avec GitHub/GitLab

```
┌──────────────┐         ┌──────────────┐         ┌──────────────┐
│   GitHub     │ ◄─────► │  Hub Central │ ◄─────► │  reMarkable  │
│   Issues     │  Webhook │   Aggregates │   Push  │   Dashboard  │
│   PRs        │         │   All repos  │         │   + Annotate │
│   Actions    │         │              │         │              │
└──────────────┘         └──────────────┘         └──────────────┘

Tu peux:
- Voir toutes les issues de tous tes repos
- Créer une issue en griffonnant sur rM
- Review PR avec annotations manuscrites
- Recevoir les alertes CI/CD
```

### Sécurité

- **Tunnels SSH** : Communication chiffrée avec les machines distantes
- **Zero Trust** : Chaque agent s'authentifie auprès du hub
- **Device Binding** : reMarkable/Android enregistrés avec tokens uniques
- **Audit Log** : Toutes les commandes sont loguées

---

## Références

- [awesome-reMarkable](https://github.com/reHackable/awesome-reMarkable) - Liste curatée des projets communautaires
- [ReMarkableAPI (splitbrain)](https://github.com/splitbrain/ReMarkableAPI) - Documentation API sync
- [remarkable-mcp](https://sam-morrow.com/blog/building-an-mcp-server-for-remarkable) - Serveur MCP existant
- [Code Shaping (CHI 2025)](https://uwaterloo.ca/computer-science/news/new-ai-system-turns-sketches-code) - Recherche sketch-to-code
- [DiagramGPT](https://www.eraser.io/diagramgpt) - Génération de diagrammes par IA
- [rmkit](https://rmkit.dev/) - Framework d'applications reMarkable
- [reMarkable SDK](https://developer.remarkable.com/documentation/sdk) - SDK officiel
- [remarkable.guide](https://remarkable.guide/) - Guide communautaire complet
- [Claude SVG Generation](https://medium.com/@joycebirkins/claude-artifacts-chatgpt-canvas-ai-text-based-visualization-svg-image-generation-1fc51d27c0a6) - Génération SVG avec Claude

## Noms de Projet Alternatifs

- **InkForge** - Forge ton code à l'encre 🔥
- **SketchFlow** - Du croquis au flow
- **InkToCode** - Simple et efficace
- **PaperStack** - Du papier au stack technique
- **DrawDev** - Dessine, développe
- **InkPilot** - Pilote ton code au stylet
- **CanvasCode** - La toile devient code
