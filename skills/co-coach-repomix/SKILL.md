---
name: co-coach-repomix
description: Usa o Repomix para compactar um projeto inteiro em um único arquivo de texto otimizado para o Claude. Use quando o usuário pedir para analisar um projeto completo, fazer refatoração de múltiplos arquivos, gerar documentação do codebase ou precisar que o Claude veja todo o contexto de um repo.
---

# Repomix — Comprime projeto para o Claude

Você é um assistente que ajuda a usar o Repomix para preparar projetos para análise pelo Claude.

## Quando ativar

- Usuário quer analisar a arquitetura de um projeto inteiro
- Refatoração que afeta múltiplos arquivos
- Gerar documentação automática do codebase
- Onboarding: "explica esse projeto para mim"
- "Usa o Repomix", "comprime o projeto", "manda tudo para o Claude"

## Como usar

### Opção 1: Sem instalar (recomendada para começar)

```bash
# Na raiz do projeto que você quer analisar:
npx repomix
```

Isso gera `repomix-output.txt` — cole esse arquivo no Claude.

### Opção 2: Instalar globalmente

```bash
npm install -g repomix
repomix
```

### Opção 3: Analisar um repo remoto

```bash
npx repomix --remote https://github.com/usuario/repo
```

### Opção 4: Ignorar arquivos desnecessários

```bash
npx repomix --ignore "node_modules,dist,*.log"
```

## Configuração avançada (repomix.config.json)

```json
{
  "output": {
    "filePath": "repomix-output.txt",
    "style": "markdown"
  },
  "ignore": {
    "patterns": ["node_modules", "dist", ".git", "*.lock"]
  }
}
```

## Dica de uso com Claude

Depois de gerar o arquivo:
1. Abra o `repomix-output.txt`
2. Cole no Claude ou use `claude < repomix-output.txt` no terminal
3. Peça o que precisa: "analisa a arquitetura", "onde estão os gargalos de performance", etc.

## Referência

- Repositório: https://github.com/yamadashy/repomix
- Documentação: https://repomix.com
