import re, sys, urllib.request, concurrent.futures as cf, json
root = sys.argv[1]; files = [l.strip() for l in open(sys.argv[2])]
VCS = re.compile(r'setuptools-scm|setuptools_scm|hatch-vcs|poetry-dynamic-versioning|uv-dynamic-versioning|versioningit|pdm-backend|dunamai')
def g(rx, s):
    m = re.search(rx, s, re.M); return m.group(1) if m else None
def one(f):
    s = open(f"{root}/{f}").read()
    if VCS.search(s): return f, "vcs-backend", None
    v = g(r'^\s*version = "([^"]+)"', s)
    if 'fetchFromGitHub' not in s: return f, "not-github", None
    o = g(r'owner = "([^"]+)"', s); r = g(r'repo = "([^"]+)"', s) or g(r'pname = "([^"]+)"', s)
    t = g(r'^\s*(?:tag|rev) = (.+?);', s)
    if not (v and o and r and t): return f, "unparsed", None
    t = t.strip().strip('"')
    t = re.sub(r'\$\{(?:finalAttrs\.)?version\}', v, t)
    if t in ("version", "finalAttrs.version"): t = v
    if re.search(r'[${}]', t): return f, "unparsed", None
    try:
        import subprocess; cp = subprocess.run(["curl","-sfL","--max-time","20",f"https://raw.githubusercontent.com/{o}/{r}/{t}/pyproject.toml"],capture_output=True,text=True); assert cp.returncode==0; txt=cp.stdout
    except Exception as e: return f, "fetch-failed", None
    up = g(r'^version\s*=\s*["\']([^"\']+)', txt)
    if up is None: return f, "no-static-version", None
    if up in ("0.0.0", "0", "0.0", "0.0.0.dev0", "0.0.dev0", "0.1.0.dev0", "0.0.1"): return f, "placeholder", (v, t, up)
    return f, ("mismatch" if up != v else "equal"), (v, t, up)
res = list(cf.ThreadPoolExecutor(16).map(one, files))
json.dump(res, open(sys.argv[3], "w"), indent=0)
from collections import Counter; print(Counter(c for _, c, _ in res))
for f, c, d in res:
    if c == "mismatch": print(f.split('/')[-2], d)
