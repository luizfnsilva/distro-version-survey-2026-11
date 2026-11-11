# Gentoo (snapshot 2026-11-10)
gentoo/gentoo depth 1 @ 03b412ed6. Denominador: 33613 ebuilds.

## P1
`distutils-r1.eclass` (e python-utils-r1) não verifica versão de wheel/METADATA contra PV: grep por METADATA/Version/PRETEND/PV no eclass sem ocorrência relevante; só linha 144 (comentário sobre PEP 621) e 1019 (`HATCH_METADATA_CLASSIFIERS_NO_VERIFY`, não é versão). Não há checagem.

## P2 (piso)
- ebuilds com `*_PRETEND_VERSION`: 114/33613 (SETUPTOOLS_SCM_PRETEND_VERSION: 110). Padrão dominante: `export SETUPTOOLS_SCM_PRETEND_VERSION=${PV}` (~100); há `${PV/_}` (3) -- mangling Gentoo deliberado.
- sed sobre version nos arquivos-alvo: 9/33613.
Listas: gentoo-p2-*.txt.

## P3 (20 casos; só PV sem `_` e não 9999; pulados: 1 mangled, 5 sem GitHub)
| pacote | versão da distro | declarada no tag | classe |
|---|---|---|---|
| x11-terms/guake/guake-3.10.ebuild | 3.10 | - | nao deu |
| dev-python/pdm-backend/pdm-backend-2.4.10.ebuild | 2.4.10 | - | sem versao estatica |
| dev-python/astroid/astroid-4.3.1.ebuild | 4.3.1 | - | sem versao estatica |
| dev-python/docker/docker-7.2.0.ebuild | 7.2.0 | - | sem versao estatica |
| dev-python/pytest-services/pytest-services-2.2.2.ebuild | 2.2.2 | - | sem versao estatica |
| dev-python/configupdater/configupdater-3.2.ebuild | 3.2 | - | sem versao estatica |
| media-sound/whipper/whipper-0.10.0-r4.ebuild | 0.10.0 | - | sem versao estatica |
| dev-util/unicorn/unicorn-2.1.3-r1.ebuild | 2.1.3 | 2.1.3 | confere |
| dev-db/mycli/mycli-2.30.0.ebuild | 2.30.0 | - | sem versao estatica |
| dev-python/astroid/astroid-4.3.3.ebuild | 4.3.3 | - | sem versao estatica |
| dev-python/tabulate/tabulate-0.10.0.ebuild | 0.10.0 | - | sem versao estatica |
| dev-python/executing/executing-2.2.1.ebuild | 2.2.1 | - | sem versao estatica |
| games-util/sc-controller/sc-controller-1.0.5.ebuild | 1.0.5 | - | sem versao estatica |
| mail-client/alot/alot-0.11-r2.ebuild | 0.11 | - | sem versao estatica |
| dev-python/astroid/astroid-4.0.4.ebuild | 4.0.4 | { | diverge? |
| dev-python/jsondiff/jsondiff-2.2.1.ebuild | 2.2.1 | - | sem versao estatica |
| dev-python/kiwisolver/kiwisolver-1.5.0.ebuild | 1.5.0 | - | sem versao estatica |
| dev-python/xmlsec/xmlsec-1.3.18.ebuild | 1.3.18 | - | sem versao estatica |
| x11-terms/guake/guake-3.10.1.ebuild | 3.10.1 | - | nao deu |
| dev-python/cvxopt/cvxopt-1.3.3.ebuild | 1.3.3 | - | sem versao estatica |

## Classificação (regra do dono)
1. Inconsistência observada (tag declara versão real diferente): **0 casos confirmados.**
2. Convenção legítima (não é defeito): 17 sem versão estática (versão via VCS/SCM: o ebuild injeta ${PV}, que é o propósito); 1 confere (unicorn). Mangling `_pre/_p/_rc`, `-rN` excluídos antes de medir -- não são divergência
3. Indecidível com estes dados (não conta): guake (2), tag/arquivo não encontrado; astroid-4.0.4 `declared={` é artefato do regex, não versão

Sem nenhum caso de divergência real; nada aqui sustenta 'defeito' no Gentoo.
