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
| `sample_issues_review_sheet.csv` | **Manual baseline / MVP-assisted review:** `expected_triage_label` (`likely_recurring` \| `likely_new` \| `review_needed`), `reviewer_agrees_with_broad_category` (`yes` \| `no`), `reviewer_notes`. Filled per validation round; not a substitute for `broad_category` / `why_this_category` on `sample_issues.csv`. |
| `known_patterns.json` | Deterministic patterns matched against normalized text. |
| `kb_ticket_mapping.json` | Grounded KB / ticket / owner mappings (no fabricated references). |

## Intentional coverage (five spines)

A valid agreed sample includes rows that exercise:

- known recurring  
- obvious / likely new  
- ambiguous grey zone (review-needed)  
- missing mapping  
- dangerous look-alike (safety challenge)  

The last two are where the MVP proves **honest uncertainty** vs **false confidence**.
