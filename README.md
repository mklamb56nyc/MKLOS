# personal (superrepo)

Personal monorepo for use with **Claude Code on the web**. One source of truth,
edited in place by Claude, tracked in git.

## Layout
- `skate-park/` — personal project (own `CLAUDE.md`)
- `toby-college/` — personal project (own `CLAUDE.md`)
- `CLAUDE.md` — standing instructions for Claude across the repo
- `.mcp.json` — MCP servers for sessions in this repo
- `.claude/settings.json` — Claude Code settings

Coming later: `site/` — the public website, deployed by Cloudflare.

## Push it
    git init && git add -A && git commit -m "Initial personal superrepo"
    gh repo create personal --private --source=. --remote=origin --push

Then at claude.ai/code: connect this GitHub repo (scoped GitHub App on just this
repo), add an environment named "personal" on Trusted networking, and enable your
Google connectors per session.

## The Sheets MCP (`.mcp.json`)
Replace the placeholder URL with your Cloudflare Worker's MCP endpoint, or delete
that entry and register the server as a custom connector in claude.ai. Until then
sessions list it as unavailable — harmless.
