# SERVICE-AS-A-SOFTWARE PARA AGÊNCIAS DE CREATORS
## Do Modelo de Ferramentas ao Modelo de Resultados

> **Premissa:** Uma agência de creators que adota a tese SWAS para de vender "gestão de influenciadores" e passa a vender **resultados mensuráveis de campanha**, com IA executando o trabalho de inteligência e humanos aplicando julgamento nas decisões de alto valor.

---

## 1. O DIAGNÓSTICO: ONDE A AGÊNCIA ESTÁ HOJE

A maioria das agências opera como **Copiloto** — usam planilhas, Notion, ferramentas de analytics — mas o trabalho ainda é feito pela equipe humana. O cliente paga pela equipe, não pelo resultado.

```
MODELO ATUAL (Copiloto)
Cliente paga → por horas/mês de gestão
Agência entrega → relatórios, planilhas, reuniões
Risco → equipe sobrecarregada, escalabilidade limitada

MODELO SWAS (Autopiloto)
Cliente paga → por resultado (CPM negociado, taxa de engajamento, ROI de campanha)
Agência entrega → o outcome, não o processo
Risco → agência assume, IA executa, humano supervisiona
```

---

## 2. O MAPA DE TAREFAS: INTELIGÊNCIA vs. JULGAMENTO

### Tarefas de INTELIGÊNCIA → IA executa

| Tarefa | Hoje (custo humano) | Com IA |
|--------|---------------------|--------|
| Briefing de campanha → script de conteúdo | 2h/campanha | < 5 min |
| Scouting: perfil de creator → fit com marca | 1h por creator | batch automatizado |
| Relatório de performance pós-campanha | 3h/relatório | gerado automaticamente |
| Rascunho de contrato de publi | 1h + revisão jurídica | template + Claude Draft |
| Calendário editorial mensal | 2h de reunião | gerado com base em histórico |
| Análise de comentários (sentimento da audiência) | manual e subjetivo | NLP automatizado |
| Extração de métricas de plataformas (IG, TT, YT) | copiar e colar | API → planilha automática |
| Geração de invoice / nota fiscal de creators | admin manual | formulário → documento |

### Tarefas de JULGAMENTO → Humano decide

| Tarefa | Por que é humano |
|--------|-----------------|
| Aprovação criativa final do conteúdo | Bom gosto, alinhamento de marca, intuição cultural |
| Negociação de contratos de alto valor | Relação, confiança, leitura do outro lado |
| Escolha do creator certo para a marca | Afinidade real, não só números |
| Gestão de crise (cancel culture, entrega errada) | Contexto, sensibilidade, velocidade |
| Definição de estratégia de crescimento do creator | Visão de longo prazo, carreira, reputação |
| Relacionamento com marcas (cliente) | Confiança, upsell, retenção |

---

## 3. O PLAYBOOK DE IMPLEMENTAÇÃO (APRENDA ENQUANTO FAZ)

### Fase 0 — Antes de codar qualquer coisa (Semana 1-2)
**Objetivo:** Mapear onde o dinheiro vai embora.

1. Liste as 10 tarefas que sua equipe mais repete por semana
2. Cronometre cada uma por 5 dias
3. Classifique cada uma: Inteligência (regra, padrão) ou Julgamento (intuição, risco)
4. Calcule: horas × salário médio/hora = custo mensal por tarefa

> **Regra de ouro:** Se você consegue explicar a tarefa em um passo-a-passo para um estagiário novo, a IA consegue fazer.

### Fase 1 — Automatize a tarefa mais cara (Semana 3-4)
**Objetivo:** Primeira vitória rápida e aprendizado prático.

Escolha a tarefa #1 do ranking e automatize **só ela**. Não tente fazer tudo de uma vez.

Exemplo típico em agências: **Relatório semanal de performance**
- Antes: analista passa 3h coletando dados e montando deck
- Depois: dados entram via API/planilha → Claude gera narrativa → humano revisa e envia

### Fase 2 — Monte o "Sistema Nervoso" (Mês 2)
**Objetivo:** Conectar as peças para que dados fluam automaticamente.

Ver stack completo na Seção 4.

### Fase 3 — Venda o resultado, não o processo (Mês 3)
**Objetivo:** Mudar o modelo de precificação.

- Proponha a 1 cliente atual: pagar por resultado (ex: R$ X por creator entregue dentro do KPI)
- Use os dados da Fase 1 para saber seu custo real — a margem é sua
- Se a IA reduziu de 3h para 20min, você tem 2h40 de margem por entrega

---

## 4. O STACK OTIMIZADO

> Critérios: fácil de usar sem saber programar, custo acessível para PME, cada ferramenta ensina algo reaproveitável.

### CAMADA 1 — Cérebro (IA)

| Ferramenta | Para quê | Custo | Por que aprender |
|-----------|----------|-------|-----------------|
| **Claude (claude.ai)** | Drafts, análise, estratégia, extração de dados de PDFs/prints | ~$20/mês (Pro) | Interface de chat, sem código. Aprende prompting |
| **Claude API via Claude Code** | Automatizar tarefas recorrentes, gerar relatórios em lote | Pay-per-use (~$5-15/mês no início) | Aprende a instruir IA com precisão |

### CAMADA 2 — Automação (Fluxo de trabalho)

| Ferramenta | Para quê | Custo | Por que aprender |
|-----------|----------|-------|-----------------|
| **Make.com** (antigo Integromat) | Conectar apps sem código: "quando X acontecer, faça Y" | Free até 1000 ops/mês | Pensamento de automação visual. Referência do mercado |
| **n8n** (alternativa self-hosted) | Mesma coisa, mas sem limite e com mais controle | ~$20/mês (cloud) ou grátis (self-host) | Aprende lógica de workflows, exportável para qualquer empresa |

