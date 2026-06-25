# co-coach — Diagramas do Sistema

> Renderiza automaticamente no GitHub. No VS Code, instale a extensão **Markdown Preview Mermaid Support**.

---

## 1. Visão geral — as 3 camadas

```mermaid
graph TD
    subgraph INPUT["📥 Entrada de conteúdo"]
        A1[iOS Shortcut\ncompartilha URL]
        A2[GitHub Stars\nsemanais]
        A3[Issue manual\nno GitHub]
    end

    subgraph KB["🗂️ Knowledge Base (kb/)"]
        B1[scripts/ingest.py\nClaude Haiku sumariza]
        B2[Arquivo .md\ncom frontmatter YAML]
    end

    subgraph FEED["📱 Feed Mobile"]
        C1[scripts/build-site.py]
        C2[docs/index.html\n+ knowledge-base.json]
        C3[GitHub Pages\nvictorauad.github.io/co-coach]
    end

    subgraph SKILLS["🛠️ Hub de Skills"]
        D1[skills/co-coach-*/\nSKILL.md]
        D2[sync-skills.yml\nGitHub Actions]
        D3[Repos registrados\niracing_analysis · alamtoco]
    end

    A1 -->|cria Issue com\nlabel add-link| A3
    A2 -->|workflow semanal| B1
    A3 -->|ingest-link.yml\ndispara| B1
    B1 --> B2
    B2 -->|push em kb/| C1
    C1 --> C2
    C2 --> C3

    D1 -->|push em skills/| D2
    D2 -->|GitHub API| D3

    style INPUT fill:#e8f4f8,stroke:#4a9eca
    style KB fill:#fff3e0,stroke:#f5a623
    style FEED fill:#e8f5e9,stroke:#4caf50
    style SKILLS fill:#f3e5f5,stroke:#9c27b0
```

---

## 2. Fluxo de ingestão de conteúdo

```mermaid
sequenceDiagram
    actor Victor
    participant iPhone
    participant GitHub
    participant Actions as GitHub Actions
    participant Script as scripts/ingest.py
    participant Claude as Claude Haiku API
    participant Repo as Repositório (kb/ + docs/)
    participant Feed as GitHub Pages

    Victor->>iPhone: Compartilha URL
    iPhone->>GitHub: POST Issues API\n(label: add-link)
    GitHub->>Actions: Dispara ingest-link.yml
    Actions->>Script: Executa com INPUT_URL
    Script->>Script: Fetch do HTML / transcrição YT
    Script->>Claude: Envia conteúdo para sumarização
    Claude-->>Script: Retorna titulo, tema, bullets, importancia
    Script->>Repo: Salva kb/YYYY-MM-DD-slug.md
    Actions->>Script: Executa build-site.py
    Script->>Repo: Atualiza docs/index.html\n+ knowledge-base.json
    Actions->>GitHub: git push (commit automático)
    Actions->>GitHub: Fecha Issue com comentário ✅
    GitHub->>Feed: GitHub Pages publica docs/
    Feed-->>Victor: Card aparece no feed (~2 min)
```

---

## 3. Fluxo de distribuição de skills

```mermaid
flowchart LR
    subgraph COACH["co-coach (hub central)"]
        S1[skills/co-coach-*/\nSKILL.md]
        S2[config/\nsync-targets.yml]
        S3[sync-skills.yml]
        S4[setup-project.yml]
    end

    subgraph TRIGGER["Gatilhos"]
        T1[Push em\nskills/** no main]
        T2[Workflow manual\nvia Actions UI]
    end

    subgraph REPOS["Repos registrados"]
        R1[victorauad/\niracing_analysis]
        R2[victorauad/\nalamtoco]
        R3[victorauad/\nnovo-projeto ...]
    end

    subgraph DESTINO[".claude/ em cada repo"]
        D1[skills/co-coach-*/\nSKILL.md]
        D2[settings.json]
        D3[memory/]
    end

    T1 -->|dispara| S3
    T2 -->|onboarding\nde novo repo| S4

    S3 --> S2
    S2 -->|lista repos| S3
    S3 -->|GitHub API PUT\npara cada skill| R1
    S3 -->|GitHub API PUT\npara cada skill| R2

    S4 -->|instala skills +\nsettings + memory/| R3
    S4 -->|adiciona ao\nsync-targets.yml| S2

    R1 --> D1
    R2 --> D1
    R3 --> D1
    R3 --> D2
    R3 --> D3

    style COACH fill:#f3e5f5,stroke:#9c27b0
    style TRIGGER fill:#e8f4f8,stroke:#4a9eca
    style REPOS fill:#fff3e0,stroke:#f5a623
    style DESTINO fill:#e8f5e9,stroke:#4caf50
```
