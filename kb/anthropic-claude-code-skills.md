---
titulo: "Extend Claude with Skills — Claude Code Docs"
tema: skills
url: https://code.claude.com/docs/en/skills
data: 2026-06-23
fonte: anthropic-docs
importancia: alta
---

# Extender o Claude com Skills (Claude Code)

Skills estendem o que o Claude consegue fazer. Crie um arquivo `SKILL.md` com instruções, e o Claude adiciona ao seu toolkit. O Claude usa skills quando relevante, ou você pode invocar diretamente com `/skill-name`.

**Claude Code skills seguem o padrão aberto [Agent Skills](https://agentskills.io)**, que funciona em múltiplas ferramentas de IA. Claude Code estende o padrão com controle de invocação, execução em subagente e injeção de contexto dinâmico.

> **Nota**: Comandos customizados foram fundidos em skills. Um arquivo em `.claude/commands/deploy.md` e uma skill em `.claude/skills/deploy/SKILL.md` ambos criam `/deploy` e funcionam da mesma forma.

## Bundled skills incluídas

Claude Code inclui skills pré-instaladas:
- `/code-review` — revisão de código
- `/batch` — operações em lote
- `/debug` — depuração
- `/loop` — loops recorrentes
- `/claude-api` — referência da API Anthropic

Três skills para rodar e verificar o app:
| Skill | Propósito |
|-------|-----------|
| `/run` | Lança e dirige o app para ver mudanças funcionando |
| `/verify` | Constrói e roda o app para confirmar que uma mudança funciona |
| `/run-skill-generator` | Ensina `/run` e `/verify` como construir e lançar seu projeto |

## Criando sua primeira skill

```bash
# Crie o diretório da skill (skills pessoais disponíveis em todos os projetos)
mkdir -p ~/.claude/skills/summarize-changes
```

Salve em `~/.claude/skills/summarize-changes/SKILL.md`:

```yaml
---
description: Summarizes uncommitted changes and flags anything risky. Use when the user asks what changed, wants a commit message, or asks to review their diff.
---

## Current changes

!`git diff HEAD`

## Instructions

Summarize the changes above in two or three bullet points, then list any risks you notice such as missing error handling, hardcoded values, or tests that need updating.
```

A sintaxe `` !`git diff HEAD` `` usa **injeção de contexto dinâmico**: o Claude Code roda o comando e substitui a linha pelo output antes que o Claude veja o conteúdo da skill.

## Onde skills ficam armazenadas

| Localização | Caminho | Aplica-se a |
|-------------|---------|-------------|
| Enterprise | Veja managed settings | Todos os usuários da organização |
| Personal | `~/.claude/skills/<skill-name>/SKILL.md` | Todos os seus projetos |
| Project | `.claude/skills/<skill-name>/SKILL.md` | Este projeto apenas |
| Plugin | `<plugin>/skills/<skill-name>/SKILL.md` | Onde o plugin está habilitado |

**Precedência**: enterprise > personal > project. Skills com o mesmo nome em níveis diferentes fazem override — um `code-review` no `.claude/skills/` do projeto substitui o bundled `/code-review`.

## Estrutura de uma skill

```text
my-skill/
├── SKILL.md           # Instruções principais (obrigatório)
├── template.md        # Template para o Claude preencher
├── examples/
│   └── sample.md      # Exemplo de output
└── scripts/
    └── validate.sh    # Script que o Claude pode executar
```

## Frontmatter reference

```yaml
---
name: my-skill                    # Nome de exibição (opcional)
description: What this skill does # RECOMENDADO — Claude usa para decidir quando aplicar
disable-model-invocation: true    # Apenas você pode invocar (não o Claude automaticamente)
user-invocable: false             # Apenas o Claude pode invocar (não aparece no menu /)
allowed-tools: Read Grep          # Ferramentas pré-aprovadas enquanto a skill está ativa
disallowed-tools: AskUserQuestion # Ferramentas removidas do pool durante a skill
context: fork                     # Roda em subagente isolado
agent: Explore                    # Qual tipo de subagente usar com context: fork
model: claude-opus-4-8            # Modelo a usar quando a skill está ativa
effort: high                      # Nível de esforço (low/medium/high/xhigh/max)
paths: "src/**/*.ts"             # Glob — skill ativada apenas com arquivos matching
---
```

## Controle de invocação

| Frontmatter | Você pode invocar | Claude pode invocar |
|-------------|------------------|---------------------|
| (padrão) | Sim | Sim |
| `disable-model-invocation: true` | Sim | Não |
| `user-invocable: false` | Não | Sim |

Use `disable-model-invocation: true` para workflows com efeitos colaterais como `/commit`, `/deploy`, `/send-slack-message`.

## Injeção de contexto dinâmico

A sintaxe `` !`<command>` `` roda comandos shell antes que o conteúdo da skill seja enviado ao Claude:

```yaml
---
name: pr-summary
description: Summarize changes in a pull request
context: fork
agent: Explore
allowed-tools: Bash(gh *)
---

## Pull request context
- PR diff: !`gh pr diff`
- PR comments: !`gh pr view --comments`
- Changed files: !`gh pr diff --name-only`
```

Para múltiplas linhas, use bloco de código com ` ```! `:
```
## Environment
```!
node --version
npm --version
git status --short
```
```

## Substituições disponíveis

| Variável | Descrição |
|----------|-----------|
| `$ARGUMENTS` | Todos os argumentos passados ao invocar |
| `$ARGUMENTS[N]` | Argumento específico por índice (base 0) |
| `$0`, `$1`, etc. | Atalho para `$ARGUMENTS[N]` |
| `$name` | Argumento nomeado declarado em `arguments:` |
| `${CLAUDE_SESSION_ID}` | ID da sessão atual |
| `${CLAUDE_EFFORT}` | Nível de esforço atual |
| `${CLAUDE_SKILL_DIR}` | Diretório contendo o SKILL.md da skill |

## Executar skills em subagente

```yaml
---
name: deep-research
description: Research a topic thoroughly
context: fork
agent: Explore
---

Research $ARGUMENTS thoroughly:
1. Find relevant files using Glob and Grep
2. Read and analyze the code
3. Summarize findings with specific file references
```

## Detecção de mudanças em tempo real

Claude Code monitora diretórios de skills. Adicionar, editar ou remover uma skill toma efeito na sessão atual sem reiniciar.

## Compartilhar skills

- **Skills de projeto**: commitar `.claude/skills/` no controle de versão
- **Plugins**: criar diretório `skills/` no plugin
- **Managed**: distribuir via managed settings da organização

## Avaliação de skills

Use o plugin `skill-creator` para automatizar o loop de comparação:

```text
/plugin install skill-creator@claude-plugins-official
```

O plugin gera casos de teste, roda comparações com/sem a skill, faz grading e produz relatório HTML com métricas de pass rate, tempo e tokens.
