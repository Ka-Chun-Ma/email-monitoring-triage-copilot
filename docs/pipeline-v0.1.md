# Pipeline v0.1 (`src/run_pipeline.py`)

## Purpose

Minimal runnable slice that **keeps three concerns separate**:

1. **Family match** — does the alert text match a pattern family in `data/known_patterns.json`?
2. **Triage posture** — given a match, what is the candidate triage label (`likely_recurring` \| `likely_new` \| `review_needed`)? **Not** “matched ⇒ recurring.”
3. **Mapping readiness** — if a mapping exists in `data/kb_ticket_mapping.json` and passes guards, emit grounded `related_kb_id` / `related_ticket_id` / `owner_hint`. Otherwise `mapping_ready: false`.

Email draft generation is **out of scope** for v0.1.

## Run

From the repository root:

```powershell
.\.venv\Scripts\Activate.ps1
python src/run_pipeline.py
```

Optional arguments:

| Flag | Default |
| ---- | ------- |
| `--sample` | `data/sample_issues.csv` |
| `--patterns` | `data/known_patterns.json` |
| `--kb` | `data/kb_ticket_mapping.json` |
| `--quiet` | Suppress stderr summary line |

Stdout is a JSON array of result objects (stderr prints a one-line summary unless `--quiet`).

## Output fields (per row)

| Field | Meaning |
| ----- | ------- |
| `matched_family` | Pattern family id, or `null` if no pattern matched |
| `matched_pattern_id` | Pattern record id, or `null` |
| `would_escalate_review` | `true` when `triage_label_candidate` is `review_needed` |
| `triage_label_candidate` | Pipeline triage only (see policies in JSON + code) |
| `related_kb_id` / `related_ticket_id` / `owner_hint` | From mapping layer, or `null` |
| `mapping_ready` | `true` only when a mapping record was applied |
| `missing_mapping_flag` | `true` when a family matched but no mapping was applied |

## Relationship to `sample_issues.csv`

`broad_category` and `why_this_category` on the CSV are **evaluation scaffolding**. Pipeline output may **differ** from `broad_category` by design (e.g. duplicate-key family defaults to `review_needed` in v0.1; timeout rows with missing grounded mapping may still be `likely_recurring` with `mapping_ready: false`). Compare both during validation.

## Version

v0.1
