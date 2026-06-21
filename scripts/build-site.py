#!/usr/bin/env python3
"""
Gera o site estático (docs/index.html) a partir de múltiplas pastas do repo.
Roda automaticamente após cada ingestão e semanalmente.
"""

import os
import re
import json
import datetime
from pathlib import Path

DOCS_DIR = Path("docs")
DOCS_DIR.mkdir(exist_ok=True)

# Pastas incluídas no feed e o tema padrão de cada uma
CONTENT_DIRS = [
    (Path("kb"),                      None),           # tema vem do frontmatter
    (Path("06-ferramentas-e-repos"), "ferramentas"),
    (Path("03-metodologias"),        "metodologia"),
    (Path("02-fluxos-de-trabalho"),  "workflow"),
    (Path("04-biblioteca-de-estudos"), "outros"),
    (Path("01-setup"),               "setup"),
    (Path("05-templates"),           "setup"),
]

# Arquivos que são índices/navegação, não conteúdo
SKIP_FILES = {"README.md", "lista-de-videos.md"}


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Extrai o frontmatter YAML simples e o corpo do markdown."""
    meta = {}
    body = text
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            for line in parts[1].strip().splitlines():
                if ":" in line:
                    k, _, v = line.partition(":")
                    meta[k.strip()] = v.strip()
            body = parts[2].strip()
    return meta, body


def extract_title(body: str, fallback: str) -> str:
    """Extrai o primeiro # H1 do markdown como título."""
    match = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
    return match.group(1).strip() if match else fallback


def extract_section(body: str, heading: str) -> str:
    """Extrai o texto de uma seção markdown pelo título."""
    pattern = rf"## {re.escape(heading)}\n+(.*?)(?=\n## |\Z)"
    match = re.search(pattern, body, re.DOTALL)
    return match.group(1).strip() if match else ""


def extract_bullets_from_body(body: str) -> list[str]:
    """Extrai até 3 itens de lista do corpo do arquivo."""
    lines = [l.lstrip("*-• ").strip() for l in body.splitlines() if re.match(r"^\s*[-*•]\s+", l)]
    return [l for l in lines if l][:3]


def first_paragraph(body: str) -> str:
    """Retorna o primeiro parágrafo de texto simples (sem markdown)."""
    for line in body.splitlines():
        line = line.strip()
        if line and not line.startswith("#") and not line.startswith(">") and not line.startswith("|"):
            return re.sub(r"\*+|`", "", line)[:200]
    return ""


def load_cards() -> list[dict]:
    cards = []
    for content_dir, default_tema in CONTENT_DIRS:
        if not content_dir.exists():
            continue
        for md_file in sorted(content_dir.glob("*.md"), reverse=True):
            if md_file.name in SKIP_FILES:
                continue
            text = md_file.read_text(encoding="utf-8")
            meta, body = parse_frontmatter(text)

            # Arquivos com frontmatter (kb): usa campos diretamente
            if meta:
                bullets_raw = extract_section(body, "Resumo")
                bullets = [line.lstrip("- ").strip() for line in bullets_raw.splitlines() if line.strip().startswith("-")]
                importancia = extract_section(body, "Por que isso importa")
                titulo = meta.get("titulo", md_file.stem)
                tema = meta.get("tema", default_tema or "outros")
                url = meta.get("url", "#")
                data = meta.get("data", "")
                fonte = meta.get("fonte", "")
                github_repo = meta.get("github_repo", "")
                github_stars = meta.get("github_stars", "")
            else:
                # Arquivos sem frontmatter: extrai título do H1, bullets da lista, resumo do primeiro parágrafo
                titulo = extract_title(body, md_file.stem.replace("-", " ").title())
                tema = default_tema or "outros"
                url = "#"
                data = ""
                fonte = ""
                github_repo = ""
                github_stars = ""
                bullets_section = extract_section(body, "Resumo")
                if bullets_section:
                    bullets = [l.lstrip("- ").strip() for l in bullets_section.splitlines() if l.strip().startswith("-")]
                else:
                    bullets = extract_bullets_from_body(body)
                importancia = first_paragraph(body)

            if not bullets:
                bullets = [first_paragraph(body)] if first_paragraph(body) else ["Ver conteúdo completo no repo"]

            cards.append({
                "titulo": titulo,
                "tema": tema,
                "url": url,
                "data": data,
                "bullets": bullets,
                "importancia": importancia,
                "filename": md_file.name,
                "pasta": content_dir.name,
                "fonte": fonte,
                "github_repo": github_repo,
                "github_stars": github_stars,
            })
    return cards


