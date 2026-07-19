# MKLOS — working context for Claude

This is MKLOS, the single repo for my personal projects and knowledge. Files here are
edited **in place** by Claude Code and version-controlled — this replaces the old
"download, re-upload, new chat" loop. When I ask you to update something, change
the file directly and let git track it.

## Layout
Each project lives in its own top-level directory with its own `CLAUDE.md`:
- `skate-park/`
- `toby-college/`

(The public website will be added later as `site/`, deployed by Cloudflare — not
set up yet.)

## How to work here
- **Read the project's `CLAUDE.md` first** and keep changes scoped to that
  project's directory.
- **Edit files in place.** Don't produce a "new version" to paste — make the
  change and show me the diff.
- **Batch edits; review the aggregate once.** Work through changes interactively
  across as many edits as it takes — don't stop to commit after each small change or
  force one-logical-change-per-commit. Let edits accumulate, then I review the whole
  aggregate diff in one pass and confirm before anything is committed.
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
Handle git automatically — but commit on my confirmation, not after every task.
- Let edits accumulate across the session. When I've reviewed the aggregate diff
  and confirmed, stage everything, commit with a clear message, push the working
  branch, and open or update a single PR for that branch. Don't auto-commit each
  task's changes before I've had that single review.
- Keep **one `claude/<topic>` branch and one PR per topic** — reuse them across
  edits rather than opening a new PR for each change.
- Leave merging to me. **Never push to `main`.**
- **Succeed silently.** When the git steps work, don't narrate them — no recap of
  the commit, push, branch, or PR mechanics, and no "opened PR #N" outcome. Assume
  success. Just do the actual work and report *that*. Only surface git when
  something fails.
- If a push fails, report the exact error instead of retrying.

## Automation
How git automation works here, for future sessions:
- **Workflow policy (above):** commit, push a `claude/` branch, open/update one
  PR per topic, never push to `main`.
- **Auto-merge:** `.github/workflows/auto-merge-claude.yml` auto-merges `claude/*`
  PRs by squash-and-delete, so most PRs land without manual action.
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
