---
titulo: "Agent Skills — Melhores Práticas de Autoria (Anthropic Docs)"
tema: skills
url: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
data: 2026-06-23
fonte: anthropic-docs
importancia: alta
---

# Agent Skills — Melhores Práticas de Autoria

## Princípios fundamentais

### Concisão é essencial

A janela de contexto é um bem público. Sua Skill compete por espaço com o prompt do sistema, histórico de conversa, metadados de outras Skills e a solicitação real.

**Suposição padrão:** Claude já é muito inteligente. Adicione apenas contexto que ele não tem. Desafie cada informação:
- "Claude realmente precisa desta explicação?"
- "Posso assumir que Claude sabe isso?"
- "Este parágrafo justifica seu custo em tokens?"

**Bom (conciso, ~50 tokens):**
```python
import pdfplumber
with pdfplumber.open("file.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```

**Ruim (muito verboso, ~150 tokens):** Explica o que são PDFs, como funciona a biblioteca — informações que Claude já sabe.

### Defina o grau de liberdade apropriado

- **Alta liberdade** (instruções em texto): Use quando múltiplas abordagens são válidas, decisões dependem de contexto
- **Liberdade média** (pseudocódigo ou scripts com parâmetros): Use quando existe um padrão preferido mas alguma variação é aceitável
- **Baixa liberdade** (scripts específicos, poucos parâmetros): Use quando operações são frágeis e a consistência é crítica

## Estrutura da Skill

### Convenções de nomenclatura

Use forma gerundiva (verbo + -ing) para nomes de Skills:
- `processing-pdfs` ✓
- `analyzing-spreadsheets` ✓
- `helper` ✗ (muito vago)
- `anthropic-helper` ✗ (palavra reservada)

### Escrever descrições eficazes

O campo `description` permite descoberta de Skills. **Sempre escreva na terceira pessoa** — a descrição é injetada no system prompt.

- **Bom:** "Processes Excel files and generates reports"
- **Evitar:** "I can help you process Excel files"

Inclua tanto o que a Skill faz quanto quando usá-la:
```yaml
description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
```

### Padrões de divulgação progressiva

SKILL.md serve como visão geral que aponta Claude para materiais detalhados conforme necessário (como um sumário em um guia de integração).

**Mantenha o corpo do SKILL.md abaixo de 500 linhas.** Divida conteúdo em arquivos separados ao se aproximar desse limite.

**Padrão 1 — Guia de alto nível com referências:**
```markdown
## Quick start
[instruções básicas]

## Advanced features
- For complete guide: See [FORMS.md](FORMS.md)
- API reference: See [REFERENCE.md](REFERENCE.md)
```

**Padrão 2 — Organização por domínio:**
```
bigquery-skill/
├── SKILL.md (visão geral e navegação)
└── reference/
    ├── finance.md
    ├── sales.md
    └── product.md
```

Evite referências profundamente aninhadas — mantenha referências a um nível de profundidade do SKILL.md.

## Workflows e loops de feedback

### Use workflows para tarefas complexas

```markdown
## Workflow de preenchimento de formulário PDF
- [ ] Passo 1: Analisar formulário (rodar analyze_form.py)
- [ ] Passo 2: Criar mapeamento de campos (editar fields.json)
- [ ] Passo 3: Validar mapeamento (rodar validate_fields.py)
- [ ] Passo 4: Preencher formulário (rodar fill_form.py)
- [ ] Passo 5: Verificar saída (rodar verify_output.py)
```

### Implemente loops de feedback

Padrão comum: Execute validador → corrija erros → repita. Este padrão melhora significativamente a qualidade do output.

## Desenvolvimento iterativo com Claude

A abordagem mais eficaz usa o próprio Claude para desenvolver Skills:
1. Complete uma tarefa sem Skill (Claude A ajuda)
2. Identifique o padrão reutilizável
3. Peça ao Claude A para criar a Skill
4. Revise para concisão
5. Teste com Claude B (instância fresca com a Skill carregada)
6. Itere com base em observações

**Por que funciona:** Claude A entende necessidades de agentes, você fornece expertise de domínio, Claude B revela lacunas através de uso real.

## Anti-padrões a evitar

- **Evite caminhos no estilo Windows** (`scripts\helper.py`): use sempre barras (`scripts/helper.py`)
- **Evite oferecer muitas opções**: forneça um padrão com uma saída de emergência
- **Evite informações sensíveis ao tempo**: use seção "old patterns" para conteúdo legado

## Para Skills com código executável

### Resolva, não delegue

Scripts devem lidar com condições de erro em vez de deixar Claude resolver:

```python
def process_file(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        print(f"File {path} not found, creating default")
        with open(path, "w") as f:
            f.write("")
        return ""
```

### Forneça scripts utilitários

Vantagens de scripts pré-fabricados:
- Mais confiáveis do que código gerado
- Economizam tokens (sem geração de código necessária)
- Garantem consistência entre usos

### Padrão verificar-antes-de-executar

Para operações em lote ou destrutivas: analise → **crie arquivo de plano** → **valide plano** → execute → verifique. Mensagens de erro específicas ajudam Claude a corrigir problemas.

## Checklist para Skills eficazes

**Qualidade principal:**
- [ ] Descrição específica com termos-chave
- [ ] Descrição inclui o que a Skill faz e quando usá-la
- [ ] Corpo do SKILL.md abaixo de 500 linhas
- [ ] Sem informações sensíveis ao tempo
- [ ] Terminologia consistente
- [ ] Referências a um nível de profundidade

**Código e scripts:**
- [ ] Scripts resolvem problemas em vez de delegar ao Claude
- [ ] Tratamento de erros explícito e útil
- [ ] Sem "constantes voodoo" (todos os valores justificados)
- [ ] Pacotes necessários listados e verificados como disponíveis
- [ ] Sem caminhos estilo Windows

**Testes:**
- [ ] Pelo menos 3 avaliações criadas
- [ ] Testado com Haiku, Sonnet e Opus
- [ ] Testado com cenários de uso real