def load_proficiency() -> dict:
    """Lê docs/proficiency.json; retorna {} se não existir."""
    p = DOCS_DIR / "proficiency.json"
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


TEMA_CORES = {
    "setup": "#4CAF50",
    "metodologia": "#2196F3",
    "agentes": "#9C27B0",
    "mcp": "#FF9800",
    "ferramentas": "#00BCD4",
    "workflow": "#F44336",
    "prompts": "#FFEB3B",
    "outros": "#757575",
}


STATUS_BADGE = {
    "novo":   ("🆕", "#555555"),
    "visto":  ("👁", "#2196F3"),
    "domina": ("✓",  "#4CAF50"),
}


def card_html(card: dict) -> str:
    bullets_html = "".join(f"<li>{b}</li>" for b in card["bullets"])
    cor = TEMA_CORES.get(card["tema"], "#757575")
    data_str = f'<span class="data">{card["data"]}</span>' if card["data"] else f'<span class="data pasta">{card["pasta"]}</span>'
    status = card.get("status_proficiency", "novo")
    badge_icon, badge_color = STATUS_BADGE.get(status, ("🆕", "#555555"))
    badge_html = f'<span class="badge-status" style="background:{badge_color}" title="{status}">{badge_icon}</span>'
    return f"""
<article class="card" data-tema="{card['tema']}" data-titulo="{card['titulo'].lower()}" data-importancia="{card['importancia'].lower()}">
  <div class="card-header">
    <span class="tag" style="background:{cor}">{card['tema']}</span>
    <div class="card-header-right">{data_str}{badge_html}</div>
  </div>
  <h2><a href="{card['url']}" target="_blank" rel="noopener">{card['titulo']}</a></h2>
  <ul>{bullets_html}</ul>
  <div class="importancia">
    <strong>Por que importa:</strong> {card['importancia']}
  </div>
</article>"""


