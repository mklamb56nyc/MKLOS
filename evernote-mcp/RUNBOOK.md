# Runbook: Evernote MCP in Claude Code on the Web

**Goal:** Every cloud session starts with Evernote tools live. Server runs inside the
Anthropic sandbox (stdio). No self-hosted infra. Egress constrained by the environment's
network allowlist.

**Audited version:** `@verygoodplugins/mcp-evernote@1.2.3` (audit of published npm
tarball: no unauthorized egress; webhook is opt-in via `WEBHOOK_URL` — leave unset).
Do not bump the version without re-auditing. Verified 2026-07-24: `dist/oauth.js` reads
`EVERNOTE_ACCESS_TOKEN` + `EVERNOTE_NOTESTORE_URL` directly from env — the running
server never needs an API consumer key; only the OAuth *minting* flow does. Any valid
access token works, however obtained.

---

## STATUS — 2026-07-24

| Phase | State |
|---|---|
| 1 — Get a token | **BLOCKED** — no consumer key; see revised Phase 1 routes below |
| 2 — Repo `.mcp.json` | **DONE** (PR #112, merged 2026-07-24) |
| 3 — Environment config | Pending a token |
| 4 — Verification | Pending Phase 3 |

**What changed:** the original Phase 1 assumed `mcp-evernote-auth` goes straight to a
browser sign-in. Wrong — reading the 1.2.3 source (`dist/auth-standalone.js`), the flow
is: (1) demand an Evernote **API Consumer Key + Secret**, (2) only then browser OAuth,
(3) write `.evernote-token.json`. There is **no keyless path and no cookie fallback**
in this version (the original runbook's cookie warning doesn't match the shipped code).
Evernote stopped self-serve key issuance years ago; the classic EDAM API this package
uses is officially deprecated. Mike holds no key. So: three routes, in order.

---

## Phase 1 (revised) — Get a token

### Route A — Developer token (try first; 60 seconds, no tooling)

Evernote developer tokens are personal full-access API tokens: exactly the two values
Phase 3 needs, no OAuth, no consumer key, no local Node.

1. Log in to evernote.com in a browser.
2. Visit **https://www.evernote.com/api/DeveloperToken.action**
3. If offered, create the token. Copy **both** the token (`S=s###:...`) → use as
   `EVERNOTE_ACCESS_TOKEN`, and the **NoteStore URL** shown → `EVERNOTE_NOTESTORE_URL`.
4. Go straight to Phase 3.

Caveats: the docs say developer tokens are "currently unavailable except for proven
necessity" — the page may refuse to issue one. It's account-dependent; just look.
A developer token is a full-account credential (same risk class as the OAuth token this
runbook already planned to store — the existing env-var handling rules cover it).
Revoke any time at the same URL.

### Route B — OAuth flow (requires an API key Evernote must grant)

1. **Request a key** via developer support (dev.evernote.com → Support → API key
   request; the FAQ documents the process). Manual review, up to ~5 business days,
   notified by email. **Request FULL access** — Basic keys cannot read existing notes
   (`findNotes`/`getNote` → `PERMISSION_DENIED`), which the MCP needs.

   Paste-ready form answers:
   - **Full name:** Michael Lamb
   - **Organization:** Received Wisdom LLC (single-member personal use)
   - **Application name:** Personal notes assistant (MCP)
   - **Access level:** Full — the assistant must search and read existing notes
     (`findNotes`, `getNote`), which Basic keys cannot do.
   - **Environment:** production (personal account; not building for third parties)
   - **Description:**
     > Single-user personal integration connecting my own Evernote account to my
     > personal AI assistant (Anthropic's Claude) via the open-source Model Context
     > Protocol server @verygoodplugins/mcp-evernote, which uses the Evernote Cloud
     > API with OAuth 1.0a. The integration searches and reads my existing notes and
     > notebooks and occasionally creates or updates notes, on my own account only.
     > No other users, no data collection, no redistribution.
2. **When the key arrives**, run the auth helper on any local machine. No-UAC
   PowerShell path (portable Node, nothing installed, delete after — update the pinned
   Node version if stale):

   ```powershell
   cd $env:USERPROFILE\Downloads
   Invoke-WebRequest https://nodejs.org/dist/v22.23.1/node-v22.23.1-win-x64.zip -OutFile node.zip -UseBasicParsing
   Expand-Archive node.zip -DestinationPath .
   cd node-v22.23.1-win-x64
   $env:Path = "$pwd;$env:Path"
   $env:EVERNOTE_CONSUMER_KEY = "<key>"
   $env:EVERNOTE_CONSUMER_SECRET = "<secret>"
   .\npx.cmd -y -p "@verygoodplugins/mcp-evernote@1.2.3" mcp-evernote-auth
   ```

   Setting the env vars first skips the interactive credential prompt (the script
   checks env before prompting). Browser opens → authorize → token written to
   `.evernote-token.json` in the current folder. Capture `token` →
   `EVERNOTE_ACCESS_TOKEN` and `noteStoreUrl` → `EVERNOTE_NOTESTORE_URL`, then:

   ```powershell
   Remove-Item -Force .evernote-token.json
   cd .. ; Remove-Item -Recurse -Force node-v22.23.1-win-x64, node.zip
   ```

3. **Known trap (hit 2026-07-24):** the helper can exit **instantly and silently** —
   no banner, no error. The script is healthy (verified chatty in a clean Linux env);
   the silent kill is machine-side, almost certainly antivirus terminating node in the
   npx cache (`npm warn cleanup EPERM` lines in the same run are the tell). If it
   happens: check `$LASTEXITCODE`, add a Defender/AV exclusion for the throwaway Node
   folder and `%LOCALAPPDATA%\npm-cache`, retry.

### Route C — ENEX fallback (no API at all)

If no token is obtainable (or sooner access is wanted): Evernote app → per notebook →
Export → `.enex`. Drop files in Drive or upload to a session; Claude parses ENEX XML
directly and the content can live/be processed in MKLOS. Snapshot, not live access —
re-export to refresh.

---

## Phase 2 — Repo changes — DONE

`.mcp.json` at repo root registers the server (alongside `google-sheets`):

```json
"evernote": { "type": "stdio", "command": "mcp-evernote" }
```

No token literal in the file — it's committed. The bare `mcp-evernote` command works
because Phase 3's setup script installs the package globally into the cached image.
Until Phase 3 is done, sessions show `evernote` as failed-to-connect; harmless.

---

## Phase 3 — Cloud environment config (claude.ai/code)

Environment selector (cloud icon) → hover environment → settings. Use a **personal**
environment, not org-shared (env vars are visible to anyone who can edit the
environment; there is no secrets store yet).

1. **Network access:** Custom. Allowed domains: `*.evernote.com`. Check **"Also include
   default list of common package managers"** (required — otherwise npm install fails).
2. **Environment variables** (no quotes; do NOT set `WEBHOOK_URL` — keeps the server's
   only non-Evernote egress path disabled):

   ```
   EVERNOTE_ACCESS_TOKEN=<from Phase 1, any route>
   EVERNOTE_NOTESTORE_URL=<from Phase 1, any route>
   ```

3. **Setup script:** `npm install -g @verygoodplugins/mcp-evernote@1.2.3 || true`

Save. Changing setup script or allowed hosts triggers a cache rebuild on next session
start; after the first successful run the install is snapshotted.

---

## Phase 4 — Verification (first cloud session after Phase 3)

1. `/mcp` → expect `evernote` connected (first session slower; approve the
   project-scoped server if prompted).
2. `which mcp-evernote && echo ${EVERNOTE_ACCESS_TOKEN:0:6}... && echo $WEBHOOK_URL`
   → path, token prefix, empty last line.
3. Prompt: "Use the evernote server to list my notebooks." → notebook list.
4. Negative egress test: `curl -sI --max-time 5 https://example.com | head -1` →
   blocked, while Evernote tools work.

---

## Phase 5 — Standing rules & maintenance

- **Never share sessions** from this environment (sessions will contain note content).
- **Token rotation:** OAuth tokens expire ~1 year; developer tokens per their page. On
  auth errors, re-run Phase 1 (whichever route) and update the Phase 3.2 env vars.
- **Version bumps:** re-audit the new tarball before changing the pinned version
  (`npm pack`, inspect `dist/` for new egress paths, re-check `WEBHOOK_URL` gating).
- **Revocation:** revoke the token (Evernote settings → Applications, or the
  DeveloperToken page for Route A) and delete the env vars.
- **Cache expiry:** environment snapshot rebuilds ~every 7 days automatically.

## Rollback

Remove the `evernote` block from `.mcp.json` (keep `google-sheets`), commit, push.
Then delete the two env vars, remove `*.evernote.com` from allowed domains, and revoke
the token in Evernote.

## Log

- **2026-07-24** — Phase 2 shipped (PR #112). Phase 1 attempted on Windows PC
  (PowerShell, portable Node — no-UAC path added after winget/UAC failure; PS 5.1
  JSON-parse gotcha broke dynamic version lookup, version now pinned literal). Auth
  helper exited silently → diagnosed as AV kill, then found the deeper blocker: 1.2.3
  requires a consumer key before any browser step; no key held; EDAM API deprecated,
  keys by manual request only. Runbook restructured into Routes A/B/C. Next action:
  Mike tries Route A (developer token page), else files Route B key request.
- **2026-07-24 (later)** — Route A page reached while logged in: banner reads
  "developer tokens are only supported for specific cases"; "Create a developer token"
  button present but appears disabled. Clicking confirmed it non-functional —
  **Route A is closed for this account.** Next action: file the Route B key request
  (form answers above); check-in scheduled for 2026-07-31 to confirm whether the key
  email arrived. Interim option if notes are needed sooner: Route C (ENEX).
