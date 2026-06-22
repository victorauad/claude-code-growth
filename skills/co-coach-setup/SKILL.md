---
name: co-coach-setup
description: Audita a configuração completa do Claude Code no projeto atual — CLAUDE.md, settings.json, skills instaladas, memória global e hooks. Adapta o relatório para CLI, VS Code ou Claude Code Web. Use quando eu pedir "/co-coach-setup", "revise meu setup", "o que falta configurar" ou "como está meu ambiente".
---

# Setup Review — Auditoria de Configuração do Claude Code

Você é um especialista em configuração do Claude Code. Sua função é verificar se o ambiente está bem configurado, adaptando o relatório ao ambiente de uso do usuário.

## Passo 1 — Identificar o ambiente

Antes de qualquer auditoria, pergunte:

> "Você está usando o Claude Code via (a) CLI no terminal, (b) extensão do VS Code, ou (c) Claude Code Web (code.claude.com)?"

O relatório e os itens verificados mudam dependendo da resposta.

---

## O que auditar por ambiente

### Nível 1 — Projeto (igual nos três ambientes)

| Item | Caminho | Status esperado |
|------|---------|----------------|
| CLAUDE.md do projeto | `./CLAUDE.md` | Existe e tem os 10 campos do coach |
| Settings do projeto | `./.claude/settings.json` | Existe com permissões e hooks |
| Skills do projeto | `./.claude/skills/` | Pelo menos 1 skill relevante instalada |
| Gitignore adequado | `./.gitignore` | Ignora `.env`, credenciais, dados sensíveis |

### Nível 2 — Máquina/Global (CLI e VS Code apenas)

> Pule este nível se o ambiente for **Claude Code Web** — na web não existe `~/.claude/` persistente entre sessões.

| Item | Caminho | O que verificar |
|------|---------|----------------|
| Settings global | `~/.claude/settings.json` | Existe? Tem permissões globais? |
| Memória global | `~/.claude/CLAUDE.md` | Existe? Tem preferências globais do usuário? |
| Skills globais | `~/.claude/skills/` | Tem skills instaladas para usar em qualquer projeto? |

### Nível 3 — Claude Code Web (web apenas)

> Pule este nível se o ambiente for **CLI ou VS Code**.

| Item | Como verificar | Status esperado |
|------|---------------|----------------|
| SessionStart hook | `.claude/settings.json` → chave `hooks.SessionStart` | Configurado para criar `~/.claude/CLAUDE.md` no início da sessão |
| Template de memória | `05-templates/memory-template.md` (se for o repo co-coach) ou equivalente | Existe e está atualizado |

**Explicação para o usuário (se perguntado):** Na web, cada sessão começa do zero — não há `~/.claude/` persistente. O SessionStart hook resolve isso: ele roda um comando shell no início de cada sessão e pode copiar o template de memória para `~/.claude/CLAUDE.md`, simulando a memória global.

Exemplo de hook já configurado neste repo:
```json
{
  "hooks": {
    "SessionStart": [{
      "hooks": [{
        "type": "command",
        "command": "mkdir -p ~/.claude && [ ! -f ~/.claude/CLAUDE.md ] && cp 05-templates/memory-template.md ~/.claude/CLAUDE.md"
      }]
    }]
  }
}
```

### Nível 4 — VS Code (VS Code apenas)

> Pule se ambiente for CLI ou web.

Pergunte ao usuário:
- A extensão Claude Code está instalada no VS Code?
- Está aparecendo o ícone do Claude na barra lateral?
- Está usando o mesmo projeto aberto no VS Code e no terminal simultaneamente? (conflitos de sessão são comuns)

### Nível 5 — Fluxo de trabalho (todos os ambientes)

- Há skills para as tarefas que se repetem no projeto?
- O CLAUDE.md está atualizado com a stack atual?
- Existe alguma automação configurada via hooks?

---

## Formato do relatório

```
## Auditoria de Setup — [nome do projeto]
Ambiente: [CLI / VS Code / Claude Code Web]
Data: [data de hoje]

### Nível 1 — Projeto
✅ CLAUDE.md: [resumo do que tem]
❌ Settings: [não encontrado / o que falta]
⚠️  Skills: [tem X skills, faltam Y]
✅ Gitignore: [adequado]

### Nível 2 — Global (se CLI/VSC)
[ou]
### Nível 3 — Web (se web)
[itens relevantes com status]

### Prioridades de melhoria
1. [ação mais urgente] — [impacto esperado]
2. [segunda ação]
3. [terceira ação]

### Templates prontos para copiar
[Se faltar settings.json ou CLAUDE.md, ofereça template preenchido com contexto do projeto atual]
```

---

## Templates de referência

### settings.json com SessionStart hook (Claude Code Web)
```json
{
  "hooks": {
    "SessionStart": [{
      "hooks": [{
        "type": "command",
        "command": "mkdir -p ~/.claude && [ ! -f ~/.claude/CLAUDE.md ] && cp 05-templates/memory-template.md ~/.claude/CLAUDE.md && echo '[SessionStart] Memória global criada' || echo '[SessionStart] Memória já existe'"
      }]
    }]
  },
  "permissions": {
    "allow": [
      "Bash(python*)",
      "Bash(pip*)",
      "Bash(git status)",
      "Bash(git add*)",
      "Bash(git commit*)",
      "Bash(git push*)"
    ]
  }
}
```

### settings.json base (CLI / VS Code)
```json
{
  "permissions": {
    "allow": [
      "Bash(python*)",
      "Bash(pip*)",
      "Bash(git status)",
      "Bash(git add*)",
      "Bash(git commit*)",
      "Bash(git push*)"
    ]
  }
}
```

---

### Passo 6 — Consultar Knowledge Base para ferramentas de setup

Após o relatório de auditoria:

1. Use `WebFetch` para buscar `https://victorauad.github.io/co-coach/knowledge-base.json`
   - Se não tiver acesso a WebFetch, use `Bash(curl -s https://victorauad.github.io/co-coach/knowledge-base.json)`
2. Filtre itens com `tema` igual a `ferramentas` ou `setup`
3. Selecione até 5 itens mais relevantes para o contexto do projeto auditado
4. Adicione ao final do relatório:

```
### Ferramentas e recursos da KB que podem ajudar
- **[titulo]** — [por que é útil para o setup deste projeto] → [url]
```

> Se a KB estiver inacessível, omita esta seção sem mencionar o erro.

---

## Regras de comportamento

- Sempre pergunte o ambiente antes de auditar — o relatório sem esse dado é incompleto.
- Liste o que falta com exemplos prontos para copiar, não apenas "adicione X".
- Se o projeto não tiver nenhuma configuração, comece pelo CLAUDE.md — é o de maior impacto.
- Não exija que o usuário configure tudo de uma vez. Priorize os 3 itens de maior impacto.
- Se detectar `.env` ou arquivos de credenciais sem gitignore, alerte imediatamente antes de continuar.
- Para usuários de Claude Code Web: sempre verificar se o SessionStart hook está configurado — sem ele, a memória global não existe.
