# claude-finance-prompts

A free, public repository of 122 finance prompts.

- `index.html` - the page readers land on. Self-contained: no CDN, no external
  fonts, nothing fetched at runtime. Grouped by desk, one anchor and one copy
  button per prompt, legible at 375px.
- `PROMPTS.md` - the same 122 prompts as plain Markdown.

Both files are generated. Do not hand-edit them. Regenerate with:

    python3 build_site.py ~/files/claude-finance-prompts

Prompt numbering is stable. Prompt 47 stays Prompt 47.

## How it is published

`https://tejasgjadhav.github.io/claude-finance-prompts` is printed in material
already in circulation. **That path must stay exactly `claude-finance-prompts`.**
Change it and the printed link goes nowhere, and it cannot be fixed afterwards.

`~/files` is itself the git repository behind
`github.com/tejasgjadhav/tejasgjadhav.github.io`, the user Pages site. This
directory sits at the root of that repository, so it is served at
`/claude-finance-prompts/` with no second repo and no extra Pages setup. There is
a `.nojekyll` at the repository root, so the folder is copied verbatim.

There is no separate `claude-finance-prompts` GitHub repository and this
directory must not have its own `.git`. If one is created, the parent repository
records it as an empty gitlink and the page 404s.

To republish after regenerating:

    cd ~/files
    git add claude-finance-prompts
    git commit -m "prompt repository: regenerated"
    git push origin main

    curl -sI https://tejasgjadhav.github.io/claude-finance-prompts/ | head -1

The last step must return `HTTP/2 200`. Pages can take a couple of minutes to
rebuild.

## Policy

No email gate, no sign-up form, no review request.
