# email-monitoring-triage-copilot

Deterministic-first, human-in-the-loop workflow to reduce triage and daily monitoring email packaging effort.

## Docs

| Document | Purpose |
| -------- | ------- |
| [docs/success-definition.md](docs/success-definition.md) | Success criteria and MVP Definition of Done |
| [docs/mvp-boundary.md](docs/mvp-boundary.md) | In-scope / out-of-scope for MVP |
| [docs/failure-modes.md](docs/failure-modes.md) | Acceptable vs unacceptable failures |

## Setup (local)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Publish to GitHub

See [docs/github-setup.md](docs/github-setup.md).
