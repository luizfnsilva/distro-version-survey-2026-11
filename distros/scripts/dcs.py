import re,json,sys,time,urllib.parse,subprocess,html
def get(u): return subprocess.run(['curl','-s','-m','120',u],capture_output=True).stdout.decode('utf8','replace')
def crawl(q,out):
    res=[];p=0;npg=None
    while True:
        u="https://codesearch.debian.net/search?perpkg=1&q="+urllib.parse.quote_plus(q)+"&page=%d"%p
        for k in range(5):
            t=get(u)
            if 'show?file' in t: break
            time.sleep(5)
        if npg is None:
            m=re.search(r'Pages:(.*?)</div>|Pages:(.*)',t,re.S)
            nums=re.findall(r'page=(\d+)',t); npg=max(map(int,nums))+1 if nums else 1
        for m in re.finditer(r'<li><a href="/show\?file=([^"&]+)&(?:amp;)?line=(\d+)[^"]*"><code>.*?</code>:\d+</a><br>\s*<pre>(.*?)</pre>',t,re.S):
            f=urllib.parse.unquote(m.group(1)); body=html.unescape(re.sub(r'<[^>]*>','',m.group(3).replace('<br>','\n')))
            hit=re.sub(r'<br>','\n',m.group(3)); 
            res.append({'file':f,'line':int(m.group(2)),'ctx':body,'hl':html.unescape(re.sub(r'<[^>]*>','',''.join(re.findall(r'<strong>(.*?)</strong>',m.group(3)))))})
        p+=1
        if p>=npg or p>60: break
    json.dump(res,open(out,'w'));print(out,len(res),'pages',npg)
if __name__=='__main__': crawl(sys.argv[1],sys.argv[2])
