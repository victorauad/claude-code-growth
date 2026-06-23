---
titulo: "Common Workflows — Claude Code Docs"
tema: workflow
url: https://code.claude.com/docs/en/common-workflows
data: 2026-06-23
fonte: anthropic-docs
importancia: alta
---

# Common Workflows (Claude Code)

> Guias passo a passo para explorar codebases, corrigir bugs, refatorar, testar e outras tarefas cotidianas com Claude Code.

## Receitas de prompts

### Entender novos codebases

**Visão geral rápida:**
```text
give me an overview of this codebase
explain the main architecture patterns used here
what are the key data models?
how is authentication handled?
```

**Encontrar código relevante:**
```text
find the files that handle user authentication
how do these authentication files work together?
trace the login process from front-end to database
```

### Corrigir bugs eficientemente

```text
I'm seeing an error when I run npm test
suggest a few ways to fix the @ts-ignore in user.ts
update user.ts to add the null check you suggested
```
Dicas: Diga o comando para reproduzir o problema e obtenha um stack trace. Mencione se o erro é intermitente ou consistente.

### Refatorar código

```text
find deprecated API usage in our codebase
suggest how to refactor utils.js to use modern JavaScript features
refactor utils.js to use ES2024 features while maintaining the same behavior
run tests for the refactored code
```

### Trabalhar com testes

```text
find functions in NotificationsService.swift that are not covered by tests
add tests for the notification service
add test cases for edge conditions in the notification service
run the new tests and fix any failures
```

Claude examina arquivos de teste existentes para corresponder ao estilo, frameworks e padrões de asserção já em uso.

### Criar pull requests

```text
summarize the changes I've made to the authentication module
create a pr
enhance the PR description with more context about the security improvements
```

### Referências de arquivos e diretórios

Use `@` para incluir rapidamente arquivos ou diretórios:

```text
Explain the logic in @src/utils/auth.js
What's the structure of @src/components?
Show me the data from @github:repos/owner/repo/issues
```

## Retomar conversas anteriores

```bash
claude --continue    # retoma sessão mais recente no diretório atual
claude --resume      # escolha de uma lista
```

## Sessões paralelas com worktrees

Trabalhe em uma feature em um terminal enquanto Claude corrige um bug em outro, sem colisões:

```bash
claude --worktree feature-auth
```

Cada worktree é um checkout separado em seu próprio branch.

## Planejar antes de editar

Para mudanças que você quer revisar antes de tocar no disco, use o modo de planejamento:

```bash
claude --permission-mode plan
```

Também pode pressionar `Shift+Tab` no meio da sessão para alternar para o modo de planejamento. Claude lê arquivos e propõe um plano, mas não faz edições até você aprovar.

## Delegar pesquisa a subagentes

Explorar um codebase grande preenche seu contexto com leituras de arquivos. Delegue a exploração para que apenas os resultados voltem:

```text
use a subagent to investigate how our auth system handles token refresh
```

O subagente lê arquivos em sua própria janela de contexto e reporta um resumo.

## Executar Claude via scripts (modo não-interativo)

```bash
git log --oneline -20 | claude -p "summarize these recent commits"
```

Útil para CI, hooks de pré-commit ou processamento em lote. Stdin e stdout funcionam como qualquer ferramenta Unix.

## Rodar Claude em um agendamento

| Opção | Onde roda | Melhor para |
|-------|-----------|-------------|
| Routines | Infraestrutura Anthropic | Tarefas que devem rodar mesmo com o computador desligado |
| Desktop scheduled tasks | Sua máquina, via app desktop | Tarefas que precisam de acesso a arquivos locais |
| GitHub Actions | Pipeline de CI | Tarefas vinculadas a eventos do repo |
| `/loop` | Sessão CLI atual | Polling rápido enquanto a sessão está aberta |

## Trabalhar com imagens

Para analisar imagens no Claude Code:
1. Arraste e solte uma imagem na janela do Claude Code
2. Copie uma imagem e cole com `ctrl+v`
3. Forneça um caminho: "Analyze this image: /path/to/your/image.png"

```text
What does this image show?
Generate CSS to match this design mockup
Here's a screenshot of the error. What's causing it?
```

## Trabalhar em notas e pastas sem código

Claude Code funciona em qualquer diretório. Execute dentro de um vault de notas, pasta de documentação ou qualquer coleção de arquivos markdown para pesquisar, editar e reorganizar conteúdo da mesma forma que código.

## Perguntar ao Claude sobre suas capacidades

```text
can Claude Code create pull requests?
how does Claude Code handle permissions?
what skills are available?
how do I use MCP with Claude Code?
```

Claude sempre tem acesso à documentação mais recente do Claude Code, independentemente da versão que você está usando.
