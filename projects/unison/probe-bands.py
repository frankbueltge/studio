import re,os,sys,statistics as st
sys.path.insert(0,'.')
exec(open('probe.py').read().split('issues = list')[0].replace('CACHE = sys.argv[1] if len(sys.argv) > 1 else "cirt"','CACHE="cirt"'))
# radius bands in the newest issue, and step events across the sample
for k in (463,):
    txt,_=get(k); rows,n,bad=parse(txt)
    bands={'<1':0,'1-10':0,'10-100':0,'100-1k':0,'1k-10k':0,'>10k':0}
    for lab,vs in rows:
        v=[x for x in vs if x is not None]
        if not v: continue
        a=abs(st.median(v))
        key = '<1' if a<1 else '1-10' if a<10 else '10-100' if a<100 else '100-1k' if a<1000 else '1k-10k' if a<10000 else '>10k'
        bands[key]+=1
    print('issue',k,'labs',len(rows),'bands',bands)
# step events: consecutive 5-day changes > 1000 ns, within each sampled issue
tot=big=huge=0
for k in list(range(100,464,12))+[463]:
    txt,_=get(k)
    if not txt: continue
    rows,n,bad=parse(txt)
    for lab,vs in rows:
        for a,b in zip(vs,vs[1:]):
            if a is None or b is None: continue
            tot+=1
            d=abs(b-a)
            if d>1000: big+=1
            if d>5000: huge+=1
print('5-day transitions sampled:',tot,'| >1000 ns:',big,'(%.2f%%)'%(100*big/tot),'| >5000 ns:',huge,'(%.2f%%)'%(100*huge/tot))
