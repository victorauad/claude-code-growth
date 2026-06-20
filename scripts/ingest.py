#!/usr/bin/env python3
"""
Processa um link enviado via GitHub Issue e salva um resumo em 07-inbox/.
Lê a URL da variável de ambiente INPUT_URL.
"""

import os
import re
import sys
import json
import datetime
import unicodedata
import requests
from bs4 import BeautifulSoup
import anthropic

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
INPUT_URL = os.environ.get("INPUT_URL", "").strip()

if not INPUT_URL:
    print("Erro: variável INPUT_URL não definida ou vazia.")
    sys.exit(1)

if not ANTHROPIC_API_KEY:
    print("Erro: variável ANTHROPIC_API_KEY não definida.")
    sys.exit(1)


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
    except NoTranscriptFound:
        return ""
    except Exception:
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

Retorne apenas o JSON, sem markdown, sem texto adicional."""

    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )

    raw = message.content[0].text.strip()
    return json.loads(raw)


def save_to_inbox(url: str, data: dict) -> str:
    today = datetime.date.today().strftime("%Y-%m-%d")
    slug = slugify(data["titulo"])
    filename = f"{today}-{slug}.md"
    filepath = os.path.join("07-inbox", filename)

    bullets_md = "\n".join(f"- {b}" for b in data["bullets"])

    content = f"""---
titulo: {data['titulo']}
tema: {data['tema']}
url: {url}
data: {today}
---

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
    print(f"Processando: {INPUT_URL}")

    if is_youtube(INPUT_URL):
        print("Detectado: YouTube. Buscando transcrição...")
        content = fetch_youtube_transcript(INPUT_URL)
        if not content:
            print("Transcrição indisponível. Usando URL como referência.")
            content = f"Vídeo do YouTube: {INPUT_URL}"
    else:
        print("Detectado: artigo/página. Extraindo texto...")
        content = fetch_article_text(INPUT_URL)

    print("Gerando resumo via API Claude...")
    data = summarize(INPUT_URL, content)

    filename = save_to_inbox(INPUT_URL, data)
    print(f"Concluído: {filename}")


if __name__ == "__main__":
    main()
