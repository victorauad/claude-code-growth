---
titulo: "Como Criar Custom Skills no Claude"
tema: skills
url: https://support.claude.com/en/articles/12512198-creating-custom-skills
data: 2026-06-22
fonte: anthropic-docs
importancia: alta
---

# Como Criar Custom Skills no Claude

Custom skills permitem adicionar conhecimento especializado e workflows específicos da organização ao Claude. Disponíveis nos planos Free, Pro, Max, Team e Enterprise (requer execução de código ativada).

## Passo a Passo

### 1. Criar o arquivo skill.md

Todo skill precisa de um diretório contendo minimamente um arquivo `skill.md` com frontmatter YAML:

```yaml
---
name: Brand Guidelines          # máximo 64 caracteres
description: Apply Acme Corp brand guidelines to presentations  # máximo 200 caracteres
---
```

A `description` é crítica: o Claude usa ela para decidir quando invocar o skill.

### 2. Adicionar Recursos

Para conteúdo extenso, crie arquivos complementares (`REFERENCE.md`) no mesmo diretório e referencie-os no arquivo principal.

### 3. Adicionar Scripts (Opcional)

Linguagens suportadas: Python (pandas, numpy, matplotlib), JavaScript/Node.js, ferramentas de edição de arquivo, visualização.

**Importante:** dependências devem estar pré-instaladas — instalação em tempo de execução não é possível.

### 4. Empacotar

```
minha-skill.zip
└── minha-skill/
    ├── skill.md
    └── recursos/
```

O ZIP deve conter a pasta como raiz (não como subpasta).

## Boas Práticas

- **Foco**: crie skills separadas para diferentes workflows
- **Descrições claras**: o Claude usa a descrição para decidir quando invocar
- **Comece simples**: inicie com instruções Markdown antes de scripts complexos
- **Use exemplos**: inclua exemplos de entrada/saída
- **Composição**: skills podem trabalhar juntas automaticamente

## Segurança

- Nunca hardcode informações sensíveis (API keys, senhas)
- Revise skills antes de habilitá-las
- Use conexões MCP para serviços externos

## Exemplos e Templates

Repositório GitHub com exemplos: [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills)
