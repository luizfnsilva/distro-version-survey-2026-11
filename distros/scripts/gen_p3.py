import re,random,json,sys,os
sys.path.insert(0,'.')
from p3lib import check
random.seed(1)
fs=sorted(set(open('gentoo-pretend.txt').read().split()+open('gentoo-sed.txt').read().split()))
random.shuffle(fs);out=[];skipped={'mangled':0,'nogithub':0}
for f in fs:
    if len(out)>=20:break
    b=os.path.basename(f)[:-7];m=re.match(r'(.+?)-(\d[\d.]*[a-z]?(?:_\w+)?)(?:-r\d+)?$',b)
    if not m:continue
    pn,pv=m.groups()
    t=open('gentoo/'+f[2:]).read()
    if '_' in pv or pv.startswith('9999'):skipped['mangled']+=1;continue
    gh=re.search(r'github\.com/([\w.-]+/[\w.-]+?)(?:\.git)?(?:/|"|\s|$)',t)
    if not gh:skipped['nogithub']+=1;continue
    r=check(gh.group(1),pv);r['ebuild']=f[2:];r['pv']=pv
    out.append(r);print(f[2:],pv,r.get('declared'),r['cls'],flush=True)
print(skipped)
json.dump(out,open('gentoo-p3.json','w'),indent=1)
