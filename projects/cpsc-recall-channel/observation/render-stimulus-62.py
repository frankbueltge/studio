#!/usr/bin/env python3
"""Render the built page to plain text for the severed panel of session 62.

The readers must meet the page's words, not its file path, its directory, its markup or
its studio. This script strips tags and writes the visible text to a neutral path. It
adds nothing and removes nothing but markup: every word a reader sees is a word on the
page. Run:  python3 render-stimulus-62.py <index.html> <out.txt>
"""
import html
import re
import sys


def render(path: str) -> str:
    src = open(path, encoding="utf-8").read()
    # drop the style block entirely — it carries no reader-visible words
    src = re.sub(r"<style\b[^>]*>.*?</style>", "", src, flags=re.S | re.I)
    src = re.sub(r"<head\b[^>]*>.*?</head>", "", src, flags=re.S | re.I)
    src = re.sub(r"<!--.*?-->", "", src, flags=re.S)
    # block elements become line breaks so the reading order survives
    src = re.sub(r"</(p|div|h[1-6]|li|blockquote|section|hr|tr)>", "\n\n", src, flags=re.I)
    src = re.sub(r"<(br|hr)\s*/?>", "\n", src, flags=re.I)

    # an ordered list is numbered on the page; a reader must meet it numbered
    def number_ol(match):
        inner = match.group(1)
        counter = [0]

        def item(m):
            counter[0] += 1
            return f"\n{counter[0]}. "

        return re.sub(r"<li\b[^>]*>", item, inner, flags=re.I)

    src = re.sub(r"<ol\b[^>]*>(.*?)</ol>", number_ol, src, flags=re.S | re.I)
    src = re.sub(r"<li\b[^>]*>", "\n", src, flags=re.I)
    src = re.sub(r"<[^>]+>", "", src)
    text = html.unescape(src)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


if __name__ == "__main__":
    out = render(sys.argv[1])
    open(sys.argv[2], "w", encoding="utf-8").write(out)
    print(f"{len(out)} characters written to {sys.argv[2]}")
