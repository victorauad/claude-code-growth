# Status do Projeto — co-coach

> Atualizado em: 20/06/2026

---

## O que este projeto entrega

Um sistema com quatro funções integradas:
1. **Feed mobile** — webapp com cards de conteúdo, acessível pelo celular
2. **Ingestão automática** — manda um link pelo iOS, o sistema processa e indexa
3. **Coach plugável** — skills instaláveis em qualquer repo para auditar contexto e setup
4. **Gestor de setup** — templates, hooks e configurações prontas para novos projetos

---

## Status atual

### ✅ Concluído

| Item | Detalhe |
|------|---------|
| Feed mobile no ar | victorauad.github.io/co-coach — 30 cards, filtro por tema, campo de contexto |
| Indexação de 7 pastas | `07-inbox`, `06-ferramentas`, `03-metodologias`, `02-fluxos`, `04-biblioteca`, `01-setup`, `05-templates` |
| Pipeline de ingestão | `scripts/ingest.py` — fetch de URL, transcrição YT, sumarização via Claude Haiku, salva em `07-inbox/` |
| Build do site | `scripts/build-site.py` — gera `docs/index.html` a partir dos markdowns |
| GitHub Action — ingestão | `.github/workflows/ingest-link.yml` — dispara ao abrir Issue com label `add-link` |
| GitHub Action — reindex semanal | `.github/workflows/reindex-weekly.yml` — reconstrói o site toda segunda 08h UTC |
| GitHub Action — install remoto | `.github/workflows/install-skills-remote.yml` — instala skills em outro repo via API GitHub |
| Skill: coach-claude-code | Avalia CLAUDE.md com score 0–10 e sugestões concretas |
| Skill: setup-review | Audita setup completo, diferenciando CLI / VS Code / Web |
| Skill: bigquery-workflow | Guia para queries BigQuery com boas práticas de custo e validação |
| Script: install-skills.sh | Instala skills localmente em qualquer projeto |
| SessionStart hook | Cria `~/.claude/CLAUDE.md` automaticamente ao abrir sessão web neste repo |
| requirements.txt | Dependências Python documentadas |
| Guia iOS Shortcut | `docs/shortcut-ios.md` — passo a passo para configurar o Shortcut |
| 6 vídeos/webinars indexados | Lista de vídeos com `[x]` nos itens já processados |

---

### ⏳ Pendente — para atingir a Definition of Done

#### ~~P1 — Bloqueiam o fluxo automático~~ ✅ Concluído

| Tarefa | Status |
|--------|--------|
| Criar secret `ANTHROPIC_API_KEY` | ✅ Feito |
| Criar label `add-link` | ✅ Feito |
| Testar ingestão via Issue | ✅ Testado — Issue #1 processou `anthropic.com/engineering/claude-code-best-practices` em ~23s, card no feed, Issue fechada |

#### P2 — Integração com outros repos

| Tarefa | O que fazer | Onde |
|--------|-------------|------|
| Criar secret `GH_PAT` no repo | PAT com escopo `repo` em github.com → Settings → Developer Settings → PAT → Generate | GitHub |
| Instalar skills no `iracing_analysis` | Actions → "Install Skills in Remote Repo" → Run workflow → `victorauad/iracing_analysis` | GitHub Actions |
| Testar `/coach-claude-code` no iracing_analysis | Abrir sessão Claude Code no iracing_analysis e invocar a skill | Claude Code Web |

#### P3 — Ingestão pelo celular

| Tarefa | O que fazer | Onde |
|--------|-------------|------|
| Configurar Apple Shortcut no iOS | Seguir `docs/shortcut-ios.md` — 5 minutos, sem código | iPhone |
| Testar fluxo completo do celular | Abrir um vídeo no YouTube → Compartilhar → "Add to Growth Repo" → confirmar card no feed em ~2 min | iPhone + feed |

#### P4 — Qualidade e manutenção

| Tarefa | O que fazer | Onde |
|--------|-------------|------|
| Atualizar `05-templates/memory-template.md` com projetos ativos | Adicionar `iracing_analysis` e outros repos ativos na seção "Projetos ativos" | Editar arquivo |
| Marcar playlist como "não processável" na lista de vídeos | Adicionar nota explicando que playlists precisam de vídeo individual | `04-biblioteca-de-estudos/lista-de-videos.md` |

---

## Definition of Done

O projeto está completo quando:

- [x] Ingestão via GitHub Issue funciona — link processado e card no feed em ~23s (testado em 20/06/2026)
- [ ] Você manda um link pelo iPhone e em até 3 minutos aparece como card no feed mobile
- [ ] O feed mostra conteúdo relevante quando você digita o que está fazendo no campo de contexto
- [ ] Em qualquer repo novo, `/coach-claude-code` avalia o CLAUDE.md e devolve score + sugestões em menos de 1 min
- [ ] Em qualquer repo novo, `/setup-review` identifica o ambiente (CLI/VSC/web) e lista o que falta configurar
- [ ] Ao abrir uma sessão web neste repo, a memória global é carregada automaticamente (SessionStart hook)
- [ ] As skills estão instaladas no `iracing_analysis` e funcionando

---

## Arquitetura em uma linha por componente

| Componente | Como funciona |
|------------|--------------|
| Feed | Python gera HTML estático → GitHub Pages serve |
| Ingestão | GitHub Issue → Action → `ingest.py` → commit em `07-inbox/` → rebuild do site |
| Skills | Arquivos SKILL.md em `skills/` → copiados via script ou Action para `.claude/skills/` do projeto alvo |
| Memória web | SessionStart hook em `.claude/settings.json` → copia `05-templates/memory-template.md` para `~/.claude/CLAUDE.md` |
| iOS | Apple Shortcut faz POST na GitHub Issues API → dispara a ingestão |
