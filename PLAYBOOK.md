# Setup playbook — MKLOS + Claude Code on the web

Order matters: the repo must exist and be pushed before Claude Code on the web
has anything to point at. Repo first, environment second, porting last.

## Prereqs (one-time)
Install tools and authenticate with your PERSONAL GitHub identity (this is your
isolation from anything work-related):

    brew install gh git
    gh auth login        # GitHub.com -> HTTPS -> browser -> personal account
    gh auth status

## 1. Land the scaffold locally
    mkdir -p ~/projects && unzip ~/Downloads/mklos-scaffold.zip -d ~/projects && cd ~/projects/mklos

## 2. Create the git repo (init + first commit)
    git init -b main && git add -A && git commit -m "Initial MKLOS commit"

## 3. Publish to GitHub (private) and push
    gh repo create mklos --private --source=. --remote=origin --push
    gh repo view --web

## 4. Connect GitHub to Claude Code on the web
Go to claude.ai/code, connect GitHub, install the Claude GitHub App scoped to
ONLY the `mklos` repo (Select repositories -> mklos). That scoping is your
isolation boundary.

## 5. Create the "mklos" environment
Add an environment: name `mklos`, repo `mklos`, network access Trusted,
no env vars or setup script yet.

## 6. Verify the loop
Start a cloud session on `personal`, enable your Google connectors, and run a
throwaway task (e.g. "add a one-line description to skate-park/CLAUDE.md under
'What this is'"). It edits on a claude/ branch and opens a PR — review, merge,
confirm on main.

## 7. (Optional, deferrable) Protect main
No live website yet and cloud sessions already can't push to main, so this can
wait. When you want the gate:

    echo '{"required_status_checks":null,"enforce_admins":false,"required_pull_request_reviews":{"required_approving_review_count":0},"restrictions":null}' | gh api -X PUT repos/<YOUR-GH-USERNAME>/mklos/branches/main/protection --input -

## 8. Port your projects
Open a session per project, bring content into `skate-park/` and `toby-college/`,
and fill in each project's `CLAUDE.md` "What this is".
