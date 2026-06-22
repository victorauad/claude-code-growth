---
titulo: "O que são Skills no Claude"
tema: skills
url: https://support.claude.com/en/articles/12512176-what-are-skills
data: 2026-06-22
fonte: anthropic-docs
importancia: alta
---

# O que são Skills no Claude

Skills são pastas com instruções, scripts e recursos que o Claude carrega dinamicamente para melhorar o desempenho em tarefas específicas. Funcionam por "progressive disclosure" — o Claude identifica quais skills são relevantes e carrega só o necessário, evitando sobrecarregar o contexto.

## Tipos de Skills

- **Anthropic Skills**: criadas pela Anthropic para documentos (Excel, Word, PowerPoint, PDF). Ativadas automaticamente quando relevante.
- **Custom Skills**: criadas por usuários para workflows específicos — diretrizes de marca, gerar comunicações, criar tarefas em JIRA/Asana, análise de dados.
- **Organization Provisioned Skills**: planos Team e Enterprise — administradores provisionam skills para todos os usuários de forma centralizada.
- **Partner Skills**: skills do Skills Directory (Notion, Figma, Atlassian) integradas com conectores MCP.

## Como Funcionam

O Claude identifica quais skills são relevantes para a tarefa e carrega apenas as informações necessárias no momento certo ("progressive disclosure"). Isso evita sobrecarga do contexto.

## Disponibilidade

Disponível para usuários nos planos Free, Pro, Max, Team e Enterprise — requer que a execução de código esteja ativada.

## Benefícios Principais

- Melhoria de desempenho em tarefas específicas
- Captura de conhecimento organizacional
- Customização sem necessidade de código
- Gerenciamento centralizado (Enterprise)

## Links Úteis

- [Como usar skills no Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
- [Como criar custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
- [Documentação oficial de Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [agentskills.io](https://agentskills.io) — padrão aberto
