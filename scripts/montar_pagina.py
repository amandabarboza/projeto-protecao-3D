"""Monta index.html a partir de src/template.html e dos dados extraídos do DWG.

Uso (na raiz do repositório):
    python scripts/montar_pagina.py
"""
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

template = (RAIZ / "src" / "template.html").read_text(encoding="utf-8")
geo = (RAIZ / "dados" / "geo.json").read_text(encoding="utf-8")
met = (RAIZ / "dados" / "met.json").read_text(encoding="utf-8")

corpo = template.replace("__GEO__", geo).replace("__MET__", met)

pagina = (
    "<!doctype html>\n"
    '<html lang="pt-BR">\n<head>\n'
    '<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    "<style>body{margin:0}[hidden]{display:none!important}</style>\n"
    "</head>\n<body>\n"
    f"{corpo}\n"
    "</body>\n</html>\n"
)

(RAIZ / "index.html").write_text(pagina, encoding="utf-8")
print("index.html gerado")
