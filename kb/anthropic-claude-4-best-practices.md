---
titulo: "Boas Práticas de Prompt para Claude 4 (e modelos atuais)"
tema: prompts
url: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices
data: 2026-06-22
fonte: anthropic-docs
importancia: alta
---

# Boas Práticas de Prompt — Claude 4 e Modelos Atuais

Guia oficial da Anthropic para Claude Fable 5, Opus 4.8, Opus 4.6, Sonnet 4.6 e Haiku 4.5.

## Princípios Gerais

### Seja Claro e Direto
Claude responde bem a instruções explícitas. Pense nele como um funcionário brilhante novo que não conhece seus workflows.

**Regra de ouro:** mostre o prompt a um colega com pouco contexto. Se ele ficaria confuso, o Claude também ficará.

### Adicione Contexto e Motivação
Explicar o *por quê* ajuda o Claude a generalizar melhor.

**Menos eficaz:** `NUNCA use reticências`
**Mais eficaz:** `Sua resposta será lida por text-to-speech, então nunca use reticências pois o engine não saberá como pronunciá-las.`

### Use Exemplos (Few-Shot)
3-5 exemplos bem escolhidos melhoram drasticamente a consistência. Use tags `<example>` para separar exemplos de instruções.

### Estruture com XML Tags
XML tags ajudam o Claude a parsear prompts complexos sem ambiguidade: `<instructions>`, `<context>`, `<input>`, `<document>`.

### Dê um Papel ao Claude
Uma linha de papel no system prompt faz diferença: `"Você é um assistente especializado em Python."`

## Controle de Formato

- **Diga o que fazer, não o que não fazer**: Em vez de "Não use markdown", use "Escreva em parágrafos fluentes."
- **Combine o estilo do prompt com o output desejado**: menos markdown no prompt → menos markdown na saída
- **Claude 4+ tem estilo mais conciso e conversacional** que versões anteriores

## Tool Use

Claude 4.6 é mais literal em seguir instruções. Para fazer o Claude agir (não só sugerir):

**Menos eficaz:** `Pode sugerir mudanças nesta função?`
**Mais eficaz:** `Mude esta função para melhorar a performance.`

Para paralelizar chamadas de ferramentas: adicione prompt explícito solicitando chamadas paralelas quando não há dependências.

## Thinking e Raciocínio

- Claude Opus 4.6 e Sonnet 4.6 usam **adaptive thinking** (`thinking: {type: "adaptive"}`) — decide automaticamente quando e quanto pensar
- Use o parâmetro `effort` para controlar a profundidade do raciocínio
- Substitui o antigo `budget_tokens` (depreciado)

## Sistemas Agênticos

### Raciocínio de Longo Horizonte
Claude 4.6 é excepcional em manter estado e orientação em sessões longas. Para tarefas multi-janela:
1. Use git para rastrear estado entre sessões
2. Escreva testes em formato estruturado (JSON) antes de implementar
3. Crie scripts de setup para retomar trabalho com novo contexto

### Evitar Overengineering
Claude Opus 4.5/4.6 tende a criar abstrações desnecessárias. Para evitar: adicione instrução explícita pedindo soluções mínimas e focadas.

### Balancear Autonomia e Segurança
Oriente o Claude sobre ações reversíveis vs. irreversíveis, especialmente em ambientes de produção.

## Mudanças de Claude 3 para Claude 4

- Prefilled responses no último assistant turn **não são mais suportados** (erro 400) nos modelos 4.6+
- Thinking usa `adaptive` em vez de `budget_tokens`
- Modelo é mais proativo — reduza instruções de "force tool use" que eram necessárias antes
- Melhor seguimento de instruções, visão e frontend design
