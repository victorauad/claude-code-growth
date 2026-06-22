---
titulo: "Introdução ao Model Context Protocol (MCP)"
tema: mcp
url: https://modelcontextprotocol.io/introduction
data: 2026-06-22
fonte: anthropic-docs
importancia: alta
---

# O que é o Model Context Protocol (MCP)?

MCP é um padrão aberto para conectar aplicações de IA a sistemas externos. É como um "USB-C para IA" — fornece uma forma padronizada de conectar aplicações de IA a fontes de dados, ferramentas e workflows.

## O que o MCP Habilita?

- Agentes podem acessar Google Calendar e Notion, atuando como assistente pessoal mais personalizado
- Claude Code pode gerar um app web completo a partir de um design no Figma
- Chatbots empresariais podem se conectar a múltiplos bancos de dados para análise via chat
- Modelos de IA podem criar designs 3D no Blender e imprimir via impressora 3D

## Arquitetura

O MCP conecta:
- **Clientes MCP**: aplicações de IA (Claude, ChatGPT, VS Code Copilot, Cursor)
- **Servidores MCP**: fornecem acesso a dados, ferramentas e prompts
- **Fontes de dados**: arquivos locais, bancos de dados, APIs externas

## Por que o MCP Importa?

- **Desenvolvedores**: reduz tempo e complexidade de integração com aplicações de IA
- **Aplicações/Agentes de IA**: acesso a ecossistema de fontes de dados e ferramentas
- **Usuários finais**: aplicações de IA mais capazes que acessam seus dados e tomam ações

## Suporte do Ecossistema

MCP é protocolo aberto suportado por Claude, ChatGPT, VS Code, Cursor, MCPJam e muitos outros — "construa uma vez, integre em qualquer lugar".

## Recursos

- [Documentação completa](https://modelcontextprotocol.io/llms.txt)
- [Construir servidores MCP](https://modelcontextprotocol.io/docs/develop/build-server)
- [Construir clientes MCP](https://modelcontextprotocol.io/docs/develop/build-client)
