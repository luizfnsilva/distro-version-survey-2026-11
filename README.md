# A tag whose code declares another version: seven distributions (2026-11-10)

How Nix, Guix, Debian, Arch, Fedora, Gentoo and Homebrew handle an upstream tag whose source declares
a different version. Questions and inclusion rules were written before measuring
(`distros/PREREGISTRO.md`). Per-distribution reports are in Portuguese; numbers are floors, not rates.

| Distribution | Compares the declared version? | Observed inconsistency | Convention | Undecidable |
|---|---|---|---|---|
| Nix | yes: `pythonMetadataCheckHook` (default for Python modules), `versionCheckHook` | 22 of 195 (see below) | 114 | 59 |
| Guix | no | — | — | — |
| Debian | no (lintian compares debian/watch with the changelog) | 7 of 19 | 6 | 6 |
| Arch | no (devtools compares pkgver with nvchecker) | 5 of 20, one author | 3 | 12 |
| Fedora | no (only a zero-version guard) | 0 of 20 | 17 | 3 |
| Gentoo | no | 0 of 20 | 17 | 2 |
| Homebrew | not in `brew audit`; optional `assert_match version` in 2,447 of 8,723 formulae | 0 of 5 | 4 | 1 |

**Nix.** The 195 are the packages using `pyprojectVersionPatchHook`, which refuses to run when the
versions already agree. At the pinned GitHub tag, 51 declare a different real version. 29 of those
have a publish job that writes the version from the tag (`uv version "${GITHUB_REF_NAME#v}"` and
similar): the file at the tag is stale on purpose and the published package is right, so they count
as convention. 22 remain, found by text search of the workflows: confirm each by hand
(`nix-guix/estritos-mecanismo.json`).

**Samples.** Debian and Arch samples are in a fixed order (alphabetical), not random draws.

## Reproduce

Snapshots: nixpkgs `a44c64d553e6`, guix `22cea881feab` (shallow clones of 2026-11-10); Debian Code
Search, gitlab.archlinux.org, src.fedoraproject.org, gentoo/gentoo and homebrew-core on the same day.

- Nix: `python3 -I nix-guix/classify.py <nixpkgs> nix-guix/pvph.txt out.json`
- Others: `distros/scripts/`, raw data next to each report.

An independent reproduction is welcome; differences are most useful as an issue on this repository.
