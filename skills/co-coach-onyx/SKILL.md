---
name: co-coach-onyx
description: Orienta na instalação e uso do Onyx — plataforma de chat com IA auto-hospedada que conecta com Google Drive, Slack, Notion, Confluence e 40+ fontes. Use quando quiser criar um buscador interno com IA sem enviar dados sensíveis para serviços externos.
---

# Onyx — Chat com IA privado e auto-hospedado

Você é um guia para instalar e usar o Onyx para criar um sistema de busca interna com IA.

## Quando ativar

- "Quero um ChatGPT interno que acessa nossos documentos"
- "Preciso de busca com IA nos nossos arquivos sem expor dados"
- "Como conectar IA ao Notion, Slack e Google Drive da empresa"
- "Usa o Onyx", "configura o Onyx"

## Pré-requisito: Docker

```bash
docker --version  # verificar instalação
```

## Instalação

```bash
git clone https://github.com/onyx-dot-app/onyx.git
cd onyx/deployment/docker_compose
touch .env  # configurações ficam aqui
docker compose -f docker-compose.dev.yml up -d
```

Acesse em: http://localhost:3000

## Conectores disponíveis (40+)

| Categoria | Fontes |
|-----------|--------|
| Documentos | Google Drive, Confluence, Notion, SharePoint |
| Comunicação | Slack, Microsoft Teams, Gmail |
| Código | GitHub, GitLab, Linear |
| Web | Websites, RSS, Sitemap |
| Dados | PostgreSQL, Salesforce, HubSpot |

## Configurar Claude como modelo

No arquivo `.env`:
```
GEN_AI_MODEL_PROVIDER=anthropic
GEN_AI_MODEL_VERSION=claude-sonnet-4-6
ANTHROPIC_API_KEY=sua-chave-aqui
```

## Casos de uso

- "Qual é nossa política de férias?" → Onyx busca no Notion
- "O que foi decidido na reunião de X?" → Busca no Slack + Confluence
- Onboarding: novos funcionários perguntam, Onyx explica
- Suporte técnico: conectado ao repo de código e documentação

## Referência

- Repositório: https://github.com/onyx-dot-app/onyx
- Documentação: https://docs.onyx.app
