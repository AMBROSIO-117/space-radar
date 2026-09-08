# Git and GitHub: Commit, Push, Fetch, Pull, and Review

Git is the local version-control system. GitHub is one possible server for sharing Git history and reviewing proposed changes. A commit can exist locally without GitHub, and a GitHub pull request is not the same operation as `git pull`.

## Mental model

```text
working tree -> staging area -> local commit history -> remote repository
   edit          git add          git commit             git push

remote repository -> remote-tracking reference -> local branch -> working tree
                     git fetch       merge/rebase          checkout
```

- **Working tree:** files currently visible in the folder.
- **Staging area/index:** the exact next snapshot selected with `git add`.
- **Commit:** an immutable snapshot plus author, time, parent commit, and message.
- **Branch:** a movable name pointing at one commit; it is not a duplicate folder.
- **Remote:** a saved name such as `origin` for another Git repository URL.
- **Remote-tracking branch:** your last fetched view, such as `origin/main`.
- **Pull request:** a GitHub collaboration record asking to merge one branch into another.

Git stores content-addressed objects. A commit points to a tree (the project snapshot), parent commit(s), and metadata. The branch name advances to the new commit. This is why commits are cheap and why an old state remains recoverable as long as it is still referenced or retained.

## 1. Inspect before changing anything

```bash
git status --short --branch
git remote -v
git log --oneline --decorate --graph -10
```

`git status` answers “where am I and what is uncommitted?” `git remote -v` answers “where could I fetch/push?” At the 2026-09-08 audit this repository had no configured remote, so push and pull required adding one first.

## 2. Initialize Git (only for a folder that is not already a repository)

```bash
git init
git status
```

## 3. Select a change for the next commit

```bash
git diff
git add path/to/file
git diff --cached
git status
```

Prefer adding named files over `git add .`. The first diff shows unstaged changes; `git diff --cached` shows the precise snapshot that the next commit will contain.

## 4. Commit locally

```bash
git commit -m "Initial Space Procurement Signal Radar hackathon project"
```

A commit does not upload anything. It creates a local, reviewable checkpoint. Use one purpose per commit and a message explaining that purpose.

## 5. Create a GitHub repository and connect the remote

Option A: use GitHub website.

Create a repo named:

```text
space-procurement-signal-radar
```

Then:

```bash
git remote add origin https://github.com/YOUR_USERNAME/space-procurement-signal-radar.git
git branch -M main
git push -u origin main
```

`git remote add origin ...` saves the URL. `git push -u origin main` sends commits reachable from local `main` to the remote and records `origin/main` as its upstream. Later, plain `git push` knows the destination.

Option B: use GitHub CLI if authenticated.

```bash
gh repo create space-procurement-signal-radar --public --source=. --remote=origin --push
```

## Push versus fetch versus pull

| Command | Direction | What it does | Main risk |
| --- | --- | --- | --- |
| `git push` | local -> remote | Publishes local commits and advances a remote branch if allowed | Publishing secrets or unwanted commits |
| `git fetch origin` | remote -> local metadata/objects | Downloads commits and refreshes `origin/*`; does not alter working files | Very low; it may reveal divergence |
| `git pull --ff-only` | remote -> current branch | Fetches, then advances only when no merge is required | Stops on divergence, intentionally |
| `git pull --rebase` | remote -> current branch | Fetches, then replays local commits on the updated upstream | Rewrites local commit IDs; conflicts need care |
| `git merge origin/main` | remote-tracking branch -> current branch | Combines histories, possibly with a merge commit | Conflict resolution can be incorrect |

“Pull” is a convenience command: **fetch plus integration**. For learning and diagnosis, use explicit steps:

```bash
git status --short --branch
git fetch origin
git log --oneline --left-right --graph HEAD...origin/main
git merge --ff-only origin/main
```

If both sides have new commits, stop and choose deliberately between merge and rebase. Do not force-push a shared branch without agreement.

## Typical feature-to-pull-request workflow

```bash
git switch main
git pull --ff-only
git switch -c concise-feature-name

# edit and test
git diff
git add path/to/changed-file
git diff --cached
git commit -m "docs: explain the analyst workflow"

git push -u origin concise-feature-name
```

Then open a pull request from `concise-feature-name` into `main`. Review the actual diff, tests, risks, and unresolved assumptions. After approval, merge it on GitHub, return locally to `main`, and update:

```bash
git switch main
git pull --ff-only
git branch -d concise-feature-name
```

Deleting the merged local branch does not delete its commits; the merged history retains them.

## Conflict and recovery basics

```bash
git restore path/to/file             # discard an unstaged file edit
git restore --staged path/to/file    # unstage without discarding the edit
git merge --abort                    # abandon an unresolved merge
git rebase --abort                   # abandon an unresolved rebase
git reflog                           # find recently visited commit positions
git revert COMMIT_ID                 # make a new commit that reverses a published commit
```

Avoid `git reset --hard`, `git clean -fd`, and force push until you understand exactly which uncommitted or remote work they can remove. On shared history, prefer `git revert` because it records the reversal rather than rewriting history.

## Do Not Commit Secrets

Never commit:

```text
TAVILY_API_KEY
APIFY_API_TOKEN
n8n production webhook URLs
```

Use `.env.example` for placeholders only.