> **Recomendação:** Comece com Make.com (mais visual e fácil). Migre para n8n quando quiser mais controle ou economizar.

### CAMADA 3 — Dados e CRM

| Ferramenta | Para quê | Custo | Por que aprender |
|-----------|----------|-------|-----------------|
| **Airtable** | Base de dados de creators, marcas, campanhas, contratos | Free / $20/mês (Pro) | Banco de dados com cara de planilha. Aprende estruturar dados |
| **Google Sheets** | Relatórios, dashboards simples, input de dados da equipe | Grátis | Universal. Toda empresa usa |
| **BigQuery** (opcional) | Analytics avançado quando o volume crescer | Pay-per-query (~R$0 no início) | SQL básico abre portas enormes |

### CAMADA 4 — Conteúdo e Comunicação

| Ferramenta | Para quê | Custo | Por que aprender |
|-----------|----------|-------|-----------------|
| **Notion** | Base de conhecimento da agência, briefings, processos | Free / $10/mês | PKM (gestão de conhecimento). Serve para vida toda |
| **Gamma.app** | Apresentações de resultado para clientes geradas por IA | Free / $15/mês | Aprende prompt-to-presentation |
| **Typeform** | Briefing do cliente → dados estruturados automaticamente | Free até 10 responses | UX de formulário inteligente |

### CAMADA 5 — Monitoramento de Creators

| Ferramenta | Para quê | Custo |
|-----------|----------|-------|
| **Modash / HypeAuditor** | Scouting e análise de autenticidade de audiência | $99-199/mês |
| **Metricool** | Agendamento + analytics multi-plataforma | Free / $22/mês |
| **Phantombuster** (uso cuidadoso) | Scraping de dados públicos de perfis | $56/mês |

---

## 5. FLUXO DE TRABALHO AUTOMATIZADO (EXEMPLO REAL)

### Fluxo: Scouting → Proposta → Contrato

```
[1] Cliente preenche Typeform de briefing
        ↓ (Make.com detecta nova resposta)
[2] Make.com cria linha no Airtable com dados do briefing
        ↓ (Make.com dispara prompt para Claude API)
[3] Claude analisa briefing + lista de creators no Airtable
    → gera lista de 5 creators recomendados com justificativa
        ↓ (Make.com envia para Notion como página de proposta)
[4] Humano revisa e aprova creators
        ↓ (Make.com dispara)
[5] Claude gera rascunho de contrato personalizado
        ↓
[6] Humano revisa → assina via DocuSign/PandaDoc
        ↓
[7] Airtable atualiza status da campanha automaticamente
```

**Tempo antes:** 2 dias de trabalho humano
**Tempo depois:** 30 minutos (humano só nas etapas 4 e 6)

---

## 6. PRECIFICAÇÃO NO MODELO SWAS

### Antes (Copiloto)
```
Retainer mensal: R$ 8.000/mês
→ inclui: gestão, relatórios, reuniões, scouting
→ cliente paga pelo tempo da equipe
→ margem limitada pela capacidade da equipe
```

### Depois (Autopiloto)
```
Performance fee: R$ X por creator entregue no KPI
+ Setup fee: R$ 5.000 (único, para onboarding e automação)
+ Margem oculta: IA faz 80% do trabalho, equipe foca em 20% de alto valor
```

**A regra dos US$ 1:6 aplicada:**
Se a marca gasta R$ 10.000 em produção de conteúdo, ela gasta ~R$ 60.000 em serviços ao redor (gestão, logística, relatórios). **Esse é o seu mercado real.**

---

## 7. KPIs PARA MEDIR SE ESTÁ FUNCIONANDO

| Métrica | Antes | Meta com IA |
|---------|-------|-------------|
| Horas por relatório | 3h | < 30min |
| Tempo de scouting (por creator) | 45min | < 5min |
| Custo por campanha gerenciada | R$ X | Reduzir 40% |
| Campanhas simultâneas por pessoa | 3-4 | 8-10 |
| NPS do cliente | - | Medir baseline |

---

## 8. ARMADILHAS PARA EVITAR

1. **Automatizar antes de entender** — primeiro faça manual 10 vezes, depois automatize
2. **Ferramentas demais de uma vez** — escolha UMA ferramenta por camada e domine
3. **IA sem revisão humana em saídas para o cliente** — sempre revise antes de enviar
4. **Esquecer o "porquê" do cliente** — resultado que importa é o do cliente, não a automação em si
5. **Dados bagunçados no Airtable** — lixo dentro, lixo fora. Comece com estrutura limpa

---

## 9. CRONOGRAMA DE 90 DIAS

```
MÊS 1 — Diagnose e primeira automação
  Semana 1-2: Mapeie e cronometre as 10 tarefas mais frequentes
  Semana 3-4: Automatize a #1 com Make.com + Claude

MÊS 2 — Construa o sistema nervoso
  Semana 5-6: Configure Airtable como CRM central
  Semana 7-8: Conecte Airtable + Make.com + Claude (fluxo de scouting)

MÊS 3 — Pivote o modelo comercial
  Semana 9-10: Proponha modelo de resultado para 1 cliente atual
  Semana 11-12: Meça, documente, replique
```

---

## 10. LEITURA COMPLEMENTAR

- [Sequoia Capital — Services: The New Software](https://sequoiacap.com/article/services-the-new-software)
- [Sequoia Capital — The Reasoning Era Begins](https://sequoiacap.com/article/generative-ais-act-o1/)
- [SWAS — Tese base](./SWAS.md)

---

> **Princípio central:** Você não está construindo um produto de software. Está construindo uma **máquina de entregar resultados** onde a IA faz o trabalho de inteligência repetível e sua equipe aplica julgamento onde realmente importa.
