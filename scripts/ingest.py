#!/usr/bin/env python3
"""
Processa um link enviado via GitHub Issue e salva um resumo em 07-inbox/.
Lê a URL da variável de ambiente INPUT_URL.
As funções summarize() e save_to_inbox() são importáveis por outros scripts.
"""

import os
import re
import sys
import json
import datetime
import unicodedata
import requests
from pathlib import Path
from bs4 import BeautifulSoup
import anthropic

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[-\s]+", "-", text)[:60]


def is_youtube(url: str) -> bool:
    return "youtube.com" in url or "youtu.be" in url


def fetch_youtube_transcript(url: str) -> str:
    from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound

    video_id_match = re.search(r"(?:v=|youtu\.be/)([A-Za-z0-9_-]{11})", url)
    if not video_id_match:
        return ""
    video_id = video_id_match.group(1)
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=["pt", "en"])
        return " ".join(t["text"] for t in transcript[:300])  # primeiros ~5 min
    except Exception:
        pass

    # fallback: busca título e descrição da página do YouTube
    try:
        resp = requests.get(url, timeout=15, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(resp.text, "html.parser")
        title = soup.find("meta", {"name": "title"}) or soup.find("meta", {"property": "og:title"})
        desc = soup.find("meta", {"name": "description"}) or soup.find("meta", {"property": "og:description"})
        title_text = title["content"] if title else ""
        desc_text = desc["content"] if desc else ""
        if title_text or desc_text:
            return f"Título: {title_text}\nDescrição: {desc_text}"
    except Exception:
        pass

    return ""


def fetch_article_text(url: str) -> str:
    try:
        resp = requests.get(url, timeout=15, headers={"User-Agent": "Mozilla/5.0"})
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer", "header"]):
            tag.decompose()
        text = soup.get_text(separator=" ", strip=True)
        return text[:8000]  # limita para não explodir o contexto
    except Exception as e:
        return f"Não foi possível extrair o conteúdo: {e}"


def summarize(url: str, content: str) -> dict:
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    prompt = f"""Você é um assistente especializado em Claude Code, IA aplicada ao trabalho e Growth/Martech.

Analise o conteúdo abaixo (extraído de {url}) e retorne um JSON com exatamente esta estrutura:

{{
  "titulo": "título em português, claro e descritivo (máximo 80 caracteres)",
  "tema": "uma das categorias: setup | metodologia | agentes | mcp | ferramentas | workflow | prompts | outros",
  "bullets": ["ponto 1", "ponto 2", "ponto 3"],
  "citacao": "uma frase ou trecho relevante do conteúdo original (em aspas, em português ou traduzida)",
  "importancia": "em 1-2 frases: por que isso importa para alguém que é Head de Growth em Martech e usa Claude Code como ferramenta de trabalho"
}}

Conteúdo:
{content[:6000]}

IMPORTANTE: Retorne APENAS o JSON puro, começando com {{ e terminando com }}. Sem markdown, sem ```json, sem texto antes ou depois."""

    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )

    raw = message.content[0].text.strip()
    # remove blocos markdown caso o modelo os inclua
    if raw.startswith("```"):
        raw = re.sub(r"^```[a-z]*\n?", "", raw)
        raw = re.sub(r"\n?```$", "", raw)
        raw = raw.strip()

    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        print(f"Resposta inesperada da API:\n{raw[:500]}")
        raise


def save_to_inbox(url: str, data: dict, extra_frontmatter: dict | None = None) -> str:
    today = datetime.date.today().strftime("%Y-%m-%d")
    slug = slugify(data["titulo"])
    filename = f"{today}-{slug}.md"
    filepath = os.path.join("07-inbox", filename)
    extra_frontmatter = extra_frontmatter or {}

    bullets_md = "\n".join(f"- {b}" for b in data["bullets"])

    extra_lines = "".join(f"{k}: {v}\n" for k, v in extra_frontmatter.items())
    content = f"""---
titulo: {data['titulo']}
tema: {data['tema']}
url: {url}
data: {today}
{extra_lines}---

# {data['titulo']}

**Tema:** {data['tema']}
**Fonte:** {url}

## Resumo

{bullets_md}

## Por que isso importa

{data['importancia']}

## Citação

> {data['citacao']}
"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Salvo em: {filepath}")
    return filename


def main():
    input_url = os.environ.get("INPUT_URL", "").strip()
    api_key = os.environ.get("ANTHROPIC_API_KEY")

    if not input_url:
        print("Erro: variável INPUT_URL não definida ou vazia.")
        sys.exit(1)
    if not api_key:
        print("Erro: variável ANTHROPIC_API_KEY não definida.")
        sys.exit(1)

    print(f"Processando: {input_url}")

    if is_youtube(input_url):
        print("Detectado: YouTube. Buscando transcrição...")
        content = fetch_youtube_transcript(input_url)
        if not content:
            print("Transcrição indisponível. Usando URL como referência.")
            content = f"Vídeo do YouTube: {input_url}"
    else:
        print("Detectado: artigo/página. Extraindo texto...")
        content = fetch_article_text(input_url)

    print("Gerando resumo via API Claude...")
    data = summarize(input_url, content)

    filename = save_to_inbox(input_url, data)
    print(f"Concluído: {filename}")


if __name__ == "__main__":
    main()
