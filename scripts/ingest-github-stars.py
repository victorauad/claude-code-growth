#!/usr/bin/env python3
"""
Busca os repositórios estrelados do usuário do GitHub e indexa os novos em 07-inbox/.
Usa GH_PAT para autenticação e ANTHROPIC_API_KEY para sumarização.
"""

import os
import sys
import base64
import datetime
from pathlib import Path

import requests

from ingest import summarize, save_to_inbox, slugify, ANTHROPIC_API_KEY

GITHUB_TOKEN = os.environ.get("GH_PAT", "")
GITHUB_USER = os.environ.get("GITHUB_USER", "victorauad")
MAX_REPOS = int(os.environ.get("MAX_REPOS", "20"))

if not GITHUB_TOKEN:
    print("Erro: variável GH_PAT não definida.")
    sys.exit(1)

if not ANTHROPIC_API_KEY:
    print("Erro: variável ANTHROPIC_API_KEY não definida.")
    sys.exit(1)

HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}


def get_starred_repos(user: str, max_repos: int) -> list[dict]:
    url = f"https://api.github.com/users/{user}/starred?per_page={max_repos}&sort=created&direction=desc"
    resp = requests.get(url, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    return resp.json()


def already_indexed(owner: str, repo: str) -> bool:
    slug = f"{owner}-{repo}".lower()
    return bool(list(Path("07-inbox").glob(f"*-{slug}.md")))


def fetch_readme(owner: str, repo: str) -> str:
    url = f"https://api.github.com/repos/{owner}/{repo}/readme"
    resp = requests.get(url, headers=HEADERS, timeout=15)
    if resp.status_code == 404:
        return ""
    resp.raise_for_status()
    data = resp.json()
    content = base64.b64decode(data["content"]).decode("utf-8", errors="replace")
    # limita para não explodir o contexto
    return content[:8000]


def summarize_repo(repo_url: str, owner: str, repo_name: str, readme: str, stars: int) -> dict:
    context = f"""Este é o README do repositório GitHub {owner}/{repo_name} ({stars} estrelas).
Foco em: o que ele faz, pra quem é útil, tecnologias principais, conexão com Growth/Martech/AI Engineering.

README:
{readme}"""
    return summarize(repo_url, context)


def main():
    print(f"Buscando repos estrelados de {GITHUB_USER} (máx {MAX_REPOS})...")
    repos = get_starred_repos(GITHUB_USER, MAX_REPOS)
    print(f"Total retornado pela API: {len(repos)}")

    processed = 0
    skipped = 0

    for repo in repos:
        owner = repo["owner"]["login"]
        name = repo["name"]
        repo_url = repo["html_url"]
        stars = repo["stargazers_count"]

        if already_indexed(owner, name):
            print(f"[skip] {owner}/{name} — já indexado")
            skipped += 1
            continue

        print(f"[new]  {owner}/{name} ({stars}⭐) — buscando README...")
        readme = fetch_readme(owner, name)
        if not readme:
            readme = f"Repositório: {owner}/{name}\nDescrição: {repo.get('description', 'sem descrição')}"

        print(f"       Gerando resumo...")
        try:
            data = summarize_repo(repo_url, owner, name, readme, stars)
            # garante que o tema seja "ferramentas" se não for definido de forma mais específica
            if data.get("tema") not in {"setup", "metodologia", "agentes", "mcp", "ferramentas", "workflow", "prompts"}:
                data["tema"] = "ferramentas"
            slug = f"{owner}-{name}".lower()
            today = datetime.date.today().strftime("%Y-%m-%d")
            filename = f"{today}-{slug}.md"
            filepath = Path("07-inbox") / filename
            extra = {
                "fonte": "github-stars",
                "github_stars": stars,
                "github_repo": f"{owner}/{name}",
            }
            # save_to_inbox usa o slug do titulo, mas para repos precisamos do slug owner-repo
            # escrevemos diretamente para garantir o nome de arquivo correto
            bullets_md = "\n".join(f"- {b}" for b in data["bullets"])
            extra_lines = "".join(f"{k}: {v}\n" for k, v in extra.items())
            content = f"""---
titulo: {data['titulo']}
tema: {data['tema']}
url: {repo_url}
data: {today}
{extra_lines}---

# {data['titulo']}

**Tema:** {data['tema']}
**Fonte:** {repo_url}
**GitHub Stars:** {stars}

## Resumo

{bullets_md}

## Por que isso importa

{data['importancia']}

## Citação

> {data['citacao']}
"""
            filepath.write_text(content, encoding="utf-8")
            print(f"       Salvo em: {filepath}")
            processed += 1
        except Exception as e:
            print(f"       Erro ao processar {owner}/{name}: {e}")
            continue

    print(f"\nConcluído: {processed} novos indexados, {skipped} pulados (já existentes).")


if __name__ == "__main__":
    main()
