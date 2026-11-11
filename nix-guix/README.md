# Nix e Guix: tag × versão declarada (10/11/2026)

Base da resposta ao Chris Lamb na rb-general (fio "Tags that name a version their commit does not declare").

- Snapshots: nixpkgs `a44c64d553e6`, guix `22cea881feab` (clone raso de 10/11).
- `pvph.txt`: os 195 arquivos do nixpkgs que usam `pyprojectVersionPatchHook`.
- `classify.py`: lê owner/repo/tag de cada um e baixa o `pyproject.toml` na tag do GitHub.
  Uso: `python3 -I classify.py <nixpkgs> pvph.txt saida.json`
- `pvph-classes.json`: resultado (arquivo, classe, [versão nix, tag, versão declarada]).

Resultado: 69 tags declaram outra versão real (4 à frente da tag), 78 placeholder, 24 sem versão estática, 24 fora (commit, VCS, não-GitHub, falha).
Guix: só injeta versão para backends VCS; não compara.
