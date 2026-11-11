import json,re,subprocess
from concurrent.futures import ThreadPoolExecutor
o=json.load(open('deb_p2b_patches.json'))
cand=[]
for x in o:
    for t,vl in x['hits']:
        if re.search(r'(pyproject\.toml|setup\.py|setup\.cfg)$',t) and any(l[0]=='-' for l in vl) and any(l[0]=='+' for l in vl):
            cand.append((x['file'],t,vl)); break
cand.sort(key=lambda c:c[0]); sel=cand[:20]
print(len(cand),'candidates with -/+ version in patch; selected first 20 alphabetical')
def fetch(c):
    f,t,vl=c; pv=f.split('/')[0]; pkg,ver=pv.split('_',1)
    pre=pkg[:4] if pkg.startswith('lib') else pkg[0]
    tgt=re.sub(r'^[ab]/','',t); 
    # strip leading dir components until a known filename
    base=t.split('/')[-1]
    res={}
    for path in [base]+[tgt]:
        u=f"https://sources.debian.org/data/main/{pre}/{pkg}/{ver}/{path}"
        txt=subprocess.run(['curl','-s','-m','60',u],capture_output=True).stdout.decode('utf8','replace')
        if txt and '<html' not in txt[:200].lower(): 
            lines=[(i+1,l.strip()) for i,l in enumerate(txt.split('\n')) if re.match(r'\s*(version|__version__)\s*[=:]|\s*version\s*=|dynamic|use_scm_version|setuptools_scm',l)]
            return {'pkg':pkg,'deb':ver,'patch':f.split('/')[-1],'file':base,'url':u,'patch_lines':vl[:3],'upstream_lines':lines[:5]}
    return {'pkg':pkg,'deb':ver,'patch':f.split('/')[-1],'file':base,'url':None,'patch_lines':vl[:3],'upstream_lines':[]}
with ThreadPoolExecutor(8) as ex: R=list(ex.map(fetch,sel))
json.dump(R,open('deb_p3_raw.json','w'),indent=1)
for r in R: print(r['pkg'],r['deb'],'|',r['file'],'|',[l[:40] for l in r['patch_lines'][:2]],'=>',[f"{n}:{l[:45]}" for n,l in r['upstream_lines'][:3]])
