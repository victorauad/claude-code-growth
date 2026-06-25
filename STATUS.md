# co-coach — Visão Geral do Sistema

> Última atualização: 2026-06-24

## O que é este projeto

O co-coach é um **sistema pessoal de conhecimento e automação para Claude Code**. Funciona em três camadas simultâneas:

1. **Knowledge Base viva** — artigos, vídeos e repos indexados com sumarização por IA em `kb/`
2. **Feed mobile** — site estático (GitHub Pages) com cards da KB para consulta rápida
3. **Hub de skills** — biblioteca de 30+ skills instaláveis em qualquer projeto via GitHub Actions

---

## Features ativas

### Ingestão de conteúdo

| Feature | Trigger | O que faz |
| --- | --- | --- |
| **Ingestão por link** | Label `add-link` em uma Issue do GitHub | `ingest-link.yml` → `scripts/ingest.py` → sumariza com Claude Haiku → salva em `kb/` → fecha a Issue com confirmação |
| **Ingestão de GitHub Stars** | Toda segunda 09h UTC | `ingest-github-stars.yml` → `scripts/ingest-github-stars.py` → varre repos estrelados e indexa READMEs em `kb/` |

O script `ingest.py` gera frontmatter YAML com: `titulo`, `tema`, `bullets`, `url`, `importancia`.
Temas disponíveis: `agentes`, `ferramentas`, `mcp`, `metodologia`, `prompts`, `setup`, `workflow`.

**Fluxo de ingestão pelo celular (iOS Shortcut):**
Você copia/compartilha uma URL no iPhone → o Shortcut faz POST na GitHub Issues API criando uma Issue com label `add-link` → o workflow roda automaticamente → em ~2 minutos o card aparece no feed.

---

### Feed mobile (GitHub Pages)

- **URL pública:** `https://victorauad.github.io/co-coach`
- Gerado por `scripts/build-site.py` → produz `docs/index.html` + `docs/knowledge-base.json`
- Cards com filtro por tema e campo "o que estou fazendo agora"
- **Rebuild automático** via `reindex-weekly.yml`:
  - Toda segunda 08h UTC (agendado)
  - A cada push em `kb/**` ou `skills/**` (imediato)
  - Manualmente via GitHub Actions interface

---

### Skills disponíveis (30+)

| Skill | Função |
| --- | --- |
| `co-coach-review` | Audita CLAUDE.md e contexto do projeto (score 0–10 com exemplos concretos) |
| `co-coach-setup` | Audita configuração completa: hooks, settings, skills, memória global |
| `co-coach-bigquery` | Monta queries BigQuery Standard SQL otimizadas a partir de perguntas de negócio |
| `co-coach-handoff` | Gera resumo de sessão e salva em `memory/YYYYMMDD-projeto.md` |
| `co-coach-builder` | Cria nova skill no padrão co-coach via perguntas interativas |
| `co-coach-digest` | Briefing dos itens mais recentes da KB |
| `co-coach-quiz` | Quiz por tema com score de proficiência salvo em `docs/proficiency.json` |
| `co-coach-list` | Índice de todas as skills com descrições e como ativar |
| `co-coach-research` | Pesquisa aprofundada com síntese |
| `co-coach-content` | Apoio à criação de conteúdo |
| `co-coach-analytics` | Análise de dados e métricas |
| `co-coach-ads` | Estratégia de mídia paga |
| `co-coach-seo` | Otimização para buscadores |
| `co-coach-copy` | Criação de copy persuasivo |
| `co-coach-social` | Conteúdo para redes sociais |
| `co-coach-market` | Análise de mercado e concorrência |
| `co-coach-competitor` | Análise competitiva |
| `co-coach-marketing-plan` | Planejamento de marketing |
| `co-coach-dify` | Integração com Dify (plataforma de fluxos de IA) |
| `co-coach-flowise` | Integração com Flowise |
| `co-coach-onyx` | Integração com Onyx (busca empresarial) |
| `co-coach-obsidian` | Integração com Obsidian |
| `co-coach-notebooklm` | Integração com NotebookLM |
| `co-coach-repomix` | Usa Repomix para compactar codebase em um único arquivo |
| `co-coach-pdf` | Processamento de PDFs |
| `co-coach-docx` | Processamento de arquivos Word |
| `co-coach-pptx` | Processamento de apresentações PowerPoint |
| `co-coach-xlsx` | Processamento de planilhas Excel |
| `co-coach-wizard` | Assistente guiado por etapas |
| `co-coach-support` | Suporte e troubleshooting |

---

### Distribuição automática de skills

**Sync contínuo (`sync-skills.yml`):**

- Dispara em qualquer push em `skills/**` na branch `main`
- Lê `config/sync-targets.yml` para saber quais repos recebem as skills
- Usa GitHub API (via `GH_PAT`) para criar ou atualizar cada `SKILL.md` nos repos alvo
- Remove automaticamente skills com nomenclatura antiga (legados `coach-claude-code`, `setup-review`, `bigquery-workflow`)
- **Repos registrados:** `victorauad/iracing_analysis`, `victorauad/alamtoco`

