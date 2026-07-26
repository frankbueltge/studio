#!/usr/bin/env python3
"""Minimal PDF text extractor: FlateDecode content streams -> text-showing operators.
Positional: uses Td/TD/TM/T* to break lines. Good enough for a text-only court order list."""
import re, sys, zlib

data = open(sys.argv[1], 'rb').read()

# collect all stream objects
objs = {}
for m in re.finditer(rb'(\d+)\s+(\d+)\s+obj(.*?)endobj', data, re.S):
    objs[int(m.group(1))] = m.group(3)

streams = []
for num, body in objs.items():
    sm = re.search(rb'stream\r?\n(.*?)endstream', body, re.S)
    if not sm:
        continue
    raw = sm.group(1)
    if b'FlateDecode' in body.split(b'stream')[0]:
        try:
            raw = zlib.decompress(raw)
        except Exception:
            continue
    streams.append((num, raw))


def unescape(s):
    out = bytearray()
    i = 0
    while i < len(s):
        c = s[i]
        if c == 0x5c:  # backslash
            i += 1
            if i >= len(s):
                break
            n = s[i]
            mapping = {0x6e: 10, 0x72: 13, 0x74: 9, 0x62: 8, 0x66: 12,
                       0x28: 40, 0x29: 41, 0x5c: 92}
            if n in mapping:
                out.append(mapping[n])
                i += 1
            elif 0x30 <= n <= 0x37:
                oct_digits = ''
                while i < len(s) and 0x30 <= s[i] <= 0x37 and len(oct_digits) < 3:
                    oct_digits += chr(s[i]); i += 1
                out.append(int(oct_digits, 8) & 0xFF)
            elif n == 0x0a:
                i += 1
            else:
                out.append(n); i += 1
        else:
            out.append(c); i += 1
    return bytes(out)


tok = re.compile(rb'\((?:\\.|[^\\()])*\)|<[0-9A-Fa-f\s]*>|\[|\]|[-+0-9.]+|T[dDmJj*]|TD|Tf|BT|ET|\'|"', re.S)

pages_text = []
for num, s in streams:
    if b'BT' not in s:
        continue
    lines = []
    cur = bytearray()
    for m in tok.finditer(s):
        t = m.group(0)
        if t in (b'Td', b'TD', b'T*', b'Tm', b"'", b'"'):
            if cur.strip():
                lines.append(bytes(cur).decode('cp1252', 'replace'))
            cur = bytearray()
        elif t.startswith(b'('):
            cur += unescape(t[1:-1])
        elif t.startswith(b'<') and not t.startswith(b'<<'):
            hexs = re.sub(rb'\s', b'', t[1:-1])
            if len(hexs) % 2:
                hexs += b'0'
            try:
                cur += bytes.fromhex(hexs.decode())
            except Exception:
                pass
    if cur.strip():
        lines.append(bytes(cur).decode('cp1252', 'replace'))
    if lines:
        pages_text.append((num, lines))

pages_text.sort(key=lambda x: x[0])
for num, lines in pages_text:
    print(f'%%% obj {num}')
    for l in lines:
        print(l)
