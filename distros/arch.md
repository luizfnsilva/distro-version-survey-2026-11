# Arch Linux: tag do upstream × versão declarada (snapshot 2026-11-10)

Pré-registro: PREREGISTRO.md. Números = **pisos**, não taxas.

## P1 mecanismo: nenhum encontrado
- makepkg (pacman, `scripts/libmakepkg/lint_pkgbuild/pkgver.sh.in` linhas 40-47): `check_pkgver` só valida sintaxe de pkgver (vazio, `:/-`, espaço, não-ASCII).
- namcap (`Namcap/rules/`, 47 regras listadas pela API do GitLab): nenhuma compara pkgver com versão declarada no código.
- devtools `src/lib/version/check.sh:177`: `pkgctl version check` usa `vercmp upstream_version pkgver`, onde upstream_version vem do nvchecker (último release), **não** do que o código na tag declara.

## P2 piso de casos (extra, PKGBUILDs de gitlab.archlinux.org .../packages/<pkg>/-/raw/main/PKGBUILD)
Denominador: 2090 pkgbases com pkgname `python-*` (API archlinux.org, repos Extra e Extra-Testing deduplicados por pkgbase); 2090 PKGBUILDs baixados, 0 faltando.
| Padrão | Pkgbases |
|---|---|
| `SETUPTOOLS_SCM_PRETEND_VERSION` | 63 (3,0% de 2090) |
| `sed` que reescreve a versão em pyproject/setup/`__init__` | 9: aiocarbon, aiofile, aiohttp-asgi, aiothreads, awesomeversion, awscrt, caio, pydocstyle, pyroute2 |
Linhas de sed que apenas tocam dependências foram excluídas à mão (cvxpy, datasets, configobj, pytorch, teamcity-messages; pylint-pydantic só comentário). A taxa é sobre pacotes `python-*`, não sobre todo o Arch.

## P3 amostra (20: os 9 sed + os 11 primeiros PRETEND em ordem alfabética; upstream na tag = pkgver, raw do GitHub)
### (1) Inconsistência observada: a tag declara outra versão real (5)
| Pacote | Arch | Tag declara | Linha |
|---|---|---|---|
| python-aiocarbon | 0.17.0 | 0.16.0 | pyproject.toml:3 |
| python-aiofile | 3.12.3 | 3.9.0 | pyproject.toml:3 |
| python-aiohttp-asgi | 0.7.1 | 0.6.1 | pyproject.toml:3 |
| python-aiothreads | 1.1.4 | 1.0.0 | pyproject.toml:3 |
| python-caio | 0.12.10 | 0.10.2 | pyproject.toml:7 |
Os 5 são do mesmo autor (mosquito/*): um padrão de manutenção, não 5 observações independentes. (caio também aparece no Debian, 0.12.4 declarando 0.10.2.)

### (2) Convenção legítima, não é defeito (2 conferidos)
python-pydocstyle (`0.0.0-dev` placeholder na tag 6.3.0, pyproject.toml:3); python-automat (`dynamic = ["version"]`, pyproject.toml:12, VCS). Por desenho, awesomeversion (`version = "0"` placeholder no padrão do sed) também cai aqui, sem checagem na tag.

### (3) Os dados não decidem (12)
awscrt, pyroute2 (sed em arquivo de versão, não conferido na tag); aiomysql, ansi2html, anyio, argon2-cffi-bindings, astropy-iers-data, auditwheel, cbor2, cccl, cheroot, cherrypy (PRETEND: repo não localizado automaticamente no PKGBUILD ou sem versão estática achada).
Contar (2) e (3) como defeito seria erro; PRETEND_VERSION em si é convenção setuptools-scm.
Ressalva: amostra por regra de ordem, não aleatória; conferência na tag só via GitHub raw.
