---
titulo: Como usar abordagem spec-driven para codificar com IA — JetBrains
tema: metodologia
url: https://blog.jetbrains.com/junie/2025/10/how-to-use-a-spec-driven-approach-for-coding-with-ai/
data: 2026-06-25
importancia: 4
---

# Como usar abordagem spec-driven para codificar com IA — JetBrains

**Tema:** metodologia
**Fonte:** https://blog.jetbrains.com/junie/2025/10/how-to-use-a-spec-driven-approach-for-coding-with-ai/

## Resumo

- JetBrains (criadores do IntelliJ, PyCharm) adotaram SDD como metodologia principal para seu agente Junie
- Specs devem focar em comportamento, gerenciamento de estado e interfaces — não em implementação detalhada
- O ciclo prático: escrever spec em markdown → deixar o agente propor um plano → aprovar o plano → agente executa → validar contra a spec original
- Specs ruins são vagas demais ("faça um sistema de login") ou específicas demais (ditando como o código deve ser escrito linha a linha)
- O ponto de equilíbrio: spec define o "o quê" e as restrições; o agente decide o "como"

## Por que isso importa

JetBrains tem décadas de experiência em ferramentas para desenvolvedores e integrou SDD diretamente no Junie. O artigo é prático, com exemplos reais de specs bem e mal escritas — útil para aprender o ponto certo de abstração antes de usar Claude Code.

## Citação

> "The spec should focus on behaviour, state management, and interfaces — not pixel-perfect design or implementation details."
