---
titulo: "Agent Skills — Visão Geral (Anthropic Docs)"
tema: skills
url: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
data: 2026-06-23
fonte: anthropic-docs
importancia: alta
---

# Agent Skills — Visão Geral

## O que são Agent Skills

Agent Skills são capacidades modulares que estendem a funcionalidade do Claude. Cada Skill empacota instruções, metadados e recursos opcionais (scripts, templates) que o Claude usa automaticamente quando relevante.

**Benefícios principais:**
- **Especializar o Claude**: adaptar capacidades para tarefas específicas de domínio
- **Reduzir repetição**: criar uma vez, usar automaticamente
- **Compor capacidades**: combinar Skills para construir workflows complexos

## Como Skills funcionam — 3 níveis de carregamento

Skills operam num ambiente de VM onde o Claude tem acesso ao filesystem, comandos bash e execução de código.

### Nível 1: Metadata (sempre carregada)
O frontmatter YAML da Skill fornece informações de descoberta (~100 tokens por Skill):
```yaml
---
name: pdf-processing
description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
---
```

### Nível 2: Instruções (carregadas quando ativada)
O corpo principal do SKILL.md com workflows, boas práticas e orientações (<5k tokens).

### Nível 3: Recursos e código (carregados conforme necessário)
Scripts executáveis, arquivos de referência, templates — sem limite prático de tamanho porque não consomem contexto até serem acessados.

| Nível | Quando Carregado | Custo em Tokens |
|-------|-----------------|-----------------|
| Nível 1: Metadata | Sempre (na inicialização) | ~100 tokens por Skill |
| Nível 2: Instruções | Quando Skill é ativada | Menos de 5k tokens |
| Nível 3+: Recursos | Conforme necessário | Efetivamente ilimitado |

## Onde Skills funcionam

- **Claude API**: Skills pré-construídas e customizadas via parâmetro `skill_id`
- **Claude Code**: apenas Skills customizadas baseadas em filesystem
- **claude.ai**: Skills pré-construídas e customizadas (upload como .zip)

## Estrutura de uma Skill

```yaml
---
name: your-skill-name
description: Brief description of what this Skill does and when to use it
---

# Your Skill Name

## Instructions
[Orientações claras e passo a passo para o Claude seguir]

## Examples
[Exemplos concretos de uso desta Skill]
```

**Campos obrigatórios:** `name` e `description`

Requisitos:
- `name`: máx 64 chars, apenas letras minúsculas/números/hífens, sem palavras reservadas "anthropic" ou "claude"
- `description`: não vazio, máx 1024 chars, sem tags XML, deve incluir o que faz E quando usar

## Skills pré-construídas disponíveis

- **PowerPoint (pptx)**: criar apresentações, editar slides
- **Excel (xlsx)**: criar planilhas, analisar dados, gerar relatórios
- **Word (docx)**: criar documentos, editar conteúdo
- **PDF (pdf)**: gerar documentos PDF formatados

## Arquitetura

Skills rodam num ambiente de execução de código onde o Claude tem acesso ao filesystem via bash. O acesso progressivo garante que apenas conteúdo relevante ocupe a janela de contexto a qualquer momento.

Exemplo de fluxo:
1. **Startup**: sistema inclui metadata: `PDF Processing - Extract text and tables...`
2. **Pedido do usuário**: "Extraia o texto deste PDF"
3. **Claude invoca**: `bash: read pdf-skill/SKILL.md` → Instruções carregadas no contexto
4. **Claude executa**: usa instruções do SKILL.md para completar a tarefa

## Considerações de segurança

Use Skills apenas de fontes confiáveis. Skills fornecem ao Claude novas capacidades via instruções e código — Skills maliciosas podem direcionar invocações de ferramentas de maneiras prejudiciais, incluindo exfiltração de dados e acesso não autorizado ao sistema.

## Retenção de dados

Agent Skills não é coberta por acordos ZDR (Zero Data Retention). Dados são retidos conforme a política padrão da Anthropic.
