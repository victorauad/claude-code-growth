---
titulo: Como escrever uma boa spec para agentes de IA — Addy Osmani
tema: prompts
url: https://addyosmani.com/blog/good-spec/
data: 2026-06-25
importancia: 5
---

# Como escrever uma boa spec para agentes de IA — Addy Osmani

**Tema:** prompts
**Fonte:** https://addyosmani.com/blog/good-spec/

## Resumo

- Uma spec para agente de IA precisa responder 6 perguntas obrigatórias — deixar qualquer uma em aberto faz o agente responder por conta própria, geralmente de forma indesejada
- As 6 perguntas: O que o sistema faz? Quem usa? Quais são os limites (in-scope / out-of-scope)? Quais são as restrições técnicas? Como o sucesso é medido? O que pode dar errado?
- Specs focadas em comportamento e interfaces de estado produzem código mais robusto do que specs focadas em layout ou aparência visual
- O nível de detalhe deve ser proporcional à irreversibilidade da decisão — decisões de arquitetura exigem mais detalhe
- Specs iterativas são melhores que specs completas: comece pequeno, refine com o feedback do agente

## Por que isso importa

Addy Osmani é Engineering Manager no Google Chrome. Seu framework de 6 perguntas é direto ao ponto e aplicável imediatamente ao Claude Code — qualquer task complexa fica melhor com essas perguntas respondidas antes de começar.

## Citação

> "Leave any of them open and the agent will answer them for you, in ways you won't like."
