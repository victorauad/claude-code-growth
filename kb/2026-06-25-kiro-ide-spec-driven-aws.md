---
titulo: Kiro — IDE da AWS construída para Spec-Driven Development
tema: ferramentas
url: https://kiro.dev/docs/specs/
data: 2026-06-25
importancia: 4
---

# Kiro — IDE da AWS construída para Spec-Driven Development

**Tema:** ferramentas
**Fonte:** https://kiro.dev/docs/specs/

## Resumo

- Kiro é uma IDE lançada pela AWS em julho de 2025 construída nativamente para SDD, substituta do Amazon Q Developer
- Gera automaticamente 3 documentos ao iniciar um projeto: requirements.md (histórias de usuário em EARS notation), design.md (arquitetura técnica) e tasks.md (passos atômicos de implementação)
- Inclui Spec Editor com suporte a OpenAPI, JSON Schema e formatos customizados — o spec vira a fonte de verdade do projeto
- Monitora arquivos de rotas de API e atualiza automaticamente a especificação OpenAPI quando o código muda
- Automated hooks verificam se o código gerado está aderente à spec antes de cada commit

## Por que isso importa

Kiro é evidência de que grandes players (AWS) estão apostando em SDD como o modelo padrão de desenvolvimento com IA. Mesmo usando Claude Code em vez do Kiro, a estrutura de 3 documentos (requirements + design + tasks) é um padrão diretamente adaptável.

## Citação

> "Kiro moves beyond AI coding to agentic engineering — the spec is the source of truth, everything else derives from it."
