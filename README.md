# email-monitoring-triage-copilot

Deterministic-first, human-in-the-loop workflow to reduce triage and daily monitoring email packaging effort.

## Docs

| Document | Purpose |
| -------- | ------- |
| [docs/success-definition.md](docs/success-definition.md) | Success criteria and MVP Definition of Done (v1.2) |
| [docs/evaluation-sample-set.md](docs/evaluation-sample-set.md) | Fixed evaluation sample set rules and canonical `data/` artifacts |
| [docs/sample-issues-workflow.md](docs/sample-issues-workflow.md) | CSV v1 steps, `broad_category` enum, pitfalls, pattern/mapping order |
| [docs/sample-issues-review-v0.1.md](docs/sample-issues-review-v0.1.md) | Pilot v0.1 review notes, 12-row v1 candidate, patterns/mapping conservatism |
| [docs/mvp-boundary.md](docs/mvp-boundary.md) | In-scope / out-of-scope for MVP |
| [docs/failure-modes.md](docs/failure-modes.md) | Acceptable vs unacceptable failures |
| [docs/pipeline-v0.1.md](docs/pipeline-v0.1.md) | Minimal pipeline: family match → triage → grounded mapping |
| [docs/pipeline-v0.2.md](docs/pipeline-v0.2.md) | v0.2: duplicate subfamilies + `issue_subfamily` field |
| [docs/evaluation-pass-v0.1.md](docs/evaluation-pass-v0.1.md) | First hands-on evaluation: manual baseline vs MVP-assisted, bottleneck question |
| [docs/review-sheet-guide-v0.1.md](docs/review-sheet-guide-v0.1.md) | How to fill `sample_issues_review_sheet.csv` (comparable, short notes) |
| [docs/evaluator-summary-template-v0.1.md](docs/evaluator-summary-template-v0.1.md) | Blank template for post-pass evaluator summary |
| [docs/evaluator-summary-v0.1-round1.md](docs/evaluator-summary-v0.1-round1.md) | Example filled summary (round 1, simulated) |
| [docs/round-2-plan-v0.1.md](docs/round-2-plan-v0.1.md) | Round 2: refine duplicate judgment boundary (not scope expansion) |
| [docs/duplicate-subfamily-working-note-v0.1.md](docs/duplicate-subfamily-working-note-v0.1.md) | Human pass before code: canonical / context-poor / replay / mapping uncertainty |
| [docs/round-2-evaluation-note-v0.1.md](docs/round-2-evaluation-note-v0.1.md) | Short checklist: duplicate rerun (001 / 006 / 008 / 011) |
| [docs/evaluation-pass-v0.2-round2.md](docs/evaluation-pass-v0.2-round2.md) | Full round-2 judgment test: safety / precision / complexity gates |

## Setup (local)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run pipeline v0.1

Deterministic family match, triage candidate, and mapping layer (no email draft):

```powershell
python src/run_pipeline.py
```

See [docs/pipeline-v0.1.md](docs/pipeline-v0.1.md) and [docs/pipeline-v0.2.md](docs/pipeline-v0.2.md) (duplicate v0.2).

## Publish to GitHub

See [docs/github-setup.md](docs/github-setup.md).
