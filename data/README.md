# Data (agreed sample set)

This directory holds the **frozen** acceptance sample and supporting mappings for a validation round.

## Order matters

1. **`sample_issues.csv`** first — source of truth (12–18 rows, representative mix).
2. **`known_patterns.json`** second — derived from real families in the CSV, not guessed early.
3. **`kb_ticket_mapping.json`** last — only for groups that are stable enough to ground hints.

See [`docs/evaluation-sample-set.md`](../docs/evaluation-sample-set.md) (CSV-first philosophy and canonical artifacts).

## Files

| File | Role |
| ---- | ---- |
| `sample_issues.csv` | **v1 starter:** 8 rows with the recommended category mix (replace with real alerts, then add rows to reach 12–15). See [`docs/sample-issues-workflow.md`](../docs/sample-issues-workflow.md). |
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
