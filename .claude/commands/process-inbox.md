# Skill: /process-inbox

Você é um assistente especializado em curadoria de conhecimento sobre IA aplicada ao trabalho.

## Objetivo

Processar os links da seção "Aguardando processamento" do arquivo `inbox.md`, extrair os aprendizados relevantes e integrá-los nos arquivos `.md` corretos do repositório.

## Passo a passo

### 1. Ler o inbox
Abra `inbox.md` e colete todos os links da seção **Aguardando processamento**.
Se não houver links, informe o usuário e encerre.

### 2. Para cada link, fazer:

**a) Buscar o conteúdo**
Use WebFetch para acessar o link. Se for vídeo do YouTube, busque a transcrição ou resumo disponível na página. Se for artigo, leia o texto completo.

**b) Extrair os aprendizados**
Identifique:
- Conceito principal (1 frase)
- Aprendizados práticos (até 5 bullets)
- Citações diretas relevantes (no máximo 2)
- Nível: iniciante / intermediário / avançado
- Tema principal (ver lista abaixo)

**c) Classificar o destino**
Use os temas para decidir em qual arquivo `.md` o conteúdo se encaixa:

| Tema | Arquivo destino |
|------|----------------|
| Setup, instalação, primeiros passos | `01-setup/` |
| BigQuery, dados, SQL | `02-fluxos-de-trabalho/banco-de-dados-bigquery.md` |
| Planilhas, Sheets | `02-fluxos-de-trabalho/planilhas-estruturadas.md` |
| POCs, prototipagem | `02-fluxos-de-trabalho/pocs-ai-coding.md` |
| MCP, integrações, ferramentas externas | `02-fluxos-de-trabalho/mcp-hubspot-e-saas.md` |
| Prompts, instruções | `03-metodologias/prompts.md` |
| Skills | `03-metodologias/skills.md` |
| Agentes, subagentes, multi-agente | `03-metodologias/agentes-e-subagentes.md` |
| Workflows, automações | `03-metodologias/workflows.md` |
| Vídeos, palestras | `04-biblioteca-de-estudos/lista-de-videos.md` |
| Ferramentas, repos, OSS | `06-ferramentas-e-repos/` (criar arquivo numerado se necessário) |
| Novo tema sem encaixe | criar arquivo em `03-metodologias/` ou `02-fluxos-de-trabalho/` |

**d) Atualizar o arquivo destino**
Adicione uma nova seção ou item no arquivo correto, no formato:

```markdown
### [Título do conteúdo](URL)
*Fonte: tipo (artigo/vídeo/repo) — Data de adição: DD/MM/AAAA*

Conceito principal em uma frase.

- Aprendizado 1
- Aprendizado 2
- Aprendizado 3

> "Citação direta relevante, se houver."
```

Se o arquivo destino já tiver uma seção compatível, adicione dentro dela. Não duplique conteúdo.

### 3. Atualizar o inbox.md

Mova cada link processado da seção **Aguardando processamento** para a seção **Processados**, no formato:

```
- [Título](URL) — adicionado em DD/MM/AAAA → destino: caminho/do/arquivo.md
```

### 4. Relatório final

Ao terminar, mostre um resumo:

```
✓ X links processados
Destinos atualizados:
  - arquivo1.md (N itens adicionados)
  - arquivo2.md (N itens adicionados)
Temas novos identificados: [lista, se houver]
```

## Regras

- Nunca invente conteúdo. Se não conseguir acessar um link, marque como `⚠️ erro ao acessar` e siga para o próximo.
- Preserve o estilo dos arquivos existentes (tom direto, sem jargão, em português).
- Não apague conteúdo existente nos arquivos destino — apenas adicione.
- Se o link for vídeo e não houver transcrição acessível, extraia o que for possível do título, descrição e comentários pinados.
- Valide: depois de adicionar, confira se o arquivo destino ficou sintaticamente correto (MD válido, sem quebras de formatação).
