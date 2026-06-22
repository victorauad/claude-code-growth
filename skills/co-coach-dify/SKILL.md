---
name: co-coach-dify
description: Orienta na criação de aplicações de IA usando o Dify — plataforma visual sem código. Use quando quiser criar chatbots internos, fluxos de processamento de documentos ou aplicações de IA para clientes sem escrever código.
---

# Dify — Plataforma visual de IA

Você é um guia para criar aplicações de IA com o Dify, sem precisar escrever código.

## Quando ativar

- "Quero criar um chatbot que responde sobre os meus documentos"
- "Como criar uma aplicação de IA sem programar"
- "Preciso de um fluxo automatizado com IA"
- "Usa o Dify", "configura o Dify"

## Pré-requisito: Docker

Verifique se o Docker está instalado:
```bash
docker --version
```

Se não tiver: https://docker.com/get-started

## Instalação

```bash
git clone https://github.com/langgenius/dify.git
cd dify/docker
cp .env.example .env
docker compose up -d
```

Acesse em: http://localhost/

## Casos de uso típicos

| Caso | Como configurar |
|------|----------------|
| Q&A sobre documentos internos | Knowledge Base → Upload PDFs → Chatbot |
| Resumo automático de PDFs | Workflow → Input: PDF → Summarize Node |
| Agente que pesquisa na web | Agent → Tool: Web Search → Output |
| Chatbot de atendimento | Chatbot → Base de conhecimento customizada |

## Fluxo básico no Dify

1. **Criar aplicação** → Escolher tipo (Chatbot, Agent, Workflow)
2. **Adicionar Knowledge Base** → Upload de PDFs, URLs ou textos
3. **Configurar modelo** → Selecionar Claude (requer API Key da Anthropic)
4. **Testar** → Painel de preview interno
5. **Publicar** → Gera URL de embed ou API

## Configurar Claude no Dify

Em Settings → Model Providers → Anthropic:
- API Key: sua chave da Anthropic
- Modelo recomendado: `claude-sonnet-4-6`

## Referência

- Repositório: https://github.com/langgenius/dify
- Documentação: https://docs.dify.ai
