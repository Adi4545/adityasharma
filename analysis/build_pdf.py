#!/usr/bin/env python3
"""Render the chapter Markdown to a printable academic PDF."""

from __future__ import annotations

import html
import re
from pathlib import Path

import markdown
from weasyprint import HTML

ROOT = Path(__file__).resolve().parents[1]
MD = ROOT / "manuscript" / "When_the_Algorithm_Meets_the_Absent_Facility_REVISED.md"
OUT = ROOT / "manuscript" / "When_the_Algorithm_Meets_the_Absent_Facility.pdf"
FIG = ROOT / "results" / "figures"

CSS = """
@page {
  size: A4;
  margin: 22mm 20mm 24mm 20mm;
  @bottom-center {
    content: "AIPEG · India's e-waste circular economy · " counter(page);
    font-size: 8.5pt;
    font-family: "Liberation Serif", "Times New Roman", serif;
    color: #444;
  }
}
html { font-size: 10.5pt; }
body {
  font-family: "Liberation Serif", "Times New Roman", "DejaVu Serif", serif;
  line-height: 1.38;
  color: #111;
}
h1 { font-size: 16.5pt; line-height: 1.25; margin: 0 0 0.6em; }
h2 { font-size: 13pt; margin: 1.4em 0 0.45em; border-bottom: 0.4pt solid #333; padding-bottom: 0.15em; page-break-after: avoid; }
h3 { font-size: 11.5pt; margin: 1.1em 0 0.35em; page-break-after: avoid; }
p { margin: 0 0 0.65em; text-align: justify; hyphens: auto; }
ul, ol { margin: 0.2em 0 0.7em 1.3em; }
li { margin-bottom: 0.25em; }
em { font-style: italic; }
strong { font-weight: 700; }
code, .math {
  font-family: "Liberation Mono", "DejaVu Sans Mono", monospace;
  font-size: 0.92em;
}
.math-block {
  display: block;
  text-align: center;
  margin: 0.7em 0;
  font-family: "Liberation Serif", serif;
  font-style: italic;
  font-size: 10.5pt;
}
img {
  max-width: 100%;
  height: auto;
  display: block;
  margin: 0.6em auto;
}
table {
  border-collapse: collapse;
  width: 100%;
  margin: 0.6em 0 1em;
  font-size: 8.4pt;
  page-break-inside: avoid;
}
th, td {
  border: 0.4pt solid #555;
  padding: 3px 5px;
  vertical-align: top;
  text-align: left;
}
th { background: #f2f2f2; }
.authors { font-size: 11pt; margin-bottom: 0.3em; }
.affil { font-size: 9.5pt; color: #333; margin-bottom: 1.1em; }
.keywords { font-size: 9.5pt; margin: 0.8em 0 1.2em; }
"""


def mathify(text: str) -> str:
    def block(m):
        inner = html.escape(m.group(1).strip())
        return f'<div class="math-block">{inner}</div>'

    def inline(m):
        inner = html.escape(m.group(1).strip())
        return f'<span class="math">{inner}</span>'

    text = re.sub(r"\\\[(.*?)\\\]", block, text, flags=re.S)
    text = re.sub(r"\\\((.*?)\\\)", inline, text, flags=re.S)
    return text


def fix_images(html_doc: str) -> str:
    def repl(m):
        src = m.group(1)
        name = Path(src).name
        path = FIG / name
        if path.exists():
            return f'<img src="{path.as_uri()}" alt="{html.escape(name)}"/>'
        return m.group(0)

    return re.sub(r'<img[^>]+src="([^"]+)"[^>]*>', repl, html_doc)


def main():
    raw = MD.read_text(encoding="utf-8")
    # Drop the first markdown title duplication handled by h1
    raw = mathify(raw)
    body = markdown.markdown(
        raw,
        extensions=["tables", "fenced_code", "sane_lists", "nl2br"],
    )
    body = fix_images(body)
    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<title>When the Algorithm Meets the Absent Facility</title>
<style>{CSS}</style>
</head>
<body>
{body}
</body>
</html>"""
    HTML(string=doc, base_url=str(ROOT)).write_pdf(OUT)
    print("Wrote", OUT, "size", OUT.stat().st_size)


if __name__ == "__main__":
    main()
