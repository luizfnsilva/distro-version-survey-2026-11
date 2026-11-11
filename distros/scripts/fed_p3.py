import re,random,json,sys
sys.path.insert(0,'.')
from p3lib import check
random.seed(1)
names=[l.strip() for l in open('fed/pretend.txt')]+[l.strip() for l in open('fed/sed.txt')]
names=sorted(set(names));random.shuffle(names)
out=[]
for n in names:
    if len(out)>=20:break
    t=open('fed/specs/'+n).read()
    v=re.search(r'^Version:\s*(\S+)',t,re.M);gh=re.search(r'github\.com/([\w.-]+/[\w.-]+?)(?:\.git)?(?:/|\s|$)',t)
    if not v or not gh or '%' in v.group(1):continue
    r=check(gh.group(1),v.group(1));r['spec']=n;r['src']='pretend' if n in open('fed/pretend.txt').read() else 'sed'
    out.append(r);print(n,r['dist_version'],r.get('declared'),r['cls'],flush=True)
json.dump(out,open('fed/p3.json','w'),indent=1)
