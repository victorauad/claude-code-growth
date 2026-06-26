# co-coach

Base de conhecimento viva e sistema de skills instaláveis em outros projetos. Não é um produto de software — é uma ferramenta de trabalho pessoal.

## Como trabalhar neste projeto (Spec-Driven Development)

Antes de qualquer tarefa não trivial, siga este ciclo de 4 fases:

1. **Specify** — escreva o que precisa ser feito em linguagem clara (o "o quê" e o "por quê"). Consulte `requirements.md` para contexto e `design.md` para restrições técnicas.
2. **Plan** — proponha um plano em bullets e aguarde aprovação antes de executar.
3. **Implement** — execute os passos do plano, um de cada vez.
4. **Validate** — confira se o resultado bate com o que foi especificado. "Rodou" não é suficiente.

Os 3 documentos de spec deste projeto:
- `requirements.md` — o que o sistema precisa fazer (histórias de usuário e objetivos)
- `design.md` — como está construído (arquitetura, decisões técnicas, restrições)
- `TASKS.md` — passos atômicos de implementação e backlog priorizado

Quando receber uma tarefa, consulte esses três arquivos antes de propor qualquer plano.

## Arquitetura em 3 camadas

1. **Knowledge base viva** — conteúdo indexado automaticamente em `kb/` via: (a) link enviado por GitHub Issue (iOS Shortcut), (b) repos do GitHub estrelados (workflow semanal). Cada arquivo `.md` tem frontmatter YAML com titulo, tema, bullets, url, importancia.

2. **Feed mobile** — site estático em GitHub Pages (`https://victorauad.github.io/co-coach`) gerado por `scripts/build-site.py`. Cards com filtro por tema e campo de contexto "o que estou fazendo agora".

3. **Skills instaláveis** — arquivos `SKILL.md` em `skills/*/`, copiados para `.claude/skills/` de outros repos via GitHub Action `sync-skills.yml`. Para ver skills disponíveis: `ls skills/`.

## Como usar a knowledge base

Arquivos em `kb/` têm frontmatter `tema:`. Busque contexto antes de responder tarefas de Claude Code, ferramentas ou setup:

```bash
grep -r "tema: <assunto>" kb/
```

Temas: `agentes`, `ferramentas`, `mcp`, `metodologia`, `prompts`, `setup`, `workflow`.
Skills `co-coach-review` e `co-coach-setup` consultam `https://victorauad.github.io/co-coach/knowledge-base.json` via WebFetch.
