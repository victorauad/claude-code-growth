---
name: setup-review
description: Audita a configuração completa do Claude Code no projeto atual e na máquina local — CLAUDE.md, settings.json, skills instaladas, extensão VS Code, memória. Use quando eu pedir "/setup-review", "revise meu setup", "o que falta configurar" ou "como está meu ambiente".
---

# Setup Review — Auditoria de Configuração do Claude Code

Você é um especialista em configuração do Claude Code. Sua função é verificar se o ambiente do projeto e da máquina estão bem configurados, comparando com as boas práticas documentadas.

## O que auditar

### Nível 1 — Projeto (pasta atual)

Verifique a existência e qualidade de cada item:

| Item | Caminho | Status esperado |
|------|---------|----------------|
| CLAUDE.md | `./CLAUDE.md` | Existe e tem os 10 campos do coach |
| Settings do projeto | `./.claude/settings.json` | Existe com permissões básicas |
| Skills do projeto | `./.claude/skills/` | Pelo menos 1 skill relevante |
| Gitignore adequado | `./.gitignore` | Ignora `.env`, credenciais, arquivos de dados sensíveis |

### Nível 2 — Máquina (configuração global)

Verifique:

| Item | Caminho | O que verificar |
|------|---------|----------------|
| Settings global | `~/.claude/settings.json` | Existe? Tem permissões globais configuradas? |
| Skills globais | `~/.claude/skills/` | Tem skills instaladas globalmente? |
| Memória | `~/.claude/CLAUDE.md` | Existe arquivo de memória global? |

### Nível 3 — VS Code

Pergunte ao usuário (não tente detectar automaticamente):
- A extensão Claude Code está instalada no VS Code?
- Está usando Claude Code na web também? Se sim, tem o SessionStart hook configurado?

### Nível 4 — Fluxo de trabalho

Avalie com base no CLAUDE.md e nas skills presentes:
- Há skills para as tarefas que se repetem no projeto?
- O CLAUDE.md está atualizado com a stack atual?
- Existe alguma automação configurada via hooks?

## Formato do relatório

```
## Auditoria de Setup — [nome do projeto ou pasta]
Data: [data de hoje]

### Nível 1 — Projeto
✅ CLAUDE.md: [resumo do que tem]
❌ Settings: [não encontrado / o que falta]
⚠️  Skills: [tem X skills, faltam Y]
✅ Gitignore: [adequado]

### Nível 2 — Máquina
[mesma estrutura]

### Nível 3 — VS Code
[baseado na resposta do usuário]

### Prioridades de melhoria
1. [ação mais urgente] — [impacto esperado]
2. [segunda ação]
3. [terceira ação]

### Templates prontos para copiar
[Se faltar settings.json ou CLAUDE.md, ofereça um template preenchido com o contexto do projeto atual]
```

## Templates de referência

### settings.json base para projetos de dados
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

### Hooks recomendados (para adicionar ao settings.json)
```json
{
  "hooks": {
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'Sessão encerrada em $(date)' >> ~/.claude/session-log.txt"
          }
        ]
      }
    ]
  }
}
```

## Regras de comportamento

- Liste o que falta com exemplos prontos para copiar, não apenas "adicione X".
- Se o projeto não tiver nenhuma configuração, comece pelo CLAUDE.md — é o de maior impacto.
- Não exija que o usuário configure tudo de uma vez. Priorize os 3 itens de maior impacto.
- Se detectar `.env` ou arquivos de credenciais sem gitignore, alerte imediatamente antes de continuar.
