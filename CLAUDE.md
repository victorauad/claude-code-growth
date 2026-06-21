# Sobre este projeto e sobre mim

## Quem sou
Sou Victor, Head de Growth numa startup de Martech (MMM / media measurement). Não sou desenvolvedor — uso Claude Code como ferramenta de trabalho para dados, análises, automações e POCs. Estou aprendendo AI na prática, sem background técnico formal.

## Como prefiro que você se comunique
- Sem jargão de programação. Se precisar usar um termo técnico, explique em uma linha logo depois.
- Antes de tarefas não triviais, mostre um plano em 3 bullets e espere eu aprovar.
- Responda sempre em português (Brasil).
- Saídas que eu consiga colar direto no Notion ou Google Sheets sem reformatar.
- Se eu estiver seguindo um caminho ruim, me avise — não concorde só pra concordar.

## Stack e contexto
- Ferramentas do dia a dia: Notion, Slack, Gmail, HubSpot, Google Sheets, BigQuery.
- Dados sensíveis de cliente/CRM aparecem com frequência — nunca peça nem manuseie credenciais; eu cuido da autenticação.

## Regras de trabalho
- "Rodou" não significa "está certo": valide uma amostra dos resultados e me diga o que conferiu.
- Para queries no BigQuery, otimize para escanear o mínimo de dados.
- Para planilhas, siga o padrão: abas Resumo / Detalhe / Qualidade, datas em DD/MM/AAAA, moeda em R$.

## O que estou aprendendo
Estou aprendendo Claude Code e IA aplicada ao trabalho. Quando eu fizer algo sem entender o porquê, prefiro uma explicação rápida do conceito antes do resultado — não precisa ser longa, só o suficiente pra eu entender o que está acontecendo.

## Meta deste projeto
Usar Claude Code como ferramenta de trabalho — não virar engenheiro de software. O repositório é uma base de conhecimento viva e um sistema de skills instaláveis em outros projetos.

## Arquitetura em 3 camadas

1. **Knowledge base viva** — conteúdo indexado automaticamente em `kb/` via: (a) link enviado por GitHub Issue (iOS Shortcut), (b) repos do GitHub estrelados (workflow semanal). Cada arquivo `.md` tem frontmatter YAML com titulo, tema, bullets, url, importancia.

2. **Feed mobile** — site estático em GitHub Pages (`https://victorauad.github.io/claude-code-growth`) gerado por `scripts/build-site.py`. Cards com filtro por tema e campo de contexto "o que estou fazendo agora".

3. **Skills instaláveis** — arquivos `SKILL.md` em `skills/`, copiados para `.claude/skills/` de outros repos via GitHub Action `install-skills-remote.yml`. Skills atuais: `coach-claude-code`, `setup-review`, `bigquery-workflow`.

## Estrutura real do repositório
```
claude-code-growth/
├── kb/                          — knowledge base indexada (30+ arquivos .md com frontmatter)
├── scripts/
│   ├── build-site.py            — gera docs/index.html + knowledge-base.json
│   ├── ingest.py                — fetch + sumarização via Claude Haiku → kb/
│   └── ingest-github-stars.py  — busca repos estrelados e indexa READMEs
├── skills/
│   ├── coach-claude-code/SKILL.md
│   ├── setup-review/SKILL.md
│   └── bigquery-workflow/SKILL.md
├── docs/                        — gerado automaticamente (GitHub Pages)
├── .github/workflows/
│   ├── ingest-link.yml          — dispara ao Issue receber label "add-link"
│   ├── ingest-github-stars.yml  — toda segunda 09h UTC
│   ├── reindex-weekly.yml       — rebuild do site toda segunda 08h UTC
│   └── install-skills-remote.yml
├── 00-comece-aqui/ a 06-ferramentas-e-repos/ — documentação editorial
└── .claude/settings.json
```

## Como usar a knowledge base

Os arquivos em `kb/` são artigos, vídeos e repos indexados por tema (frontmatter `tema:`).
Quando receber uma tarefa relacionada a Claude Code, ferramentas, metodologia ou setup,
busque contexto relevante antes de responder:

```bash
grep -r "tema: <assunto>" kb/
```

Temas disponíveis: `agentes`, `ferramentas`, `mcp`, `metodologia`, `prompts`, `setup`, `workflow`.

As skills `coach-claude-code` e `setup-review` consultam `https://victorauad.github.io/claude-code-growth/knowledge-base.json` via WebFetch para trazer recomendações contextualizadas da KB ao final de cada avaliação.
