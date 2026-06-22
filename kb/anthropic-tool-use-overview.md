---
titulo: "Tool Use com Claude — Visão Geral"
tema: agentes
url: https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview
data: 2026-06-22
fonte: anthropic-docs
importancia: alta
---

# Tool Use com Claude

Tool use permite que o Claude chame funções que você define ou que a Anthropic fornece. O Claude decide quando chamar uma ferramenta com base no pedido do usuário e na descrição da ferramenta.

## Como Funciona

### Client Tools (ferramentas do cliente)
Claude retorna `stop_reason: "tool_use"` + blocos `tool_use`. Sua aplicação executa a operação e retorna `tool_result`. O Claude então continua com base no resultado.

### Server Tools (ferramentas do servidor)
Executam na infraestrutura da Anthropic. Você vê os resultados diretamente, sem precisar lidar com a execução. Exemplos: `web_search`, `code_execution`, `web_fetch`.

## Quando o Claude Usa Ferramentas

Com `tool_choice: {"type": "auto"}` (padrão), o Claude decide por conta própria. Para forçar mais uso de ferramentas:

- Suave: `"Use as ferramentas para investigar antes de responder."`
- Forte: `"Sempre chame uma ferramenta primeiro antes de responder."`
- Para garantia: use `tool_choice` forçado na API

## MCP (Model Context Protocol)

Para conectar a servidores MCP, use o [MCP connector](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector). Para construir seu próprio cliente MCP, veja [modelcontextprotocol.io](https://modelcontextprotocol.io).

## Strict Tool Use

Adicione `strict: true` nas definições de ferramentas para garantir que as chamadas do Claude sempre correspondam ao schema exato.

## Precificação

Tool use é cobrado com base em:
1. Total de tokens de input (incluindo o parâmetro `tools`)
2. Tokens de output gerados
3. Para server tools: cobrança adicional por uso (ex: web_search cobra por busca realizada)

A Anthropic adiciona automaticamente um system prompt para tool use. Tokens adicionais por modelo (com pelo menos 1 tool):

| Modelo | auto/none | any/tool |
|--------|-----------|----------|
| Claude Opus 4.8 | 290 tokens | 410 tokens |
| Claude Sonnet 4.6 | 497 tokens | 589 tokens |
| Claude Haiku 4.5 | 496 tokens | 588 tokens |

## Impacto em Benchmarks

Em benchmarks como LAB-Bench FigQA e SWE-bench, adicionar ferramentas básicas produz grandes ganhos de performance, frequentemente superando baselines de especialistas humanos.
