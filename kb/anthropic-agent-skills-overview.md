---
titulo: "Agent Skills — Visão Geral (Anthropic Docs)"
tema: skills
url: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
data: 2026-06-23
fonte: anthropic-docs
importancia: alta
---

# Agent Skills — Visão Geral

## Por que usar Skills

Skills são recursos reutilizáveis baseados em sistema de arquivos que fornecem ao Claude expertise específica de domínio: workflows, contexto e melhores práticas que transformam agentes generalistas em especialistas. Ao contrário de prompts (instruções de nível de conversa para tarefas únicas), Skills carregam sob demanda e eliminam a necessidade de fornecer as mesmas orientações repetidamente.

**Benefícios principais:**
- **Especialize o Claude**: adapte capacidades para tarefas específicas de domínio
- **Reduza repetição**: crie uma vez, use automaticamente
- **Componha capacidades**: combine Skills para criar workflows complexos

## Como Skills funcionam — 3 níveis de carregamento

Skills aproveitam o ambiente de VM do Claude para fornecer capacidades além do que é possível apenas com prompts. Claude opera em uma máquina virtual com acesso ao sistema de arquivos.

### Nível 1: Metadados (sempre carregados)
O frontmatter YAML da Skill fornece informações de descoberta:
```yaml
---
name: pdf-processing
description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
---
```
Claude carrega esses metadados na inicialização. Abordagem leve: você pode instalar muitas Skills sem penalidade de contexto.

### Nível 2: Instruções (carregadas quando acionadas)
O corpo principal do SKILL.md contém conhecimento procedimental: workflows, melhores práticas e orientações. Quando o usuário solicita algo que corresponde à descrição de uma Skill, Claude lê SKILL.md via bash.

### Nível 3: Recursos e código (carregados conforme necessário)
Skills podem agrupar materiais adicionais: outros arquivos .md, scripts executáveis e recursos de referência. Claude acessa esses arquivos apenas quando referenciados.

| Nível | Quando Carregado | Custo de Tokens | Conteúdo |
|-------|-----------------|-----------------|---------|
| Metadados | Sempre (na inicialização) | ~100 tokens por Skill | name e description do frontmatter YAML |
| Instruções | Quando Skill é acionada | Menos de 5k tokens | Corpo do SKILL.md |
| Recursos | Conforme necessário | Efetivamente ilimitado | Arquivos agrupados executados via bash |

## Estrutura de uma Skill

Toda Skill requer um arquivo `SKILL.md` com frontmatter YAML:

```yaml
---
name: your-skill-name
description: Brief description of what this Skill does and when to use it
---

# Your Skill Name

## Instructions
[Clear, step-by-step guidance for Claude to follow]

## Examples
[Concrete examples of using this Skill]
```

**Campos obrigatórios:** `name` e `description`

Requisitos do campo `name`:
- Máximo 64 caracteres
- Apenas letras minúsculas, números e hífens
- Sem tags XML
- Sem palavras reservadas: "anthropic", "claude"

## Onde Skills funcionam

### Claude API
Suporta Skills pré-construídas e personalizadas. Especifique o `skill_id` relevante no parâmetro `container`. Requer três headers beta: `code-execution-2025-08-25`, `skills-2025-10-02`, `files-api-2025-04-14`.

### Claude Code
Suporta apenas Skills Personalizadas. Crie Skills como diretórios com arquivos SKILL.md. Claude descobre e usa automaticamente. Skills são baseadas em sistema de arquivos e não requerem uploads de API.

### claude.ai
Suporta Skills pré-construídas e personalizadas. Skills personalizadas são específicas de usuário (não compartilhadas por organização).

## Skills Pré-construídas disponíveis

- **PowerPoint (pptx)**: Crie apresentações, edite slides
- **Excel (xlsx)**: Crie planilhas, analise dados, gere relatórios com gráficos
- **Word (docx)**: Crie documentos, edite conteúdo, formate texto
- **PDF (pdf)**: Gere documentos PDF formatados e relatórios

## Considerações de segurança

Use Skills apenas de fontes confiáveis. Skills fornecem ao Claude novas capacidades através de instruções e código — uma Skill maliciosa pode direcionar o Claude a invocar ferramentas de maneiras prejudiciais. Trate a instalação de uma Skill como instalar software: audite todos os arquivos antes de usar.

## Limitações importantes

- Skills personalizadas não sincronizam entre superfícies (claude.ai, API e Claude Code são separados)
- claude.ai: Skills são individuais por usuário
- Claude API: Skills são por workspace (todos os membros do workspace têm acesso)
- Claude Code: Personal (`~/.claude/skills/`) ou por projeto (`.claude/skills/`)
- Claude API não tem acesso à rede nas Skills e não permite instalação de pacotes em runtime

## Links relacionados

- [Boas práticas de autoria](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- [Skills no Claude Code](https://code.claude.com/docs/en/skills)
- [Guia de Skills com a API](https://platform.claude.com/docs/en/build-with-claude/skills-guide)
