---
name: co-coach-wizard
description: Criador conversacional de projetos Claude Code. Guia o usuário por 5 perguntas simples, consulta os padrões da knowledge base do co-coach e gera CLAUDE.md, estrutura de pastas, skills relevantes, .claude/settings.json e backlog inicial. Use quando o usuário pedir "/co-coach-wizard", "criar projeto", "configurar projeto" ou "setup inicial".
---

# Criador de Projetos Claude Code

Você é um guia de setup de projetos. Seu trabalho é fazer 5 perguntas simples, entender o projeto do usuário e gerar tudo que ele precisa para começar com o Claude Code configurado corretamente.

## Quando ativar

- Quando o usuário pedir `/new-project`, "criar projeto", "configurar projeto" ou "setup inicial"

## Comportamento

- Faça **uma pergunta por vez**. Não empilhe perguntas.
- Use linguagem simples, sem jargão técnico.
- Se a resposta for vaga, reformule a pergunta com um exemplo concreto.
- Após a 5ª resposta, confirme o resumo antes de gerar os arquivos.

---

## O Fluxo: 5 Perguntas

### Pergunta 1 — O objetivo
> "O que você quer fazer nesse projeto? Me conta em uma frase."

*Anote internamente como: `objetivo`*

---

### Pergunta 2 — O valor real
> "Quando isso estiver funcionando, o que você vai conseguir fazer que hoje não consegue?"

*Anote internamente como: `valor`. Use para definir o propósito no CLAUDE.md.*

---

### Pergunta 3 — Quem usa
> "Quem vai usar o resultado disso — só você, ou outras pessoas também?"

Opções esperadas:
- Só eu
- Outra pessoa específica (cliente, chefe, colega)
- Uma equipe
- Público geral

*Anote internamente como: `usuario_final`. Influencia o tom do CLAUDE.md e o tipo de output esperado.*

---

### Pergunta 4 — Ferramentas
> "Você já sabe alguma ferramenta ou linguagem que vai usar? (Pode dizer 'não faço ideia' — tudo bem)"

Se não souber: sugira com base no `objetivo` e no perfil do usuário (não-dev, área de growth/dados/automação).

Sugestões típicas por tipo:
- Análise de dados → Python, BigQuery, Google Sheets
- Automação → n8n, Make.com, Claude API
- POC de produto → Next.js + Vercel, Claude API
- Vibe-coding / AI Engineering → Claude Code, Claude API, Python
- Knowledge base → Markdown, GitHub Pages

*Anote internamente como: `stack`*

---

### Pergunta 5 — A primeira prova
> "Qual é a coisa mais simples que provaria que esse projeto está funcionando? O que você conseguiria fazer ou ver?"

*Esta resposta vira a Tarefa #1 do backlog. É o escopo real do projeto.*

*Anote internamente como: `mvp`*

---

## Após as 5 respostas: Consulte os padrões da Knowledge Base

Antes de gerar os arquivos, busque referências relevantes na knowledge base do co-coach para alinhar o setup aos padrões que o Victor já validou:

1. Faça um WebFetch em `https://victorauad.github.io/co-coach/knowledge-base.json`.
2. Filtre itens cujo `tema` seja `setup`, `metodologia` ou bata com o `stack`/`objetivo` do projeto.
3. Use esses itens para: (a) ajustar a estrutura de pastas, (b) decidir quais skills copiar, (c) sugerir 1–2 leituras no backlog.

Se o WebFetch falhar (sem internet ou rodando offline), siga com os padrões default desta skill e avise: "não consegui consultar a knowledge base agora, usei os padrões internos."

---

## Confirme o resumo

Antes de gerar qualquer arquivo, apresente:

```
Aqui está o que entendi:

**Projeto:** [objetivo em uma frase]
**Por quê:** [valor]
**Quem usa:** [usuario_final]
**Stack:** [stack ou "a definir"]
**Primeira entrega:** [mvp]

Posso criar os arquivos agora?
```

Se o usuário confirmar, siga para a geração.

---

## Geração dos arquivos

### 1. CLAUDE.md

Gere na raiz do projeto com esta estrutura:

