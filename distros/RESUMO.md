# Resumo (10/11/2026) — pré-registro 561a375

| Distro | Compara versão declarada? | Piso P2 | (1) inconsistência | (2) convenção | (3) inconclusivo |
|---|---|---|---|---|---|
| Nix | sim: pythonMetadataCheckHook (padrão), versionCheckHook (2.337) | 195 patch-hook + 27 PRETEND + 19 substitute | 51 | 85 | 59 |
| Guix | não | — | — | — | — |
| Debian | não (lintian compara watch × changelog) | 134 PRETEND, 93 patches em manifesto | 7 de 19 | 6 | 6 |
| Arch | não (devtools compara com nvchecker) | 63 PRETEND + 9 sed / 2.090 | 5 de 20 (um só autor) | 3 | 12 |
| Fedora | não (só trava versão zero) | 61 PRETEND + 28 sed / 1.774 | 0 de 20 | 17 | 3 |
| Gentoo | não | 114 PRETEND + 9 sed / 33.613 | 0 de 20 | 17 | 2 |
| Homebrew | não no audit; assert_match version em 2.447/8.723 | 6 | 0 de 5 | 4 | 1 |

Mesmo upstream corrigido em mais de uma distro: caio (Debian, Arch), cross-web (Nix, Debian), aiothreads (Nix, Arch).
Amostras de Debian/Arch em ordem fixa, não sorteadas. Números são pisos, não taxas.
Nix: o 69 enviado ao Chris contava 0.1.0/1.0.0 como inconsistência; estrito = 51.
