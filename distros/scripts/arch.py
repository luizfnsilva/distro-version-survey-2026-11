import json,re,subprocess,urllib.parse
from concurrent.futures import ThreadPoolExecutor
def get(u): return subprocess.run(['curl','-s','-m','60',u],capture_output=True).stdout.decode('utf8','replace')
pk={};p=1
while True:
    j=json.loads(get(f"https://archlinux.org/packages/search/json/?repo=Extra&repo=Extra-Testing&q=python-&limit=250&page={p}"))
    for r in j['results']:
        if r['pkgname'].startswith('python-'): pk[r['pkgbase']]=r['pkgver']
    if p>=j['num_pages']: break
    p+=1
print('python-* pkgbases (extra, name startswith python-):',len(pk),'pages',j['num_pages'])
def one(b):
    t=get(f"https://gitlab.archlinux.org/archlinux/packaging/packages/{urllib.parse.quote(b)}/-/raw/main/PKGBUILD")
    if not t or t.lstrip().startswith('<'): return b,None
    return b,t
with ThreadPoolExecutor(8) as ex: R=dict(ex.map(one,sorted(pk)))
json.dump({'pkgs':pk,'pkgbuild':R},open('arch_pkgbuilds_raw.json','w'))
miss=[b for b,t in R.items() if t is None]; print('missing PKGBUILD',len(miss))
