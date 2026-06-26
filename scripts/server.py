#!/usr/bin/env python3
"""
Servidor local para o gerenciador do co-coach.
Expõe endpoints REST simples para ler e salvar arquivos locais.

Uso:
    python scripts/server.py

Acesse o gerenciador em: docs/gerenciador.html (abra no browser)
"""

import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import urlparse, parse_qs

PORT = 8765
ROOT = Path(__file__).parent.parent  # raiz do repo co-coach


class Handler(BaseHTTPRequestHandler):

    def log_message(self, format, *args):
        print(f"  {args[0]} {args[1]}")

    def send_json(self, data, status=200):
        body = json.dumps(data, ensure_ascii=False).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-Length", len(body))
        self.end_headers()
        self.wfile.write(body)

    def send_cors(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_OPTIONS(self):
        self.send_cors()

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        qs = parse_qs(parsed.query)

        if path == "/ping":
            self.send_json({"ok": True})

        elif path == "/skills":
            skills_dir = ROOT / "skills"
            if skills_dir.exists():
                names = sorted([d.name for d in skills_dir.iterdir()
                                if d.is_dir() and (d / "SKILL.md").exists()])
            else:
                names = []
            self.send_json(names)

        elif path == "/file":
            rel = qs.get("path", [None])[0]
            if not rel:
                self.send_json({"error": "path param required"}, 400)
                return
            target = (ROOT / rel).resolve()
            if not str(target).startswith(str(ROOT)):
                self.send_json({"error": "path outside repo"}, 403)
                return
            if not target.exists():
                self.send_json({"error": "file not found"}, 404)
                return
            self.send_json({"content": target.read_text(encoding="utf-8")})

        else:
            self.send_json({"error": "not found"}, 404)

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path

        if path == "/file":
            length = int(self.headers.get("Content-Length", 0))
            body = json.loads(self.rfile.read(length))
            rel = body.get("path")
            content = body.get("content", "")
            if not rel:
                self.send_json({"error": "path required"}, 400)
                return
            target = (ROOT / rel).resolve()
            if not str(target).startswith(str(ROOT)):
                self.send_json({"error": "path outside repo"}, 403)
                return
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
            print(f"  ✅ Salvo: {rel}")
            self.send_json({"ok": True})
        else:
            self.send_json({"error": "not found"}, 404)


if __name__ == "__main__":
    print(f"\n  co-coach servidor local")
    print(f"  Porta: {PORT}")
    print(f"  Raiz:  {ROOT}")
    print(f"\n  Abra docs/gerenciador.html no browser")
    print(f"  Ctrl+C para parar\n")
    HTTPServer(("localhost", PORT), Handler).serve_forever()
