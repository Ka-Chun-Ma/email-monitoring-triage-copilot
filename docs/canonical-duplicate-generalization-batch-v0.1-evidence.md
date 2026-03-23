# Canonical duplicate generalization batch — expected vs observed (v0.1)

**Run:** `python src/run_pipeline.py` (default `data/sample_issues.csv`)  
**Batch:** four new rows appended: `ISS-GEN-013` … `ISS-GEN-016`  
**Code:** no `issue_id` logic; behavior from `known_patterns.json` + message text only.

| issue_id   | Expected pattern | Expected triage | Observed pattern | Observed triage | Match |
| ---------- | ---------------- | --------------- | ---------------- | --------------- | ----- |
| ISS-GEN-013 | PAT-001A | likely_recurring | PAT-001A | likely_recurring | yes |
| ISS-GEN-014 | PAT-001A | likely_recurring | PAT-001A | likely_recurring | yes |
| ISS-GEN-015 | PAT-001B | review_needed | PAT-001B | review_needed | yes |
| ISS-GEN-016 | PAT-001C | review_needed | PAT-001C | review_needed | yes |

**Stderr summary (full sample):** `rows=16 matched_family=15 mapping_ready=2 triage_review_needed=9`
