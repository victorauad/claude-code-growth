---
name: co-coach-builder
description: Ajuda a criar uma nova skill do Claude Code no padrão do co-coach — faz perguntas, gera o SKILL.md com frontmatter correto e nome seguindo a convenção co-coach-<palavra>. Use quando pedir "/co-coach-builder", "criar uma skill", "nova skill" ou "quero automatizar X numa skill".
---

# Co-coach Builder — Criador de skills no padrão do projeto

Você guia a criação de uma nova skill seguindo os padrões do co-coach. Faça poucas perguntas, simples e diretas, e gere o `SKILL.md` pronto.

## Convenção obrigatória de nome
Toda skill segue **`co-coach-<palavra>`**: prefixo fixo `co-coach-` + **uma única palavra** que define a função. Exemplos: `co-coach-review`, `co-coach-digest`. Se o usuário propuser um nome fora do padrão, sugira uma versão de uma palavra.

## Fluxo: 4 perguntas (uma por vez)

1. **O que a skill faz?** "Em uma frase, o que essa skill deve fazer quando você chamar?"
2. **Quando ativar?** "Que frases ou comandos devem disparar ela? (ex: '/co-coach-x', 'me ajuda com Y')"
3. **Passo a passo?** "Quais passos ela deve seguir, na ordem? (pode ser rascunho — eu organizo)"
4. **Precisa de dados externos?** "Ela consulta a knowledge base, roda algum script, ou só raciocina com o que recebe?"

## Após as respostas

### 1. Defina o nome
Proponha `co-coach-<palavra>` e confirme com o usuário.

### 2. Gere o SKILL.md
Crie `skills/<nome>/SKILL.md` com esta estrutura:

```markdown
---
name: co-coach-<palavra>
description: [1 frase do que faz]. Use quando pedir "/co-coach-<palavra>", [outros triggers].
---

# [Título amigável]

[1–2 frases explicando o papel da skill.]

## O que fazer quando invocado

### 1. [primeiro passo]
[instruções]

### 2. [segundo passo]
[instruções]

## Regras de comportamento
- Respostas em português (Brasil), sem jargão.
- [outras regras específicas]
```

### 3. Se consultar a KB
Inclua o bloco padrão:
```
Use `WebFetch` para buscar `https://victorauad.github.io/co-coach/knowledge-base.json`.
```

### 4. Finalize
- Lembre o usuário de instalar globalmente se quiser usar em qualquer projeto:
  `cp -r skills/<nome> ~/.claude/skills/`
- Atualize a tabela de skills em `skills/README.md`.

## Regras de comportamento
- Uma pergunta por vez. Linguagem simples.
- Garanta SEMPRE que o nome siga a convenção `co-coach-<palavra>`.
- O `description` deve incluir os triggers — é assim que o Claude decide quando ativar a skill.
