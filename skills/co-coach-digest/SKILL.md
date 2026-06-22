---
name: co-coach-digest
description: Gera um briefing curto dos itens mais recentes e importantes da knowledge base do co-coach — "o que há de novo". Use quando pedir "/co-coach-digest", "o que tem de novo na KB", "me atualiza", "resumo da semana" ou "novidades".
---

# Co-coach Digest — O que há de novo na KB

Você gera um resumo curto e escaneável dos conteúdos mais recentes/relevantes da knowledge base, para o Victor se manter atualizado sem abrir o feed.

## O que fazer quando invocado

### 1. Buscar a Knowledge Base
1. Use `WebFetch` para buscar `https://victorauad.github.io/co-coach/knowledge-base.json`.
   - Se não tiver acesso a WebFetch, use `Bash(curl -s https://victorauad.github.io/co-coach/knowledge-base.json)`.
2. Cada item tem `titulo`, `tema`, `url`, `data`, `bullets`, `importancia` e (para repos) `github_stars`.

### 2. Selecionar os itens
- Ordene por `data` (mais recente primeiro).
- Se o usuário pedir um período ("essa semana", "últimos 7 dias"), filtre por `data`.
- Por padrão, traga os **8 itens mais recentes**.
- Agrupe por `tema`.

### 3. Montar o briefing
Formato da resposta (pronto para colar no Notion):

```
## 📰 Novidades da sua Knowledge Base
_Atualizado em [data de hoje] — [N] itens recentes_

### [tema]
- **[titulo]** — [1 frase do que é / por que importa] → [url]

### [outro tema]
- **[titulo]** — [1 frase] → [url]

---
**Destaque:** [o item mais relevante e por quê, em 1 frase]
```

### 4. Fechamento
Ao final, ofereça um próximo passo:
- "Quer que eu detalhe algum desses?" ou
- "Quer testar seu conhecimento sobre algum tema? (use `/co-coach-quiz`)"

## Regras de comportamento
- Respostas em português (Brasil), sem jargão.
- Seja conciso: 1 frase por item. O objetivo é escanear rápido.
- Se a KB estiver vazia ou inacessível, avise de forma simples e não invente itens.
