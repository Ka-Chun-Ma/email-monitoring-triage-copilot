# Data (agreed sample set)

This directory holds the **frozen** acceptance sample and supporting mappings for a validation round.

## Order matters

1. **`sample_issues.csv`** first — source of truth (pilot **8** rows → **v1 candidate 12** → up to **12–15** for full round; representative mix).
2. **`known_patterns.json`** second — derived from real families in the CSV, not guessed early.
3. **`kb_ticket_mapping.json`** last — only for groups that are stable enough to ground hints.

See [`docs/evaluation-sample-set.md`](../docs/evaluation-sample-set.md) (CSV-first philosophy and canonical artifacts).

## Files

| File | Role |
| ---- | ---- |
| `sample_issues.csv` | **v1 candidate (12 rows):** distribution 3 / 2 / 3 / 2 / 2; includes `why_this_category` and `would_match_family` (`yes` / `no` / `maybe`) per row. See [`docs/sample-issues-workflow.md`](../docs/sample-issues-workflow.md). |
| `sample_issues_review_sheet.csv` | Empty template. **Manual baseline / MVP-assisted:** `expected_triage_label`, `reviewer_agrees_with_broad_category` (`yes` \| `no` \| `partly`), `reviewer_notes`. How to fill: [`docs/review-sheet-guide-v0.1.md`](../docs/review-sheet-guide-v0.1.md). Full pass: [`docs/evaluation-pass-v0.1.md`](../docs/evaluation-pass-v0.1.md). |
| `sample_issues_review_sheet_manual_baseline.csv` | Example **Stage A** fill (synthetic). |
| `sample_issues_review_sheet_mvp_assisted.csv` | Example **Stage B** fill (synthetic). See [`docs/evaluation-result-v0.1-synthetic.md`](../docs/evaluation-result-v0.1-synthetic.md). |
| `known_patterns.json` | v0.1 — conservative pattern families; match ≠ safe recurring (see `triage_policy_notes`). |
| `kb_ticket_mapping.json` | v0.1 — grounded hints only where stable; `do_not_apply_if_contains_any` + `intentional_missing_mappings`. |

**Runnable slice:** `python src/run_pipeline.py` reads the CSV and both JSON files (see [docs/pipeline-v0.1.md](../docs/pipeline-v0.1.md)).

## Intentional coverage (five spines)

A valid agreed sample includes rows that exercise:

- known recurring  
- obvious / likely new  
- ambiguous grey zone (review-needed)  
- missing mapping  
- dangerous look-alike (safety challenge)  

The last two are where the MVP proves **honest uncertainty** vs **false confidence**.
