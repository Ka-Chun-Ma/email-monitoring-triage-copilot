# Canonical duplicate — boundary-stress batch v0.2 (expected vs observed)

**Run:** `python src/run_pipeline.py`  
**Batch only:** `ISS-GEN-017` … `ISS-GEN-020` (second generalization batch)  
**Code:** no `issue_id` logic; text rules only.

| issue_id | Design intent | Expected pattern | Expected triage | Observed pattern | Observed triage | Match |
| -------- | ------------- | ---------------- | --------------- | ---------------- | --------------- | ----- |
| ISS-GEN-017 | Clear canonical | PAT-001A | likely_recurring | PAT-001A | likely_recurring | yes |
| ISS-GEN-018 | A/B edge: `reported` | PAT-001B | review_needed | PAT-001B | review_needed | yes |
| ISS-GEN-019 | A/B edge: `source row context not provided` | PAT-001B | review_needed | PAT-001B | review_needed | yes |
| ISS-GEN-020 | A/C edge: replay + reinsert + differs | PAT-001C | review_needed | PAT-001C | review_needed | yes |

**Stderr (full sample, 20 rows):** `rows=20 matched_family=19 mapping_ready=2 triage_review_needed=12`

**Note:** v0.1 batch remains **valid evidence**; **PAT-001A stability** is **not** treated as **closed** — this batch adds **boundary** stress only.
