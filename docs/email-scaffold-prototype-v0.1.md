# Email scaffold prototype v0.1

**Status:** Constrained presentation layer only. **No** changes to duplicate triage rules, `known_patterns.json`, evaluation templates, or KB mapping scope.

## Input

JSON array from **`python src/run_pipeline.py`** (stdout). Same fields the pipeline already emits.

## Output

Plain-text / markdown body with **three** separated lists:

1. **Likely recurring** — `triage_label_candidate == likely_recurring` (explicitly *not* final resolution).
2. **Review needed** — `review_needed`, plus a sub-block for **`likely_new`** (unmatched family) under human review.
3. **No grounded KB / ticket / owner** — `missing_mapping_flag == true` (mapping gap; not automation).

Overlap between sections is **documented** (e.g. recurring + missing mapping).

## Human review

Header and footer state that the draft is **not** closure and that **human review is mandatory**.

**Skim hardening (copy only):** Immediately after the subject line, a one-line **Action required** reminder; each section heading includes an **item count** so reviewers see workload at a glance.

## Command

```bash
python src/run_pipeline.py --quiet | python src/email_scaffold.py
```

(Or redirect stderr: `2>/dev/null` / `2>$null` if not using `--quiet`.)

Optional: `--date YYYY-MM-DD` or env `EMAIL_SCAFFOLD_DATE`.

## Implementation

`src/email_scaffold.py`