**Setup de novo projeto (`setup-project.yml`):**

- Workflow manual via aba **Actions** no GitHub
- Instala todas as 30+ skills no repo alvo
- Cria `.claude/settings.json` base (a partir de `05-templates/project-settings.json`)
- Cria pasta `memory/` no repo alvo
- Opcionalmente adiciona o repo ao `config/sync-targets.yml` para sync futuro automático

---

### Memória de sessão

- Toda sessão Claude Code pode ser salva com `/co-coach-handoff`
- Gera `memory/YYYYMMDD-projeto.md` com: contexto, decisões tomadas e prompt de retomada
- Template base em `05-templates/memory-template.md`
- Cada projeto registrado já tem a pasta `memory/` criada pelo workflow de setup

---

## Estrutura de pastas

```text
co-coach/
├── kb/                          → 100+ artigos indexados (frontmatter YAML)
├── scripts/
│   ├── ingest.py                → fetch + sumarização via Claude Haiku
│   ├── ingest-github-stars.py   → indexa READMEs de repos estrelados
│   └── build-site.py            → gera docs/index.html + knowledge-base.json
├── skills/
│   └── co-coach-*/SKILL.md      → 30+ skills instaláveis
├── docs/                        → gerado automaticamente (GitHub Pages)
├── config/
│   └── sync-targets.yml         → repos que recebem auto-sync de skills
├── .github/workflows/
│   ├── ingest-link.yml          → ingestão por Issue
│   ├── ingest-github-stars.yml  → ingestão semanal de stars
│   ├── reindex-weekly.yml       → rebuild do site (também dispara por push em kb/ ou skills/)
│   ├── sync-skills.yml          → distribui skills para repos registrados
│   └── setup-project.yml        → onboarding de novo projeto
├── 00-comece-aqui/              → guia de início
├── 01-setup/                    → checklist e instalação
├── 02-fluxos-de-trabalho/       → BigQuery, MCP, planilhas, POCs
├── 03-metodologias/             → SWAS, prompts, agentes, skills, workflows
├── 04-biblioteca-de-estudos/    → lista de vídeos e materiais
├── 05-templates/                → CLAUDE.md.exemplo, settings.json.exemplo, skill-exemplo
├── 06-ferramentas-e-repos/      → guias de ferramentas específicas
├── 07-outros/                   → briefings e documentos avulsos
└── memory/                      → handoffs de sessão
```

---

## Como adicionar um novo projeto ao sistema

1. Crie o repo no GitHub
2. Abra a aba **Actions** do co-coach em `github.com/victorauad/co-coach`
3. Execute o workflow **"Setup Novo Projeto com co-coach"**
4. Informe o repo alvo (ex: `victorauad/novo-projeto`) e marque `add_to_sync: true`
5. Abra o novo repo no Claude Code e execute `/co-coach-setup` para configurar o `CLAUDE.md`

---

## Próximos passos sugeridos

### Prioridade alta

1. **iOS Shortcut funcionando** — o fluxo está descrito mas falta confirmar que o Shortcut está configurado no iPhone. Com ele funcionando, o ciclo "vejo → capturo → aparece no feed" fica 100% automático sem abrir o computador.

2. **`docs/proficiency.json` real** — a skill `co-coach-quiz` menciona salvar scores em `docs/proficiency.json`, mas o arquivo não existe. Criar o schema e garantir que o quiz escreve nele fecha o loop de aprendizado com tracking real de progresso por tema.

3. **Feedback visual no feed mobile** — o site não mostra quando foi o último rebuild nem total de cards por tema. Um rodapé com essas estatísticas gerado pelo `build-site.py` tornaria o feed mais confiável como ferramenta diária.

### Prioridade média

1. **Skills especializadas por contexto** — as skills atuais são genéricas. Criar uma `co-coach-mmm` (Marketing Mix Modeling) ou `co-coach-ibt` (telemetria iRacing) exploraria o potencial do hub para casos de uso específicos dos projetos ativos.

2. **Dashboard de sync** — não há visibilidade de quais repos estão em qual versão das skills. Um arquivo `config/sync-status.md` gerado pelo `sync-skills.yml` após cada run mostraria o estado atual de cada repo registrado.

3. **Ingestão de playlists do YouTube** — o fluxo atual suporta vídeos individuais mas não playlists. Adicionar suporte a playlists no `ingest.py` expandiria significativamente a capacidade de indexar cursos completos.

### Prioridade baixa

1. **Changelog automático de KB** — cada ingestão fecha uma Issue mas não gera histórico consolidado. Um `kb/CHANGELOG.md` atualizado pelo `ingest-link.yml` daria visibilidade do que foi adicionado ao longo do tempo.

2. **Documentação das skills atualizada** — `skills/README.md` pode estar desatualizado com 30+ skills. Reorganizar por categoria (produtividade, marketing, dados, ferramentas, integrações) facilitaria descoberta.

3. **Teste de integração dos workflows** — não há nenhum teste automático que valide se a ingestão produziu um arquivo válido ou se o sync de skills chegou corretamente nos repos alvo. Um step de verificação básica nos workflows reduziria falhas silenciosas.
