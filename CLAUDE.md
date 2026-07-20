# MKLOS — working context for Claude

This is MKLOS, the single repo for my personal projects and knowledge. Files here are
edited **in place** by Claude Code and version-controlled — this replaces the old
"download, re-upload, new chat" loop. When I ask you to update something, change
the file directly and let git track it.

## Layout
Each project lives in its own top-level directory with its own `CLAUDE.md`:
- `skate-park/`
- `toby-college/`
- `driggs/` — due diligence on a Crossed Arrows Lot 3 land purchase, Tetonia, Idaho

(The public website will be added later as `site/`, deployed by Cloudflare — not
set up yet.)

## How to work here
- **Read the project's `CLAUDE.md` first** and keep changes scoped to that
  project's directory.
- **Edit files in place.** Don't produce a "new version" to paste — make the
  change and show me the diff.
- **Don't make me manage git.** Edit as freely as the work needs — don't fret commit
  boundaries and never pause for my review or confirmation. Git is handled
  automatically and invisibly (see Git workflow).
- **The files are the record.** Don't restate large blocks in chat when a diff
  will do.
- **Don't invent facts.** If a detail isn't in the repo, in a connected source,
  or given by me, say so rather than guessing.
- **Preserve history.** When a fact changes, update it and note what it replaced
  if the prior value still matters.

## Working style
- Be concise and direct. Lead with the answer or the change; skip preamble.
- When you give shell commands, give single-line copyable commands.
- Flag risks and tradeoffs honestly rather than just agreeing.

## Git workflow
I never want to think or worry about git here — handle it fully automatically.
- Commit and push the working `claude/<topic>` branch automatically at natural
  stopping points. Never wait for my confirmation, and group edits into commits
  however's convenient — don't force one-change-per-commit.
- Keep **one `claude/<topic>` branch *name* per topic**, but treat a merged branch as
  finished. Because `claude/*` PRs auto-merge (squash) and the branch is then deleted,
  reusing it stacks already-merged history and creates a merge conflict. So **before each
  new chunk of work, re-cut the branch from the latest main**:
  `git fetch origin main && git checkout -B claude/<topic> origin/main`. Never add commits
  to a branch whose PR already merged. Expect several short-lived PRs per topic, not one
  long-lived one.
- Leave merging to me. **Never push to `main`.**
- **Succeed silently — but verify the merge landed.** When the git steps work, don't
  narrate them — no recap of the commit, push, branch, or PR mechanics, and no "opened
  PR #N" outcome. Just do the actual work and report *that*. Only surface git when
  something fails. **The one check to always run: after pushing work you expect to
  auto-merge, confirm it actually merged — a PR stuck at `mergeable_state: dirty` (a
  conflict) fails silently. If you find one, re-cut the branch from main, re-apply, and
  `git push --force-with-lease`, then say so.**
- If a push fails, report the exact error instead of retrying.

## Automation
How git automation works here, for future sessions:
- **Workflow policy (above):** commit, push a `claude/` branch, open a PR, never push
  to `main`. Re-cut the branch from main before each new chunk (merged branches are
  finished — see Git workflow).
- **Auto-merge:** `.github/workflows/auto-merge-claude.yml` auto-merges `claude/*`
  PRs by squash-and-delete, so most PRs land without manual action.
- **Squash-merge caveat (learned the hard way):** squash creates a new commit on main,
  so a *reused* branch never sees its old commits as merged and will eventually conflict.
  Always re-cut `claude/<topic>` from the latest main before new work. If a base does go
  stale, the workflow now labels the PR `automerge-blocked` and comments how to fix it
  instead of failing silently in the Actions log — rebase and force-push to clear it.
- **Exception:** PRs that touch `site/` are **not** auto-merged — they stay open
  for human review, because `site/` is the public website Cloudflare deploys and
  production changes must be reviewed.
- **Do not remove the `site/` guard** in that workflow — it's the safety gate
  that keeps production changes from merging unreviewed.

## Google connectors
When enabled on a session, you can use my personal Google connectors:
- **Drive** — read reference docs and pull source data. Read-only.
- **Gmail** — search and draft; you can create drafts, you cannot send. Never
  assume a draft was sent.
- **Calendar** — read, and when I ask, create or update events.

Only the connectors I've toggled on for a session are available. If something you
need isn't connected, tell me and I'll enable it.

## Google Sheets workflow
When a project has a spreadsheet meant for collaborators:
- Keep the working source inside the project directory so you can edit it in place.
- Push changes to the live Google Sheet through the `google-sheets` MCP in
  `.mcp.json` so collaborators always see the current version.
- When the MCP isn't available, update the source file here and I'll import or
  convert manually.

## Guardrails
- **Never commit secrets.** Cloud environments have no secrets store, and env
  vars / setup scripts are visible to anyone who can edit the environment. Keep
  tokens out of the repo; MCP servers authenticate themselves (OAuth).
- **This repo is personal** — deliberately separate from any employer systems,
  repos, or connectors. Keep it that way.
- **Ask before anything destructive** (deleting files, rewriting history, bulk
  changes).
