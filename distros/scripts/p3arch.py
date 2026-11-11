import json,re,subprocess
from concurrent.futures import ThreadPoolExecutor
d=json.load(open('arch_pkgbuilds_raw.json'));P=d['pkgbuild'];pk=d['pkgs']
a=json.load(open('arch_p2.json'))
sed=[b for b,l in a['sed'] if b not in('python-cvxpy','python-datasets','python-pylint-pydantic','python-pytorch','python-teamcity-messages','python-configobj')]
sel=sed+[b for b in sorted(a['pretend']) if b not in sed][:20-len(sed)]
def get(u): return subprocess.run(['curl','-sL','-m','40',u],capture_output=True).stdout.decode('utf8','replace')
def one(b):
    t=P[b]; ver=pk[b]
    m=re.search(r'github\.com/([\w.-]+/[\w.-]+?)(?:\.git|/)',t)
    repo=m.group(1) if m else None
    cls={'pkg':b,'arch_ver':ver,'repo':repo,'kind':'sed' if b in sed else 'pretend','tag':None,'lines':[]}
    if not repo: return cls
    for tag in (ver,'v'+ver):
        for f in ('pyproject.toml','setup.py','setup.cfg'):
            x=get(f"https://raw.githubusercontent.com/{repo}/{tag}/{f}")
            if x and '404' not in x[:20]:
                L=[(i+1,l.strip()[:90]) for i,l in enumerate(x.split('\n')) if re.match(r'\s*(version|__version__)\s*[=:]|dynamic|use_scm_version|setuptools[-_]scm|versioneer|hatch-vcs|^\s*version\s*=',l)]
                if L: cls.update(tag=tag,file=f,lines=L[:3]); return cls
    return cls
with ThreadPoolExecutor(8) as ex: R=list(ex.map(one,sel))
json.dump(R,open('arch_p3_raw.json','w'),indent=1)
for r in R: print(r['pkg'],r['arch_ver'],r['kind'],r['repo'],r['tag'],r.get('file'),r['lines'][:2])
