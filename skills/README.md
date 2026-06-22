# Skills do co-coach

Skills instaláveis do Claude Code. Cada pasta tem um `SKILL.md` com frontmatter (`name`, `description`) e instruções.

## Convenção de nomenclatura

Toda skill segue o padrão **`co-coach-<palavra>`**:

- **Prefixo fixo `co-coach-`** — facilita a busca e o reconhecimento, já que as skills são instaladas globalmente (`~/.claude/skills`) e aparecem misturadas a skills de outros projetos.
- **Uma única palavra ao final** — define a função da skill de forma direta.

Exemplos: `co-coach-review`, `co-coach-setup`, `co-coach-support`.

> Ao criar uma skill nova, use a `co-coach-builder`, que já aplica essa convenção automaticamente.

## Skills disponíveis

| Skill | Função |
|-------|--------|
| `co-coach-review` | Audita o contexto do projeto atual (CLAUDE.md, skills, settings) com score 0–10 e sugestões. |
| `co-coach-setup` | Audita a configuração completa do Claude Code (settings, hooks, memória global). |
| `co-coach-wizard` | Criador conversacional de projetos novos (gera CLAUDE.md, pastas, skills, settings). |
| `co-coach-support` | Tira-dúvidas que responde **somente com base na knowledge base**, sem revisar o projeto. |
| `co-coach-digest` | Briefing curto dos itens mais recentes/importantes da knowledge base. |
| `co-coach-builder` | Ajuda a criar novas skills no padrão do projeto (gera o SKILL.md). |
| `co-coach-list` | Índice vivo: lista todas as skills `co-coach-*` instaladas e o que cada uma faz. |
| `co-coach-bigquery` | Monta queries BigQuery Standard SQL a partir de perguntas de negócio. |
| `co-coach-quiz` | Quiz por tema baseado na KB, mede progresso e atualiza o painel de proficiência. |
| `co-coach-handoff` | Gera arquivo de memória da sessão e bloco de retomada (handoff). |

## Como as skills são distribuídas

O workflow `.github/workflows/install-skills-remote.yml` copia cada pasta de `skills/` para o `.claude/skills/` de outro repositório. As cópias globais ficam em `~/.claude/skills/`.
