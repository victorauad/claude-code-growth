---
titulo: "Common Workflows — Claude Code Docs"
tema: workflow
url: https://code.claude.com/docs/en/common-workflows
data: 2026-06-23
fonte: anthropic-docs
importancia: alta
---

# Workflows Comuns do Claude Code

Receitas para tarefas cotidianas de desenvolvimento: explorar codebases, corrigir bugs, refatorar, testar, criar PRs e mais.

## Receitas de prompt

### Entender novos codebases

```text
give me an overview of this codebase
explain the main architecture patterns used here
what are the key data models?
how is authentication handled?
```

**Dicas:**
- Comece com perguntas amplas, depois aprofunde em áreas específicas
- Pergunte sobre convenções de código e padrões do projeto
- Peça um glossário de termos específicos do projeto

### Encontrar código relevante

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

**Dicas:**
- Informe o comando para reproduzir o problema e obter um stack trace
- Mencione se o erro é intermitente ou consistente

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

### Criar pull requests

```text
summarize the changes I've made to the authentication module
create a pr
enhance the PR description with more context about the security improvements
```

Ao criar um PR com `gh pr create`, a sessão é automaticamente vinculada a esse PR. Para retornar mais tarde: `claude --from-pr <number>`.

### Lidar com documentação

```text
find functions without proper JSDoc comments in the auth module
add JSDoc comments to the undocumented functions in auth.js
improve the generated documentation with more context and examples
```

### Trabalhar com imagens

Você pode arrastar e soltar imagens na janela do Claude Code, colar com Ctrl+V, ou fornecer o caminho:

```text
What does this image show?
Here's a screenshot of the error. What's causing it?
Generate CSS to match this design mockup
```

### Referenciar arquivos e diretórios

Use `@` para incluir arquivos ou diretórios rapidamente:

```text
Explain the logic in @src/utils/auth.js
What's the structure of @src/components?
Show me the data from @github:repos/owner/repo/issues
```

**Dicas:**
- Caminhos podem ser relativos ou absolutos
- Referências de diretório mostram listagem de arquivos, não conteúdos
- Você pode referenciar múltiplos arquivos em uma única mensagem

## Retomar conversas anteriores

```bash
claude --continue    # Retoma a sessão mais recente no diretório atual
claude --resume      # Escolhe de uma lista de sessões
```

Use `/resume` de dentro de uma sessão em execução.

## Sessões paralelas com worktrees

Trabalhe em uma feature em um terminal enquanto o Claude corrige um bug em outro, sem os edits colidirem:

```bash
claude --worktree feature-auth
```

Cada worktree é um checkout separado em seu próprio branch.

## Planejar antes de editar

Para mudanças que você quer revisar antes de tocarem o disco, use o modo plan:

```bash
claude --permission-mode plan
```

Ou pressione `Shift+Tab` durante uma sessão para alternar para o modo plan. O Claude lê arquivos e propõe um plano mas não faz edições até você aprovar.

## Delegar pesquisa para subagentes

Explorar uma codebase grande preenche seu contexto com leituras de arquivos. Delegue a exploração para que apenas as descobertas retornem:

```text
use a subagent to investigate how our auth system handles token refresh
```

O subagente lê arquivos em sua própria janela de contexto e relata um resumo.

## Usar Claude em scripts (modo não-interativo)

```bash
git log --oneline -20 | claude -p "summarize these recent commits"
```

Para CI, hooks de pre-commit ou processamento em lote.

## Agendar tarefas

| Opção | Onde roda | Melhor para |
|-------|-----------|-------------|
| Routines | Infraestrutura Anthropic | Tarefas que rodam mesmo com o computador desligado |
| Desktop scheduled tasks | Sua máquina via app desktop | Tarefas com acesso direto a arquivos locais |
| GitHub Actions | Pipeline CI | Tarefas vinculadas a eventos do repo |
| `/loop` | Sessão CLI atual | Polling rápido enquanto uma sessão está aberta |

## Trabalhar em notas e pastas não-código

O Claude Code funciona em qualquer diretório — cofres de notas, pastas de documentação, coleções de markdown. O diretório `.claude/` e `CLAUDE.md` ficam junto a outros diretórios de configuração sem conflito.

## Perguntar ao Claude sobre suas capacidades

```text
can Claude Code create pull requests?
how does Claude Code handle permissions?
what skills are available?
how do I use MCP with Claude Code?
what are the limitations of Claude Code?
```

O Claude tem acesso integrado à sua documentação e pode responder perguntas sobre suas próprias funcionalidades e limitações.
