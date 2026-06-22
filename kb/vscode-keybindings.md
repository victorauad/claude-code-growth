---
titulo: "VS Code: Atalhos de Teclado e Personalização"
tema: ferramentas
url: https://code.visualstudio.com/docs/getstarted/keybindings
data: 2026-06-22
fonte: vscode-docs
importancia: alta
---

# VS Code: Atalhos de Teclado

Guia completo de atalhos e como personalizar o teclado no VS Code.

## Acessar o Editor de Atalhos

- **Mac**: ⌘K ⌘S
- **Windows/Linux**: Ctrl+K Ctrl+S
- Ou via menu: File > Preferences > Keyboard Shortcuts
- Referência completa em PDF: Help > Keyboard Shortcut Reference

## Atalhos Mais Importantes

### Navegação Geral
| Função | macOS | Windows/Linux |
|--------|-------|---------------|
| Command Palette | ⇧⌘P | Ctrl+Shift+P |
| Quick Open (arquivo) | ⌘P | Ctrl+P |
| Terminal integrado | ⌃` | Ctrl+` |
| Buscar no arquivo | ⌘F | Ctrl+F |
| Sidebar | ⌘B | Ctrl+B |
| Panel inferior | ⌘J | Ctrl+J |
| Fechar todos editores | ⌘K ⌘W | Ctrl+K Ctrl+W |

### Edição de Texto
| Função | macOS | Windows/Linux |
|--------|-------|---------------|
| Multi-cursor (click) | Option+Click | Alt+Click |
| Multi-cursor ↑/↓ | ⌥⌘↑/↓ | Ctrl+Alt+Up/Down |
| Selecionar todas ocorrências | ⇧⌘L | Ctrl+Shift+L |
| Próxima ocorrência (uma a uma) | ⌘D | Ctrl+D |
| Copiar linha acima/abaixo | ⇧⌥↑/↓ | Shift+Alt+Up/Down |
| Mover linha acima/abaixo | ⌥↑/↓ | Alt+Up/Down |
| Selecionar linha inteira | ⌘L | Ctrl+L |
| Formatar documento | ⇧⌥F | Shift+Alt+F |
| Comentar linha | ⌘/ | Ctrl+/ |

### Navegação no Código
| Função | macOS | Windows/Linux |
|--------|-------|---------------|
| Ir para definição | F12 | F12 |
| Ver definição inline (Peek) | ⌥F12 | Alt+F12 |
| Voltar (posição anterior) | ⌃- | Alt+Left |
| Ir para linha | ⌃G | Ctrl+G |
| Símbolo no arquivo | ⇧⌘O | Ctrl+Shift+O |
| Renomear símbolo | F2 | F2 |

## Como Personalizar Atalhos

### Via Interface Gráfica
No editor de atalhos (Ctrl+K Ctrl+S), pesquise o comando desejado e clique para editar.

### Via JSON (keybindings.json)
```json
{
  "key": "ctrl+shift+x",
  "command": "seu.comando.aqui",
  "when": "editorTextFocus"
}
```

Para **remover** um atalho, prefixe com hífen: `"command": "-nomeComando"`

Para executar **múltiplos comandos** com um atalho:
```json
{
  "key": "ctrl+alt+c",
  "command": "runCommands",
  "args": {
    "commands": ["comando1", "comando2"]
  }
}
```

## Keymaps para Migrantes

Se você veio de outro editor, instale um keymap para manter seus atalhos:
- File > Preferences > Migrate Keyboard Shortcuts from...
- Disponível: Vim, Sublime Text, Emacs, Atom, Eclipse, Visual Studio

## Resolução de Conflitos

- Clique direito em um atalho → **Show Same Keybindings** para ver sobreposições
- Ative **Developer: Toggle Keyboard Shortcuts Troubleshooting** para logs detalhados

## Filtrar Atalhos Modificados

No editor de atalhos, use `@source:user` para ver apenas os que você personalizou.
