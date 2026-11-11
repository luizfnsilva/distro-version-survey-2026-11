# Debian: tag do upstream × versão declarada (snapshot 2026-11-10, DCS + sources.debian.org)

Pré-registro: PREREGISTRO.md. Números abaixo são **pisos** (nunca taxa; denominador = não medido, universo Debian main não varrido).

## P1 mecanismo: nenhum encontrado
Busca no código das ferramentas (DCS, versões do dia):
- lintian 2.143.0, `lib/Lintian/Check/Debian/Watch.pm` ~436-452: `debian-watch-file-specifies-wrong/old-upstream-version` compara a versão **do debian/watch** com o changelog. Não lê pyproject/setup.py.
- lintian `lib/Lintian/Check/Languages/Python.pm` ~250: só avisa egg-info legado.
- dh-python 7.20261030 (`dhpython/*.py`): `Version` = versão do interpretador Python; `accept_upstream_versions` (depends.py:268) trata dependências. Nenhuma comparação pacote × versão declarada.
- debhelper e uscan: busca por mismatch/compare sem achado (ausência por busca de palavras-chave, não leitura integral).
Conclusão: pacote Debian herda a versão do changelog/watch; o que o código declara não é conferido.

## P2 piso de casos
| Padrão (DCS, perpkg=1) | Pacotes-fonte | Nota |
|---|---|---|
| `SETUPTOOLS_SCM_PRETEND_VERSION` em debian/rules | 135 com ocorrência, 134 não comentada | convenção (classe 2): versão vem do changelog |
| patch em debian/patches com linha `^[-+]version = / version=` (excl. `rust-*`, `golang-*`; 179 patches buscados) | 93 pacotes tocam um manifesto: 67 pyproject/setup.py/setup.cfg, 26 Cargo.toml | inclui linhas de dependência no Cargo; nos Python 31 patches trocam `-versão +versão` |
Limite: DCS pagina com teto; os dois números são piso. Exclusão de rust-/golang- é decisão desta medição (patches de relax-deps inflam).

## P3 amostra (primeiros 20 patches Python com `-`/`+` de versão, ordem alfabética; 19 pacotes)
Evidência = linha `-` do patch (conteúdo do upstream antes do patch; sources.debian.org já entrega a árvore *com* patches, então a linha `-` é o estado upstream). Conferido na tag do GitHub em 4 casos (*).

### (1) Inconsistência observada: o upstream declara outra versão real (7)
| Pacote (versão Debian) | Upstream declara | Arquivo |
|---|---|---|
| caio 0.12.4-1 * | 0.10.2 (tag 0.12.4, pyproject.toml:7) | pyproject.toml |
| django-ldapdb 2.0.0-2 * | 1.5.2.dev0 (tag 2.0.0, setup.cfg:3) | setup.cfg |
| python-cross-web 0.7.0-2 * | 0.6.0 (tag 0.7.0, pyproject.toml:3) | pyproject.toml |
| drslib 0.3.2-3 | 0.3.1p3 | setup.py |
| phat 1.7-2 | 1.6.0.post2 | setup.py |
| python-alpha-vantage 3.0.0-1 | 2.3.1 | setup.py |
| python-batinfo 2.0-1 | 0.2 (patch põe 0.4.2; nenhum bate com 2.0) | setup.py |

### (2) Diferença de convenção legítima, não é defeito (6)
cwiid (versão dinâmica por comando), lookatme (placeholder `{{VERSION}}`), px (versão calculada), pydocstyle (`0.0.0-dev`, placeholder), python-gnuplot (`__version__` importado), apricot-select (só aspas, mesmo valor).

### (3) Os dados não decidem (6)
assimp (setup.py de subpasta pyassimp com versão própria 5.2.5 × pacote 6.0.5), comitup (tag upstream só v1.47; 1.47.1 sem tag), cpuset (`version = version` variável), expeyes (módulo com versão própria 1.0.0), pyjdata (patch diz 0.4.0, tag v0.4.1 declara 0.4.1: orig ≠ tag), python-magic (snapshot git depois de 0.4.27, declara 0.4.28).

Nem (2) nem (3) contam como defeito. Mangling Debian (epoch, +dfsg/+ds, ~) foi normalizado antes de comparar; nenhum caso de (1) depende dele.
Ressalvas: amostra por regra de ordem, não aleatória; ~4 de 7 de (1) sem checagem na tag do GitHub (só no patch).