def proficiency_panel_html(prof: dict) -> str:
    temas_data = prof.get("temas", {})
    if not temas_data:
        return ""
    linhas = []
    for tema, dados in sorted(temas_data.items(), key=lambda x: -x[1].get("score", 0)):
        score = dados.get("score", 0)
        blocos = "█" * (score // 10) + "░" * (10 - score // 10)
        exposicao = dados.get("exposicao", 0)
        qa = dados.get("quiz_acertos", 0)
        qt = dados.get("quiz_total", 0)
        quiz_str = f"quiz: {qa}/{qt}" if qt > 0 else "sem quiz"
        cor = TEMA_CORES.get(tema, "#757575")
        fill_pct = score
        linhas.append(
            f'<div class="prof-barra">'
            f'<span class="prof-nome" style="color:{cor}">{tema}</span>'
            f'<div class="prof-track"><div class="prof-fill" style="width:{fill_pct}%;background:{cor}"></div></div>'
            f'<span class="prof-pct">{score}%</span>'
            f'<span class="prof-detalhe">visto {exposicao}x · {quiz_str}</span>'
            f'</div>'
        )
    ultima = prof.get("ultima_atualizacao", "")
    updated_str = f'<span class="prof-updated">Atualizado em {ultima}</span>' if ultima else ""
    return f"""<section class="proficiency-panel">
  <h2>Progresso por Tema <button class="prof-toggle" onclick="toggleProf()">▼</button></h2>
  {updated_str}
  <div id="prof-content">{''.join(linhas)}</div>
  <p class="prof-hint">Use <code>/proficiency-check</code> no Claude Code para fazer um quiz e atualizar os scores.</p>
</section>"""


def build_html(cards: list[dict], prof: dict = None) -> str:
    if prof is None:
        prof = {}
    # Injeta status de proficiência em cada card
    cards_prof = prof.get("cards", {})
    for c in cards:
        status = cards_prof.get(c["filename"], {}).get("status", "novo")
        c["status_proficiency"] = status

    cards_html = "\n".join(card_html(c) for c in cards)
    temas = sorted(set(c["tema"] for c in cards))
    tema_buttons = "".join(
        f'<button class="filtro-btn" data-tema="{t}" style="border-color:{TEMA_CORES.get(t,"#757575")}">{t}</button>'
        for t in temas
    )
    total = len(cards)
    updated = datetime.date.today().strftime("%d/%m/%Y")

    cards_json = json.dumps(cards, ensure_ascii=False)
    panel_html = proficiency_panel_html(prof)

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Claude Code Growth — Feed</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<header>
  <h1>Claude Code Growth</h1>
  <p class="subtitle">{total} conteúdos indexados · Atualizado em {updated}</p>
</header>

{panel_html}

<div class="context-box">
  <label for="context-input">O que estou fazendo agora:</label>
  <input id="context-input" type="text" placeholder="Ex: estruturando meu CLAUDE.md, pipeline de BigQuery, criando agentes..." />
  <p class="context-hint">Digite para ver os conteúdos mais relevantes primeiro.</p>
</div>

<div class="filtros">
  <button class="filtro-btn active" data-tema="todos">todos</button>
  {tema_buttons}
</div>

<main id="feed">
{cards_html}
</main>

<footer>
  <p>Alimentado por <a href="https://github.com/victorauad/claude-code-growth">claude-code-growth</a></p>
</footer>

<script>
const cards = {cards_json};
let temaAtivo = 'todos';

function score(card, query) {{
  if (!query) return 0;
  const q = query.toLowerCase();
  const campos = [card.titulo, card.tema, card.importancia, ...card.bullets].join(' ').toLowerCase();
  return (campos.match(new RegExp(q.split(' ').filter(Boolean).join('|'), 'g')) || []).length;
}}

function render() {{
  const query = document.getElementById('context-input').value;
  const articles = document.querySelectorAll('.card');

  let visiveis = Array.from(articles).filter(el => {{
    const tema = el.dataset.tema;
    return temaAtivo === 'todos' || tema === temaAtivo;
  }});

  const ocultos = Array.from(articles).filter(el => !visiveis.includes(el));
  ocultos.forEach(el => el.style.display = 'none');

  if (query.trim()) {{
    visiveis.sort((a, b) => {{
      const cardA = cards.find(c => c.titulo.toLowerCase() === a.dataset.titulo);
      const cardB = cards.find(c => c.titulo.toLowerCase() === b.dataset.titulo);
      return score(cardB, query) - score(cardA, query);
    }});
  }}

  const feed = document.getElementById('feed');
  visiveis.forEach(el => {{
    el.style.display = '';
    feed.appendChild(el);
  }});
}}

function toggleProf() {{
  const el = document.getElementById('prof-content');
  const btn = document.querySelector('.prof-toggle');
  if (el) {{ el.style.display = el.style.display === 'none' ? '' : 'none'; btn.textContent = el.style.display === 'none' ? '▶' : '▼'; }}
}}

document.getElementById('context-input').addEventListener('input', render);

document.querySelectorAll('.filtro-btn').forEach(btn => {{
  btn.addEventListener('click', () => {{
    document.querySelectorAll('.filtro-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    temaAtivo = btn.dataset.tema;
    render();
  }});
}});
</script>
</body>
</html>"""


def build_css() -> str:
    return """:root {
  --bg: #0d1117;
  --card-bg: #161b22;
  --border: #30363d;
  --text: #e6edf3;
  --muted: #8b949e;
  --accent: #58a6ff;
  font-size: 16px;
}

* { box-sizing: border-box; margin: 0; padding: 0; }

body {
  background: var(--bg);
  color: var(--text);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  max-width: 720px;
  margin: 0 auto;
  padding: 1rem;
}

header { padding: 1.5rem 0 1rem; }
header h1 { font-size: 1.4rem; }
.subtitle { color: var(--muted); font-size: 0.85rem; margin-top: 0.25rem; }

.context-box {
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 1rem;
  margin: 1rem 0;
}

.context-box label { display: block; font-size: 0.85rem; color: var(--muted); margin-bottom: 0.5rem; }

#context-input {
  width: 100%;
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 6px;
  color: var(--text);
  font-size: 1rem;
  padding: 0.6rem 0.8rem;
}

#context-input:focus { outline: none; border-color: var(--accent); }
.context-hint { font-size: 0.75rem; color: var(--muted); margin-top: 0.4rem; }

.filtros { display: flex; flex-wrap: wrap; gap: 0.5rem; margin: 1rem 0; }

.filtro-btn {
  background: transparent;
  border: 1px solid var(--border);
  border-radius: 20px;
  color: var(--text);
  cursor: pointer;
  font-size: 0.8rem;
  padding: 0.3rem 0.8rem;
}

.filtro-btn.active, .filtro-btn:hover { background: var(--border); }

.card {
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 1.2rem;
  margin-bottom: 1rem;
}

.card-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem; }

