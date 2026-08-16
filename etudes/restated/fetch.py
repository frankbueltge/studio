import json,urllib.request,os,time,hashlib
q=("https://web.archive.org/cdx/search/cdx?url=ice.gov/doclib/detention/FY25_detentionStats"
   "&matchType=prefix&output=json&fl=original,timestamp,statuscode&collapse=urlkey&limit=400")
rows=[r for r in json.load(urllib.request.urlopen(q,timeout=120))[1:]
      if r[2]=='200' and r[0].endswith('.xlsx')]
rows.sort(key=lambda r:r[1])
man=[]
for orig,ts,_ in rows:
    name=orig.split('/')[-1]; out=f"caps/{name}"
    for attempt in range(4):
        if os.path.exists(out) and os.path.getsize(out)>50000: break
        try:
            b=urllib.request.urlopen(f"https://web.archive.org/web/{ts}id_/{orig}",timeout=240).read()
            open(out,'wb').write(b); time.sleep(2); break
        except Exception as e:
            print("retry",attempt,name,e,flush=True); time.sleep(5*(attempt+1))
    if os.path.exists(out) and os.path.getsize(out)>50000:
        b=open(out,'rb').read()
        man.append({"file":name,"wayback_ts":ts,"orig":orig,"bytes":len(b),
                    "sha256":hashlib.sha256(b).hexdigest()})
        print("OK",name,len(b),flush=True)
    else: print("MISSING",name,flush=True)
json.dump(man,open('caps/manifest.json','w'),indent=1)
print("total",len(man),"of",len(rows))
