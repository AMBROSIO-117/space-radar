# GitHub Push Guide

## 1. Initialize Git

```bash
git init
git status
```

## 2. Add Files

```bash
git add .
git status
```

## 3. Commit

```bash
git commit -m "Initial Space Procurement Signal Radar hackathon project"
```

## 4. Create GitHub Repo

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

Option B: use GitHub CLI if authenticated.

```bash
gh repo create space-procurement-signal-radar --public --source=. --remote=origin --push
```

## Do Not Commit Secrets

Never commit:

```text
TAVILY_API_KEY
APIFY_API_TOKEN
n8n production webhook URLs
```

Use `.env.example` for placeholders only.

