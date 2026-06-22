---
titulo: "Integrações de IDE do Claude Code (VS Code e outros)"
tema: setup
url: https://docs.anthropic.com/en/docs/claude-code/ide-integrations
data: 2026-06-22
fonte: anthropic-docs
importancia: alta
---

# Claude Code no VS Code

A extensão do VS Code é a forma recomendada de usar Claude Code no editor. Oferece painel gráfico nativo, diff side-by-side, @-mentions com número de linha, histórico de conversas e múltiplas abas.

## Requisitos

- VS Code 1.98.0 ou superior
- Conta Anthropic (planos Pro, Max, Team, Enterprise ou Console) — sem necessidade de API key

## Como Instalar

- [Instalar para VS Code](vscode:extension/anthropic.claude-code)
- [Instalar para Cursor](cursor:extension/anthropic.claude-code)
- Ou: `Cmd+Shift+X` → buscar "Claude Code" → Instalar

Também funciona em Kiro, Devin Desktop e outros forks do VS Code.

## Primeiros Passos

1. Abrir o painel: clicar no ícone Spark (⚡) no Editor Toolbar (canto superior direito, requer um arquivo aberto)
2. Fazer login na primeira abertura
3. Enviar um prompt — o Claude vê o código selecionado automaticamente
4. Revisar mudanças: diff side-by-side antes de aceitar

## Funcionalidades Principais

- **Modos de permissão**: Normal (pede permissão), Plan (descreve plano antes), Auto-accept
- **@-mentions**: referencie arquivos específicos com linha (`@auth.ts#5-10`)
- **Histórico de sessões**: busca por keyword ou data
- **Múltiplas conversas**: abas separadas para tarefas paralelas
- **Checkpoints**: rebobinar mudanças para um ponto anterior
- **Integração com Chrome**: `@browser` para testar apps web
- **MCP Servers**: adicione via CLI (`claude mcp add`), gerencie via `/mcp` no painel

## Atalhos Principais

| Ação | Mac | Windows/Linux |
|------|-----|---------------|
| Focar input | `Cmd+Esc` | `Ctrl+Esc` |
| Nova conversa em aba | `Cmd+Shift+Esc` | `Ctrl+Shift+Esc` |
| Inserir @-mention | `Option+K` | `Alt+K` |
| Reabrir sessão fechada | `Cmd+Shift+T` | `Ctrl+Shift+T` |

## Diferenças: Extensão vs CLI

A extensão não adiciona `claude` ao PATH. Para usar CLI no terminal integrado, instale separadamente. A extensão tem subconjunto de comandos — type `/` para ver os disponíveis.

## Configurações Relevantes

Arquivo `~/.claude/settings.json` é compartilhado entre extensão e CLI. Adicione `"$schema": "https://json.schemastore.org/claude-code-settings.json"` para autocomplete.
