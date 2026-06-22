---
titulo: "Skill Authoring Best Practices — Anthropic Docs"
tema: skills
url: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
data: 2026-06-23
fonte: anthropic-docs
importancia: alta
---

# Boas Práticas para Criar Agent Skills

## Princípios centrais

### 1. Concisão é fundamental

O contexto é um bem compartilhado. Sua Skill divide a janela de contexto com o system prompt, histórico da conversa, metadata de outras Skills e a requisição atual.

**Assunção padrão:** Claude já é muito inteligente. Só adicione contexto que o Claude não tem.

**Bom exemplo (conciso, ~50 tokens):**
```python
import pdfplumber
with pdfplumber.open("file.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```

**Mau exemplo (verboso, ~150 tokens):**
"PDF (Portable Document Format) files são um formato comum que contém texto, imagens... Para extrair texto você precisará usar uma biblioteca. Existem muitas opções disponíveis, mas pdfplumber é recomendado porque..."

### 2. Defina o grau certo de liberdade

- **Alta liberdade** (instruções em texto): quando múltiplas abordagens são válidas
- **Média liberdade** (pseudocódigo ou scripts com parâmetros): quando existe um padrão preferido mas variação é aceitável
- **Baixa liberdade** (scripts específicos): quando operações são frágeis e sequências exatas são necessárias

### 3. Teste com todos os modelos que planeja usar

- Claude Haiku (rápido): a Skill fornece orientação suficiente?
- Claude Sonnet (equilibrado): as instruções são claras e eficientes?
- Claude Opus (raciocínio poderoso): a Skill evita superexplicações?

## Convenções de nomenclatura

Use forma gerundiva para nomes de Skills (verbo + -ing):
- `processing-pdfs`
- `analyzing-spreadsheets`
- `managing-databases`

Evite: nomes vagos (`helper`, `utils`), genéricos (`documents`, `data`), palavras reservadas.

## Escrevendo descriptions efetivas

**SEMPRE escreva em terceira pessoa** — a description é injetada no system prompt.
- ✓ Bom: "Processes Excel files and generates reports"
- ✗ Evitar: "I can help you process Excel files"

**Inclua termos-chave e contexto de quando usar:**
```yaml
description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
```

## Padrões de progressive disclosure

Mantenha o corpo do SKILL.md abaixo de 500 linhas. Organize assim:

```text
pdf/
├── SKILL.md              # Instruções principais
├── FORMS.md              # Guia para preenchimento de formulários
├── reference.md          # Referência da API
└── scripts/
    ├── analyze_form.py   # Script utilitário
    └── validate.py       # Script de validação
```

O Claude carrega FORMS.md ou reference.md apenas quando necessário.

**Evite referências profundamente aninhadas** — mantenha todas as referências a um nível de profundidade do SKILL.md.

## Workflows e loops de feedback

Para tarefas complexas, use checklists que o Claude pode marcar conforme progride:

```
Task Progress:
- [ ] Step 1: Analisar o formulário
- [ ] Step 2: Criar mapeamento de campos
- [ ] Step 3: Validar mapeamento
- [ ] Step 4: Preencher o formulário
- [ ] Step 5: Verificar output
```

**Implemente loops de feedback:** Rodar validador → corrigir erros → repetir. Isso melhora muito a qualidade do output.

## Padrões comuns

### Padrão de template
```markdown
## Estrutura do relatório
SEMPRE use esta estrutura exata:
# [Título da Análise]
## Sumário executivo
## Principais achados
## Recomendações
```

### Padrão de exemplos
Forneça pares input/output para que o Claude entenda o estilo desejado.

### Padrão de workflow condicional
```markdown
1. Determine o tipo de modificação:
   - Criando novo conteúdo? → Siga "Workflow de Criação"
   - Editando conteúdo existente? → Siga "Workflow de Edição"
```

## Desenvolvimento iterativo com Claude

**Processo recomendado:**
1. Complete uma tarefa sem Skill — observe que contexto você forneceu repetidamente
2. Identifique o padrão reutilizável
3. Peça ao Claude para criar a Skill capturando esse padrão
4. Revise para concisão
5. Teste com Claude em contexto limpo (Claude B) em tarefas similares
6. Itere baseado em observações do comportamento real

## Checklist para Skills efetivas

- [ ] Description é específica e inclui termos-chave
- [ ] Inclui o QUE faz e QUANDO usar
- [ ] Corpo do SKILL.md abaixo de 500 linhas
- [ ] Sem informações dependentes de tempo
- [ ] Terminologia consistente
- [ ] Exemplos concretos, não abstratos
- [ ] Referências de arquivo a um nível de profundidade
- [ ] Ao menos 3 avaliações criadas
- [ ] Testado com Haiku, Sonnet e Opus

## Para Skills com código executável

- Scripts devem resolver problemas em vez de "passar a bola" para o Claude
- Trate erros explicitamente com mensagens úteis
- Documente constantes — evite "números mágicos"
- Liste pacotes necessários e verifique disponibilidade no ambiente de execução
- Use sempre barras `/` em caminhos de arquivo (não barras invertidas `\`)
- Não ofereça demasiadas opções — forneça um padrão com escape hatch

## Referência MCP

Para Skills que usam ferramentas MCP, sempre use nomes totalmente qualificados:
```markdown
Use the BigQuery:bigquery_schema tool para recuperar schemas de tabelas.
Use the GitHub:create_issue tool para criar issues.
```
