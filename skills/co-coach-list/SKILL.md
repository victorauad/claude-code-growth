---
name: co-coach-list
description: Índice vivo das skills co-coach — lista todas as skills co-coach-* instaladas com descrição detalhada do que cada uma faz e como ativá-la. Use quando pedir "/co-coach-list", "quais skills eu tenho", "o que cada skill faz", "menu de skills" ou "lista as skills".
---

# Co-coach List — Índice vivo das skills

Você apresenta um menu organizado de todas as skills `co-coach-*` disponíveis, lendo a definição real de cada uma (não uma lista fixa, para nunca ficar desatualizado).

## O que fazer quando invocado

### 1. Descobrir as skills instaladas
Liste os `SKILL.md` das skills `co-coach-*` em dois lugares:

```bash
echo "=== Globais (~/.claude/skills) ==="
ls -d ~/.claude/skills/co-coach-* 2>/dev/null
echo "=== Neste projeto (.claude/skills e skills/) ==="
ls -d .claude/skills/co-coach-* skills/co-coach-* 2>/dev/null
```

### 2. Ler name + description de cada uma
Para cada pasta encontrada, leia o frontmatter do `SKILL.md` (`name` e `description`). Não duplique skills que aparecem em mais de um lugar — mostre cada `name` uma vez.

### 3. Montar o menu
Formato da resposta (escaneável):

```
## 🧰 Suas skills co-coach

| Comando | O que faz |
|---------|-----------|
| `/co-coach-review` | [resumo de 1 linha da description] |
| `/co-coach-support` | [resumo de 1 linha] |
| ... | ... |

_[N] skills instaladas. Globais valem em qualquer projeto; as locais, só aqui._
```

### 4. Fechamento
Ofereça: "Quer detalhes de alguma? Ou criar uma nova com `/co-coach-builder`?"

## Regras de comportamento
- Mostre apenas skills com prefixo `co-coach-`.
- Extraia o "o que faz" da `description` real de cada skill — não invente.
- Indique quais são globais (qualquer projeto) e quais são locais (só este).
- Respostas em português (Brasil), sem jargão.
