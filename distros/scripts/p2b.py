import json,re,subprocess
from concurrent.futures import ThreadPoolExecutor
r=json.load(open('deb_p2b_raw.json'))
files=sorted({x['file'] for x in r})
def fetch(f):
    pv,path=f.split('/',1); pkg,ver=pv.split('_',1)
    pre=pkg[:4] if pkg.startswith('lib') else pkg[0]
    u=f"https://sources.debian.org/data/main/{pre}/{pkg}/{ver}/{path}"
    t=subprocess.run(['curl','-s','-m','60',u],capture_output=True).stdout.decode('utf8','replace')
    return f,u,t
out=[]
with ThreadPoolExecutor(8) as ex:
    for f,u,t in ex.map(fetch,files):
        # split into per-file diffs
        hits=[]
        for d in re.split(r'(?m)^(?=diff |--- )',t):
            m=re.search(r'(?m)^\+\+\+ (\S+)',d)
            if not m: continue
            tgt=m.group(1)
            if re.search(r'(pyproject\.toml|setup\.py|setup\.cfg|package\.json|Cargo\.toml)$',tgt):
                vl=[l for l in d.split('\n') if re.match(r'^[-+]\s*(__version__|"?version"?)\s*[=:]',l)]
                if vl: hits.append((tgt,vl[:4]))
        out.append({'file':f,'url':u,'len':len(t),'hits':hits})
json.dump(out,open('deb_p2b_patches.json','w'),indent=0)
ok=[o for o in out if o['hits']]
print(len(files),'patches;',sum(1 for o in out if o['len']==0),'unfetched;',len(ok),'with version change in manifest')
pk={}
for o in ok:
    for t,_ in o['hits']: pk.setdefault(o['file'].split('_')[0],set()).add(t.split('/')[-1])
print(len(pk),'packages'); print(sorted(pk.items())[:40])
