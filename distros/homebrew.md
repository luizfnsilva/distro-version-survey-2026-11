# Homebrew (snapshot 2026-11-10)
homebrew-core 2cb5a12, brew 95d4938. Denominador: 8723 fórmulas (Formula/*/*.rb).

## P1
O `brew audit` não compara a versão do artefato com a da fórmula. Existe só convenção: o bloco `test do` (todas as 8723 têm) pode conter `assert_match version`. Contagem:
- `assert_match` com `version`/`#{version}` em qualquer posição: 2447/8723 (28,1%); forma estrita `assert_match version`/`#{version}`: 1998/8723 (22,9%).
- audit/rubocops de brew: nenhuma regra que exija ou cheque esse assert (`rubocops/lines.rb` só regra de estilo de assert; formula_auditor.rb:1002 usa a versão só para achar release no GitHub/GitLab).
Observação: o assert mede a saída do binário, não o metadado de pacote.

## P2 (piso)
6/8723 com SETUPTOOLS_SCM_PRETEND_VERSION ou inreplace de version: theharvester, fdroidserver, otterdog, ctcache, charmcraft, pytr (lista homebrew-p2.txt). Vários injetam a versão de um resource, não do pacote principal.

## P3 (5 dos 6; fdroidserver está no GitLab, não conferido)
| pacote | versão da distro | declarada no tag | classe |
|---|---|---|---|
| theharvester | 4.11.1 | - | sem versao estatica |
| ctcache | 1.2.0 | - | sem versao estatica |
| charmcraft | 4.5.0 | - | sem versao estatica |
| pytr | 1.62.0 | - | nao deu |
| otterdog | 1.7.1 | 0.0.0 | placeholder |

## Classificação (regra do dono)
1. Inconsistência observada (tag declara versão real diferente): **0 casos confirmados.**
2. Convenção legítima (não é defeito): 3 sem versão estática (VCS); otterdog declara 0.0.0 no tag = placeholder preenchido na publicação
3. Indecidível com estes dados (não conta): pytr (tag não achado); fdroidserver (GitLab, não conferido)

Resultado: n pequeno (6); só mostra que o uso existe, sem inferência.
