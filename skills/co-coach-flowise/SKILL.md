---
name: co-coach-flowise
description: Orienta na criação rápida de agentes e chatbots com o Flowise — construtor visual com arrastar e soltar. Use quando quiser prototipar uma aplicação de IA em minutos, criar um chatbot sobre documentos ou testar uma ideia antes de investir em desenvolvimento.
---

# Flowise — Prototipagem rápida de agentes de IA

Você é um guia para criar protótipos de IA com o Flowise usando interface visual.

## Quando ativar

- "Quero testar uma ideia de chatbot rapidamente"
- "Cria um agente que lê PDFs"
- "Como prototipo uma aplicação de IA?"
- "Usa o Flowise", "configura o Flowise"

## Instalação (requer Node.js)

Verifique se tem Node.js: `node --version`

```bash
# Instalar e iniciar
npm install -g flowise
npx flowise start
```

Acesse em: http://localhost:3000

## Ou via Docker

```bash
docker run -d --name flowise -p 3000:3000 flowiseai/flowise
```

## Casos de uso típicos

| Caso | Componentes no Flowise |
|------|----------------------|
| Chatbot sobre PDFs | PDF Loader → Embeddings → Vector Store → Chat Model |
| Agente com busca na web | Agent → Tool: SerpAPI → Claude |
| Q&A sobre site | Web Scraper → Embeddings → Retrieval Chain |
| Resumo automático | Document Loader → Summarization Chain |

## Configurar Claude no Flowise

1. Abrir o editor visual (localhost:3000)
2. Adicionar componente **ChatAnthropic**
3. Configurar:
   - Model: `claude-sonnet-4-6`
   - API Key: sua chave Anthropic
4. Conectar aos outros componentes do fluxo

## Diferença Flowise vs Dify

| | Flowise | Dify |
|--|---------|------|
| Foco | Prototipagem rápida | Aplicações em produção |
| Complexidade | Simples | Mais completo |
| Deploy | Local/simples | Docker completo |

## Referência

- Repositório: https://github.com/FlowiseAI/Flowise
- Documentação: https://docs.flowiseai.com
