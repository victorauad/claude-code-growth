---
titulo: Codebase-Memory MCP: Motor de Inteligência de Código para Agentes IA
tema: mcp
url: https://github.com/DeusData/codebase-memory-mcp
data: 2026-06-20
fonte: github-stars
github_stars: 9128
github_repo: DeusData/codebase-memory-mcp
---

# Codebase-Memory MCP: Motor de Inteligência de Código para Agentes IA

**Tema:** mcp
**Fonte:** https://github.com/DeusData/codebase-memory-mcp
**GitHub Stars:** 9128

## Resumo

- Indexa repositórios em milissegundos (kernel Linux com 28M LOC em 3 minutos) através de AST analysis com tree-sitter em 158 linguagens
- Reduz tokens em 120x (3.400 vs 412.000) e tool calls em 2.1x vs exploração arquivo-por-arquivo, com análise semântica Hybrid LSP
- Funciona como binário estático único, sem dependências, plug-and-play em 11 agentes (Claude Code, Gemini CLI, Zed, Aider, VS Code, etc)
- Oferece 14 ferramentas MCP: busca, rastreamento de chamadas, análise de impacto, queries Cypher, detecção de código morto e linking HTTP cross-service

## Por que isso importa

Para Heads de Growth em Martech usando Claude Code, isso multiplica a velocidade de desenvolvimento IA e reduz custos de tokens drasticamente, permitindo análises complexas de codebase com minimal overhead. O plugin resolve o gargalo crítico de exploração de código em pipelines de AI Engineering, liberando recursos para escalar automações de growth.

## Citação

> The fastest and most efficient code intelligence engine for AI coding agents. 120x fewer tokens — 5 structural queries: ~3,400 tokens vs ~412,000 via file-by-file search.
