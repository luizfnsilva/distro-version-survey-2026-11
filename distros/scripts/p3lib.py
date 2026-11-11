import re, subprocess, json


def get(u):
    r = subprocess.run(['curl', '-fsS', '--max-time', '30', u], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


PLACE = ('0.0.0', '0', '0.0', '0.1.0.dev0', '0.0.0.dev0', '0.0.0-dev', '0.0.0-development')


def check(repo, v, extra_tags=()):
    """Return dict: tag, declared, cls. Looks at pyproject/setup.cfg/Cargo.toml/package.json at tag."""
    r = {'repo': repo, 'dist_version': v}
    tags = [f'v{v}', v] + list(extra_tags)
    for tag in tags:
        for f in ('pyproject.toml', 'Cargo.toml', 'package.json', 'setup.cfg', 'setup.py'):
            txt = get(f'https://raw.githubusercontent.com/{repo}/{tag}/{f}')
            if txt:
                r['tag'] = tag; r['file'] = f
                break
        if 'tag' in r:
            break
    if 'tag' not in r:
        r['cls'] = 'nao deu'
        return r
    f = r['file']
    if f == 'package.json':
        m = re.search(r'"version"\s*:\s*"([^"]+)"', txt)
    else:
        m = re.search(r'^\s*version\s*[=:]\s*["\']?([^"\'\s,]+)', txt, re.M)
        if f == 'setup.py' and not m:
            m = re.search(r'version\s*=\s*["\']([^"\']+)', txt)
    dyn = ('setuptools_scm' in txt or 'hatch-vcs' in txt or 'vcs' in txt.lower()
           or re.search(r'dynamic\s*=\s*\[[^\]]*version', txt))
    if m:
        d = m.group(1)
        r['declared'] = d
        if d in PLACE:
            r['cls'] = 'placeholder'
        elif d == v or d == v.lstrip('v'):
            r['cls'] = 'confere'
        else:
            r['cls'] = 'diverge?'
    else:
        r['cls'] = 'sem versao estatica' if dyn else 'nao deu'
    return r
