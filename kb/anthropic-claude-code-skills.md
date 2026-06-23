---
titulo: "Extend Claude with Skills — Claude Code Docs"
tema: skills
url: https://code.claude.com/docs/en/skills
data: 2026-06-23
fonte: anthropic-docs
importancia: alta
---

# Extend Claude with Skills (Claude Code)

> Crie, gerencie e compartilhe skills para estender as capacidades do Claude no Claude Code. Inclui comandos personalizados e skills agrupadas.

Skills estendem o que Claude pode fazer. Crie um arquivo `SKILL.md` com instruções, e Claude adiciona-o ao seu toolkit. Claude usa skills quando relevante, ou você pode invocar uma diretamente com `/nome-da-skill`.

Crie uma skill quando você fica colando as mesmas instruções, checklist ou procedimento multi-etapas no chat, ou quando uma seção do CLAUDE.md cresceu para se tornar um procedimento em vez de um fato. Ao contrário do conteúdo do CLAUDE.md, o corpo de uma skill carrega apenas quando é usada, então materiais de referência longos custam quase nada até você precisar deles.

**Nota:** Comandos personalizados foram integrados às skills. Um arquivo em `.claude/commands/deploy.md` e uma skill em `.claude/skills/deploy/SKILL.md` ambos criam `/deploy` e funcionam da mesma forma.

Claude Code skills seguem o padrão aberto [Agent Skills](https://agentskills.io), que funciona em múltiplas ferramentas de IA.

## Skills Agrupadas

Claude Code inclui um conjunto de skills agrupadas disponíveis em toda sessão, incluindo `/code-review`, `/batch`, `/debug`, `/loop` e `/claude-api`.

### Skills de executar e verificar

| Skill | Propósito |
|-------|-----------|
| `/run` | Inicia e dirige seu app para ver uma mudança funcionando |
| `/verify` | Constrói e roda seu app para confirmar que uma mudança de código faz o que deveria |
| `/run-skill-generator` | Ensina `/run` e `/verify` como construir e iniciar seu projeto |

## Criar sua primeira skill

Exemplo — skill que resume mudanças não commitadas e sinaliza riscos:

```bash
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

Summarize the changes above in two or three bullet points, then list any risks you notice such as missing error handling, hardcoded values, or tests that need updating. If the diff is empty, say there are no uncommitted changes.
```

A linha `` !`git diff HEAD` `` usa injeção dinâmica de contexto: Claude Code roda o comando e substitui a linha com sua saída antes do Claude ver o conteúdo da skill.

## Onde skills ficam

| Localização | Caminho | Aplica a |
|-------------|---------|----------|
| Enterprise | Ver managed settings | Todos os usuários da organização |
| Pessoal | `~/.claude/skills/<nome>/SKILL.md` | Todos os seus projetos |
| Projeto | `.claude/skills/<nome>/SKILL.md` | Este projeto apenas |
| Plugin | `<plugin>/skills/<nome>/SKILL.md` | Onde plugin está habilitado |

Quando skills compartilham o mesmo nome em diferentes níveis: enterprise > pessoal > projeto.

## Frontmatter de referência

| Campo | Obrigatório | Descrição |
|-------|-------------|-----------|
| `name` | Não | Nome de exibição. Padrão: nome do diretório |
| `description` | Recomendado | O que a skill faz e quando usá-la |
| `when_to_use` | Não | Contexto adicional sobre quando Claude deve invocar a skill |
| `disable-model-invocation` | Não | `true` para impedir Claude de carregar automaticamente. Use para workflows com efeitos colaterais |
| `user-invocable` | Não | `false` para ocultar do menu `/`. Use para conhecimento de fundo |
| `allowed-tools` | Não | Ferramentas que Claude pode usar sem pedir permissão quando esta skill está ativa |
| `context` | Não | `fork` para rodar em um subagente isolado |
| `agent` | Não | Qual tipo de subagente usar quando `context: fork` está definido |
| `paths` | Não | Padrões glob que limitam quando esta skill é ativada |

## Injeção de contexto dinâmico

O `` !`<comando>` `` roda comandos shell antes do conteúdo da skill ser enviado ao Claude:

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

## Your task
Summarize this pull request...
```

## Rodar skills em subagente

Adicione `context: fork` ao frontmatter quando quiser que uma skill rode em isolamento:

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

## Passagem de argumentos

```yaml
---
name: fix-issue
description: Fix a GitHub issue
disable-model-invocation: true
---

Fix GitHub issue $ARGUMENTS following our coding standards.
```

Rodar `/fix-issue 123` substitui `$ARGUMENTS` por "123".

## Detectar mudanças em tempo real

Claude Code monitora diretórios de skills para mudanças de arquivo. Adicionar, editar ou remover uma skill entra em vigor na sessão atual sem reiniciar.

## Ciclo de vida do conteúdo da skill

Quando você ou Claude invocam uma skill, o conteúdo renderizado do `SKILL.md` entra na conversa como uma única mensagem e fica lá pelo resto da sessão.

## Avaliar e iterar em uma skill

O plugin [`skill-creator`](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/skill-creator) automatiza o loop de comparação dentro do Claude Code:

```
/plugin install skill-creator@claude-plugins-official
```

Funcionalidades:
- **Casos de teste**: armazena prompts, arquivos de entrada e comportamento esperado
- **Execuções isoladas**: gera um subagente por caso de teste
- **Avaliação**: verifica cada asserção contra o output
- **Benchmark**: agrega taxa de aprovação, tempo e tokens com vs. sem skill

## Compartilhar skills

- **Project skills**: Commit `.claude/skills/` para controle de versão
- **Plugins**: Crie um diretório `skills/` no seu plugin
- **Managed**: Deploy em toda organização via managed settings
