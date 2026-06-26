---
titulo: SDD — Ferramentas Kiro, spec-kit e Tessl explicadas por Martin Fowler
tema: metodologia
url: https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html
data: 2026-06-25
importancia: 5
---

# SDD — Ferramentas Kiro, spec-kit e Tessl explicadas por Martin Fowler

**Tema:** metodologia
**Fonte:** https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html

## Resumo

- Martin Fowler compara as três principais ferramentas de SDD: Kiro (AWS), spec-kit e Tessl, cada uma com abordagem diferente para specs
- Kiro gera automaticamente três documentos: requirements.md (histórias de usuário em EARS notation), design.md (arquitetura técnica) e tasks.md (passos de implementação)
- spec-kit é a abordagem mais leve: funciona sobre qualquer editor com um arquivo de spec em markdown estruturado
- Tessl vai além e trata o spec como código-fonte — o código é o artefato derivado, não o spec
- A escolha da ferramenta depende do tamanho do time e do nível de formalidade desejado

## Por que isso importa

Fowler é uma das referências mais respeitadas em engenharia de software. Sua análise comparativa das ferramentas SDD é o melhor ponto de partida para quem quer adotar a prática com consciência de trade-offs — especialmente relevante ao usar Claude Code, que suporta os três modelos.

## Citação

> "The spec is the artifact and the code is the build output — similar to how .c files compile to binaries."
