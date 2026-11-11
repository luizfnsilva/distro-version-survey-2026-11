# Distros: a tag do upstream × a versão que o código declara — pré-registro (10/11/2026)

Escrito antes de medir. Distros: Debian, Arch, Fedora, Gentoo, Homebrew (Nix e Guix já em ../2026-11-10-nix-guix).

P1 (mecanismo): a ferramenta oficial de build da distro compara a versão do pacote com a declarada pelo código/binário? Resposta só com arquivo-fonte e linha citados.
P2 (piso de casos): quantos pacotes reescrevem ou injetam a versão declarada (sed/patch/variável PRETEND_VERSION/override). Contagem por padrão de texto fixado aqui: `SETUPTOOLS_SCM_PRETEND_VERSION`, `sed`/`substituteInPlace`/patch que toca `version` em pyproject.toml, setup.py, setup.cfg, Cargo.toml, package.json. Número = piso, nunca taxa.
P3 (amostra conferida): até 20 casos de P2 por distro, conferidos no upstream na tag fixada; classes: diverge / placeholder / sem versão estática / não deu.
Snapshot e data registrados por distro. Nada de taxa sem denominador explícito.