.tag {
  border-radius: 4px;
  color: #000;
  font-size: 0.72rem;
  font-weight: 600;
  padding: 0.2rem 0.5rem;
  text-transform: uppercase;
}

.data { color: var(--muted); font-size: 0.78rem; }

.card h2 { font-size: 1rem; margin-bottom: 0.75rem; }
.card h2 a { color: var(--accent); text-decoration: none; }
.card h2 a:hover { text-decoration: underline; }

.card ul { padding-left: 1.2rem; font-size: 0.9rem; line-height: 1.6; color: var(--muted); }
.card ul li { margin-bottom: 0.25rem; }

.importancia {
  border-top: 1px solid var(--border);
  font-size: 0.85rem;
  margin-top: 0.75rem;
  padding-top: 0.75rem;
  color: var(--muted);
}

.importancia strong { color: var(--text); }

footer { color: var(--muted); font-size: 0.78rem; padding: 2rem 0 1rem; text-align: center; }
footer a { color: var(--accent); }

.proficiency-panel {
  background: var(--card-bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 1rem;
  margin: 1rem 0;
}

.proficiency-panel h2 { font-size: 0.95rem; margin-bottom: 0.75rem; display: flex; align-items: center; gap: 0.5rem; }
.prof-toggle { background: transparent; border: 1px solid var(--border); border-radius: 4px; color: var(--muted); cursor: pointer; font-size: 0.7rem; padding: 0.1rem 0.4rem; }
.prof-updated { display: block; font-size: 0.72rem; color: var(--muted); margin-bottom: 0.5rem; }

.prof-barra {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.4rem;
  font-size: 0.82rem;
}

.prof-nome { width: 90px; font-weight: 600; flex-shrink: 0; }
.prof-track { flex: 1; background: var(--border); border-radius: 4px; height: 8px; overflow: hidden; }
.prof-fill { height: 100%; border-radius: 4px; transition: width 0.3s; }
.prof-pct { width: 36px; text-align: right; flex-shrink: 0; color: var(--text); font-weight: 600; }
.prof-detalhe { color: var(--muted); font-size: 0.74rem; flex-shrink: 0; }
.prof-hint { font-size: 0.75rem; color: var(--muted); margin-top: 0.75rem; }
.prof-hint code { background: var(--border); border-radius: 3px; padding: 0.1rem 0.3rem; font-size: 0.72rem; }

.card-header-right { display: flex; align-items: center; gap: 0.5rem; }

.badge-status {
  border-radius: 50%;
  width: 22px;
  height: 22px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 0.65rem;
  flex-shrink: 0;
}
"""


def main():
    cards = load_cards()
    print(f"Encontrados {len(cards)} cards em kb/")

    prof = load_proficiency()
    html = build_html(cards, prof)
    css = build_css()

    (DOCS_DIR / "index.html").write_text(html, encoding="utf-8")
    (DOCS_DIR / "style.css").write_text(css, encoding="utf-8")

    # robots.txt para não indexar no Google
    (DOCS_DIR / "robots.txt").write_text("User-agent: *\nDisallow: /\n")

    # Gera knowledge-base.json para consumo pelas skills
    kb_fields = ["titulo", "tema", "url", "data", "bullets", "importancia", "fonte", "github_repo", "github_stars"]
    kb_entries = [{k: c[k] for k in kb_fields} for c in cards]
    (DOCS_DIR / "knowledge-base.json").write_text(
        json.dumps(kb_entries, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"Site gerado em docs/ ({len(cards)} cards)")
    print(f"Knowledge base exportada: docs/knowledge-base.json ({len(kb_entries)} entradas)")


if __name__ == "__main__":
    main()
