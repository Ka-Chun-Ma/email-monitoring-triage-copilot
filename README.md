# email-monitoring-triage-copilot

**Deterministic-first, human-in-the-loop** triage for monitoring-style issues: separate **pattern match**, **triage posture**, and **grounded KB/ticket mapping** — without treating a label match as **resolution**.

> **Portfolio:** Start with **[`docs/case-study-v0.1.md`](docs/case-study-v0.1.md)** for the full narrative (problem → design → round-2 duplicates → generalization → email scaffold → frozen checkpoint). **Implementation is frozen** at documented checkpoints; this repo emphasizes **governance and evidence**, not live production deployment.

| | |
| --- | --- |
| **Case study** | [`docs/case-study-v0.1.md`](docs/case-study-v0.1.md) |
| **Resume / LinkedIn snippet** | Inside case study: *Resume-ready summary* |
| **Project status (phase)** | [`docs/project-control-tower.md`](docs/project-control-tower.md) |
| **Handoff / review** | [`docs/relay-to-gpt.md`](docs/relay-to-gpt.md) |

---

## What this repo contains

- **`src/run_pipeline.py`** — CSV in → JSON: `matched_family`, `issue_subfamily` (duplicates v0.2), `triage_label_candidate`, `mapping_ready`, `missing_mapping_flag`, etc.
- **`data/known_patterns.json`** — Auditable family/subfamily rules (v0.2 duplicate split: PAT-001A–001C).
- **`data/kb_ticket_mapping.json`** — Conservative grounded mappings; gaps are explicit.
- **`src/email_scaffold.py`** — **Frozen** v0.1: pipeline JSON → markdown **draft** (likely recurring / review / mapping-gap summary). Not production mail.

Frozen checkpoint: [`docs/email-scaffold-checkpoint-v0.1.md`](docs/email-scaffold-checkpoint-v0.1.md).

---

## Setup (local)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run pipeline

```powershell
python src/run_pipeline.py
```

Optional: `--sample path/to.csv`, `--quiet` (suppress stderr stats). Default sample: `data/sample_issues.csv`.

## Email draft scaffold (frozen v0.1)

```powershell
python src/run_pipeline.py --quiet | python src/email_scaffold.py
```

See [`docs/email-scaffold-prototype-v0.1.md`](docs/email-scaffold-prototype-v0.1.md) and saved examples under `docs/email-scaffold-*-output-v0.1.md`.

---

## Documentation index

| Document | Purpose |
| -------- | ------- |
| [docs/case-study-v0.1.md](docs/case-study-v0.1.md) | **Portfolio case study** |
| [docs/success-definition.md](docs/success-definition.md) | Success criteria and MVP Definition of Done |
| [docs/evaluation-sample-set.md](docs/evaluation-sample-set.md) | Fixed evaluation sample rules |
| [docs/pipeline-v0.2.md](docs/pipeline-v0.2.md) | Pipeline v0.2 (duplicate subfamilies) |
| [docs/evaluation-pass-v0.2-round2.md](docs/evaluation-pass-v0.2-round2.md) | Round 2 judgment test (full audit) |
| [docs/round-2-evaluation-note-v0.2.md](docs/round-2-evaluation-note-v0.2.md) | Focused evaluation note (**frozen** template) |
| [docs/round-2-evaluation-note-v0.2-filled-actual-run.md](docs/round-2-evaluation-note-v0.2-filled-actual-run.md) | Filled evidence (real run) |
| [docs/canonical-duplicate-generalization-batch-v0.1-evidence.md](docs/canonical-duplicate-generalization-batch-v0.1-evidence.md) | Generalization batch v0.1 |
| [docs/canonical-duplicate-generalization-batch-v0.2-boundary-evidence.md](docs/canonical-duplicate-generalization-batch-v0.2-boundary-evidence.md) | Boundary-stress batch v0.2 |
| [docs/email-scaffold-checkpoint-v0.1.md](docs/email-scaffold-checkpoint-v0.1.md) | Email scaffold frozen checkpoint |

Additional governance, MVP, round-1, and workflow docs remain under `docs/` (see earlier revisions in git history or browse the folder).

## Publish to GitHub

See [docs/github-setup.md](docs/github-setup.md).
