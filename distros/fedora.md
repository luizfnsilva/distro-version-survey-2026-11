# Fedora (snapshot 2026-11-10)
Commits: pyproject-rpm-macros 707827f, python-rpm-generators 0b2eb91 (2026-10-15), rpmlint-up f58c4f5 (2026-10-16).

## P1
Não há checagem de Version do RPM contra a versão do dist-info. Único controle: versão zero.
`python-rpm-generators/pythondistdeps.py:482-495` (`--fail-if-zero`, `RpmVersion(version).is_zero()`, exit 65; a mensagem manda usar SETUPTOOLS_SCM_PRETEND_VERSION). pyproject-rpm-macros e rpmlint (PythonCheck.py) não comparam versão (grep sem ocorrência).

## P2 (piso, não taxa)
Denominador: amostra aleatória (seed 20261110) de 3000 nomes `python-*` do dist-git (4721 únicos listados de ~13247 entradas paginadas, listagem instável); 1774 specs rawhide baixados (1226 deram 404: aposentados/sem spec).
- `SETUPTOOLS_SCM_PRETEND_VERSION`: 61/1774 specs.
- sed sobre version em pyproject/setup.py/setup.cfg/Cargo.toml/package.json: 28/1774 (regex fixada; sobreposição entre listas não calculada).
Listas: fedora-p2-*.txt.

## P3 (20 casos, tag v<Version> ou <Version> no GitHub)
| pacote | versão da distro | declarada no tag | classe |
|---|---|---|---|
| python-sphinx-argparse-cli.spec | 1.21.3 | - | sem versao estatica |
| python-can.spec | 4.6.1 | - | sem versao estatica |
| python-scooby.spec | 0.12.1 | - | sem versao estatica |
| python-packvers.spec | 21.5 | - | nao deu |
| python-pytest-regressions.spec | 2.11.0 | - | sem versao estatica |
| python-executing.spec | 2.2.1 | - | sem versao estatica |
| python-quantities.spec | 0.16.4 | - | sem versao estatica |
| python-discovery.spec | 1.9.4 | - | sem versao estatica |
| python-pipdeptree.spec | 3.1.1 | - | sem versao estatica |
| python-eth-tester.spec | 0.14.0 | - | nao deu |
| python-conda-index.spec | 0.13.0 | - | sem versao estatica |
| python-huggingface-hub.spec | 2.3.0 | - | nao deu |
| python-pytest-repeat.spec | 0.9.3 | - | sem versao estatica |
| python-zstd.spec | 1.5.7.3 | PKG_VERSION_STR | diverge? |
| python-jira.spec | 3.10.5 | - | sem versao estatica |
| python-pytest-github-actions-annotate-failures.spec | 0.4.2 | - | sem versao estatica |
| python-extractcode.spec | 31.0.0 | - | sem versao estatica |
| python-iniconfig.spec | 2.3.0 | - | sem versao estatica |
| python-rx.spec | 6.1.0 | 6.1.0 | confere |
| python-mkdocs-rss-plugin.spec | 1.17.7 | - | sem versao estatica |

## Classificação (regra do dono)
1. Inconsistência observada (tag declara versão real diferente): **0 casos confirmados.**
2. Convenção legítima (não é defeito): 17 sem versão estática (dinâmica/VCS: setuptools_scm etc.) -- PRETEND_VERSION é o uso previsto; 1 confere (python-rx)
3. Indecidível com estes dados (não conta): python-packvers, python-eth-tester, python-huggingface-hub (tag/arquivo não encontrado); python-zstd (`PKG_VERSION_STR` = artefato do regex, não versão)

Amostra de 20 não é aleatória em toda a população de P2: embaralhada com seed 1.
