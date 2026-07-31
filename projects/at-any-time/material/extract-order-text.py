import re, sys, zlib
def extract(path):
    data = open(path,'rb').read()
    out = []
    for m in re.finditer(rb'stream\r?\n', data):
        start = m.end()
        end = data.find(b'endstream', start)
        if end < 0: continue
        raw = data[start:end]
        try: dec = zlib.decompress(raw)
        except Exception: continue
        if b'Tj' not in dec and b'TJ' not in dec: continue
        txt = []
        for tm in re.finditer(rb'\((?:\\.|[^\\()])*\)|TJ|Tj|T\*|Td|TD', dec):
            tok = tm.group(0)
            if tok.startswith(b'('):
                s = tok[1:-1]
                s = re.sub(rb'\\([()\\])', rb'\1', s)
                txt.append(s.decode('latin-1'))
            elif tok in (b'T*',):
                txt.append('\n')
            elif tok in (b'Td', b'TD'):
                txt.append('\n')
        out.append(''.join(txt))
    return '\n'.join(out)
for p in sys.argv[1:]:
    print('='*20, p)
    t = extract(p)
    t = re.sub(r'\n{3,}', '\n\n', t)
    print(t.strip())
