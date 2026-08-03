# claude-finance-prompts

The free companion prompt repository for *Claude AI for Finance Professionals*.

Live at <https://tejasgjadhav.github.io/claude-finance-prompts/>

- `index.html` - the page readers land on. Self-contained: no CDN, no external
  fonts, nothing fetched at runtime. Grouped by the 15 desk chapters, every
  prompt shown as its five CRAFT layers, one anchor and one copy button per
  prompt, search across all 122, light and dark, legible at 375px.
- `PROMPTS.md` - the same 122 prompts as plain Markdown. This is the input.
- `build_site.py` - regenerates `index.html` from `PROMPTS.md`.

Prompt numbering is the book's numbering. Prompt 47 here is Prompt 47 there.

## Regenerating

`index.html` is generated. Do not hand-edit it; edit `PROMPTS.md` or
`build_site.py` and rebuild:

    python3 build_site.py

The script asserts 122 prompts across 15 chapters and fails loudly if the
Markdown drifts. The copy button reproduces each prompt byte-for-byte as it
appears in `PROMPTS.md`.

## How it is published

Page 215 of the printed book carries
`https://tejasgjadhav.github.io/claude-finance-prompts`. **That path must stay
exactly `claude-finance-prompts`** or the printed link goes nowhere and cannot be
fixed without a reprint. Renaming this repository breaks the printed link.

This repository is a GitHub Pages project site: repo `claude-finance-prompts`
under user `tejasgjadhav` serves at
`tejasgjadhav.github.io/claude-finance-prompts/`. Pages is set to deploy from
branch `main`, folder `/ (root)`.

To republish:

    python3 build_site.py
    git commit -am "prompt repository: regenerated"
    git push origin main

    # confirm it is live
    curl -sI https://tejasgjadhav.github.io/claude-finance-prompts/ | head -1

The last step must return `HTTP/2 200`. Pages can take a couple of minutes to
rebuild.

### Note on the older route

An earlier copy of this folder lives inside the `tejasgjadhav.github.io` user
Pages repository, which served the same path. This repository supersedes it: for
a given path, a project Pages site takes precedence over a same-named directory
in the user site. The copy in the user Pages repo is now stale and should be
deleted from that repository so there is one source of truth.

## Policy

No email gate, no sign-up form, no review request. A free resource tied to a
review ask is an incentivised review and breaks Amazon policy.
