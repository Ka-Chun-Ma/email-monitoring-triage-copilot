# Publish this repository to GitHub

Use the **same name as this folder**: `email-monitoring-triage-copilot`.

## Prerequisites

- A [GitHub](https://github.com) account
- [Git](https://git-scm.com/) installed (this folder should already be a git repository after the initial commit)

## 1. Create an empty repository on GitHub

1. Sign in to GitHub.
2. Click **+** → **New repository**.
3. Set **Repository name** to: `email-monitoring-triage-copilot`
4. Choose **Public** or **Private**.
5. **Do not** add a README, `.gitignore`, or license (this project already has them locally).
6. Click **Create repository**.

## 2. Add the remote and push

In PowerShell, from the project root:

```powershell
cd path\to\email-monitoring-triage-copilot

git remote add origin https://github.com/YOUR_USERNAME/email-monitoring-triage-copilot.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

If you use SSH:

```powershell
git remote add origin git@github.com:YOUR_USERNAME/email-monitoring-triage-copilot.git
git push -u origin main
```

## 3. (Optional) Create a GitHub Project

A **Project** is a board (tasks / roadmap) separate from the code repo.

1. Open your profile or organization **Projects** tab, or go to the repository → **Projects** → **New project**.
2. Choose a template (e.g. **Board**).
3. Name it e.g. `email-monitoring-triage-copilot` to match this folder/repo.
4. Link the project to the repository if prompted.

## CLI alternative (GitHub CLI)

If you install [`gh`](https://cli.github.com/):

```powershell
gh auth login
gh repo create email-monitoring-triage-copilot --public --source=. --remote=origin --push
```

Adjust `--public` to `--private` if needed.
