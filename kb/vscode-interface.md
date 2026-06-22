---
titulo: "VS Code: Interface e Navegação"
tema: ferramentas
url: https://code.visualstudio.com/docs/getstarted/userinterface
data: 2026-06-22
fonte: vscode-docs
importancia: alta
---

# VS Code: Interface e Navegação

Guia completo dos componentes da interface do VS Code e como navegar com eficiência.

## Seis Áreas da Interface

1. **Editor Central** — espaço principal de edição; suporta múltiplos arquivos lado a lado (vertical ou horizontal)
2. **Activity Bar** — barra à esquerda; alterna entre Explorer, Git, Extensões, etc.
3. **Primary Side Bar** — painel lateral com Explorer, buscas, etc. (pode ser movida para direita)
4. **Secondary Side Bar** — painel oposto, padrão com Chat; drag & drop de views
5. **Status Bar** — barra inferior com informações do arquivo e projeto ativos
6. **Panel** — área abaixo do editor com terminal, erros, output; pode ir para esquerda ou direita

## Atalhos de Teclado Essenciais de Navegação

| Função | macOS | Windows/Linux |
|--------|-------|---------------|
| Command Palette (acesso a tudo) | ⇧⌘P | Ctrl+Shift+P |
| Quick Open (abrir arquivo rápido) | ⌘P | Ctrl+P |
| Ir para linha específica | ⌃G | Ctrl+G |
| Ir para símbolo | ⇧⌘O | Ctrl+Shift+O |
| Dividir editor | ⌘\ | Ctrl+\ |
| Alternar abas abertas | ⌃Tab | Ctrl+Tab |
| Fechar aba atual | ⌘W | Ctrl+W |
| Modo Zen (foco total) | ⌘K Z | Ctrl+K Z |

## Funcionalidades de Produtividade

**Preview Mode**: clique único abre arquivo em modo temporário (aba em itálico). Duplo clique ou edição torna a aba permanente — evita poluir as abas ao navegar.

**Sticky Scroll**: mostra as linhas de cabeçalho dos escopos visíveis coladas no topo do editor. Ótimo para arquivos longos. Ative com `editor.stickyScroll.enabled`.

**Breadcrumbs**: barra de caminho de arquivo acima do editor. Permite clicar para navegar entre pastas e símbolos rapidamente.

**Minimap**: visão miniatura do código no lado direito. Desative com `"editor.minimap.enabled": false` se preferir mais espaço.

**Zen Mode**: oculta toda a UI exceto o editor, entra em tela cheia. Sair com Esc duas vezes.

## Edição Lado a Lado

- `Alt + clique` em arquivo no Explorer → abre ao lado
- `⌘\` (Ctrl+\) → divide o editor atual em dois
- Arrastar abas para qualquer lado do editor
- Arraste abas para fora da janela → cria janela flutuante independente

## Configurações Úteis

```json
"workbench.editor.showTabs": "single"    // desabilita sistema de abas
"editor.minimap.side": "left"             // minimap à esquerda
"editor.minimap.enabled": false           // remove minimap
"window.restoreWindows": "all"            // restaura todas janelas ao abrir
```

## Gerenciamento de Janelas

VS Code preserva estado entre sessões: pasta, layout e arquivos abertos são restaurados automaticamente. Configure com `window.restoreWindows` (`all`, `none`, `one`, `folders`).
