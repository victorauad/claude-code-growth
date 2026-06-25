# TASKS — co-coach

> Derivado de [STATUS.md](STATUS.md) em 2026-06-24.
> Legenda: `[ ]` pendente · `[x]` feito · `[-]` descartado

---

## Prioridade alta

- [ ] **iOS Shortcut** — confirmar que o Shortcut está configurado no iPhone e testar o fluxo completo: URL compartilhada → Issue criada com label `add-link` → card no feed em ≤3 min
- [ ] **`docs/proficiency.json`** — criar o arquivo com schema de scores por tema e garantir que a skill `co-coach-quiz` escreve e lê nele corretamente
- [ ] **Estatísticas no feed mobile** — adicionar rodapé ao `docs/index.html` gerado por `scripts/build-site.py` com: data do último rebuild e contagem de cards por tema

---

## Prioridade média

- [ ] **Skill especializada: `co-coach-mmm`** — criar skill para apoiar análise de Marketing Mix Modeling (contexto do projeto iracing ou do trabalho em Martech)
- [ ] **Dashboard de sync** — adicionar step ao final de `sync-skills.yml` que gera/atualiza `config/sync-status.md` com: repo, skills instaladas, data do último sync
- [ ] **Ingestão de playlists do YouTube** — modificar `scripts/ingest.py` para aceitar URLs de playlist e iterar sobre os vídeos

---

## Prioridade baixa

- [ ] **Changelog automático de KB** — adicionar step no `ingest-link.yml` que acrescenta uma linha em `kb/CHANGELOG.md` com: data, URL e título do conteúdo indexado
- [ ] **Reorganizar `skills/README.md`** — atualizar o índice de skills por categoria: produtividade, marketing, dados, ferramentas, integrações
- [ ] **Step de verificação nos workflows** — adicionar ao `ingest-link.yml` e `sync-skills.yml` um step básico de validação que falha se o arquivo gerado estiver vazio ou malformado

---

## Feito (referência)

- [x] Ingestão via GitHub Issue (testado em Issue #1 — ~23s, card no feed, Issue fechada)
- [x] Feed mobile no ar: `https://victorauad.github.io/co-coach`
- [x] 30+ skills criadas e no padrão `co-coach-*`
- [x] Sync automático de skills para `iracing_analysis` e `alamtoco`
- [x] Workflow de setup de novo projeto (`setup-project.yml`)
- [x] Rebuild automático do site por push em `kb/**` ou `skills/**`
- [x] Memória de sessão via `/co-coach-handoff`