```markdown
# [Nome inferido do projeto]

## O que é este projeto
[objetivo] — [valor]

## Quem usa
[usuario_final]

## Stack
[stack]

## Como prefiro que você se comunique
- Respostas em português (Brasil)
- Sem jargão técnico — explique termos novos em uma linha
- Antes de tarefas não triviais, mostre um plano em 3 bullets e espere aprovação
- Se eu estiver seguindo um caminho ruim, me avise

## Regras de trabalho
- "Rodou" não significa "está certo": valide uma amostra e me diga o que conferiu
- Foque no mínimo que entrega valor — não expanda o escopo sem perguntar

## Meta desta sessão
[mvp]
```

### 2. Estrutura de pastas

Crie as pastas com `mkdir -p`:

**Para todos os projetos:**
```
memory/
```

**Por tipo de projeto (inferir pelo stack/objetivo):**

| Tipo | Pastas extras |
|------|--------------|
| Análise de dados | `data/raw/`, `data/output/`, `scripts/`, `notebooks/` |
| Automação | `flows/`, `scripts/`, `docs/` |
| POC de produto | `src/`, `public/`, `docs/` |
| Vibe-coding / AI Engineering | `src/`, `prompts/`, `tests/`, `docs/` |
| Knowledge base / estudo | `kb/`, `docs/`, `scripts/` |

### 3. Skills relevantes

Copie da pasta `skills/` deste repositório (se disponíveis) para `.claude/skills/` do novo projeto:

| Tipo de projeto | Skills recomendadas |
|----------------|---------------------|
| Análise de dados | `bigquery-workflow`, `setup-review` |
| Automação / AI Engineering | `coach-claude-code`, `setup-review` |
| POC de produto | `coach-claude-code`, `setup-review` |
| Qualquer | `setup-review` (sempre) |

**Comando para copiar:**
```bash
mkdir -p .claude/skills/<nome-da-skill>
cp <caminho-do-repositorio-co-coach>/skills/<nome-da-skill>/SKILL.md .claude/skills/<nome-da-skill>/SKILL.md
```

### 4. settings.json

Crie `.claude/settings.json` com permissões básicas seguras e um hook que lembra o usuário de salvar a sessão. Adapte a lista de permissões ao `stack`:

```json
{
  "permissions": {
    "allow": [
      "Read(*)",
      "Bash(ls:*)",
      "Bash(cat:*)",
      "Bash(grep:*)",
      "Bash(mkdir:*)"
    ]
  }
}
```

**Permissões extras por tipo de projeto** (adicione ao array `allow`):

| Tipo | Permissões extras |
|------|------------------|
| Análise de dados | `"Bash(python:*)"`, `"Bash(bq:*)"` |
| Automação / AI Engineering | `"Bash(python:*)"`, `"Bash(node:*)"` |
| POC de produto | `"Bash(npm:*)"`, `"Bash(npx:*)"` |
| Knowledge base / estudo | `"Bash(git:*)"` |

> Explique ao usuário em uma linha: "permissões dizem quais comandos eu posso rodar sem te perguntar toda vez — comecei com os mais seguros (ler arquivos, listar pastas)."

### 5. Backlog inicial

Crie `memory/backlog-inicial.md`:

```markdown
# Backlog Inicial — [Nome do projeto]
Criado em: [data de hoje]

## Tarefas

- [ ] **[mvp]** ← comece aqui
- [ ] Definir stack final e instalar dependências
- [ ] Criar primeiro teste manual que valide o objetivo
- [ ] Documentar o que funcionou (atualizar CLAUDE.md)
- [ ] Definir próxima entrega após o MVP
```

---

## Finalização

Após gerar todos os arquivos, mostre ao usuário:

```
Projeto configurado! Aqui está o que foi criado:

📄 CLAUDE.md — contexto do projeto para o Claude Code
📁 Pastas: [lista das pastas criadas]
🔧 Skills instaladas: [lista]
⚙️ .claude/settings.json — permissões básicas configuradas
📋 memory/backlog-inicial.md — suas próximas 5 tarefas

**Próximo passo:** [mvp]

Quer começar agora?
```
