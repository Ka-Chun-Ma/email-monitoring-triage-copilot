# Pipeline v0.2 (`src/run_pipeline.py`)

## Changes from v0.1

- **`duplicate_key_violation`** is split into **three sub-patterns** in `data/known_patterns.json` v0.2 (see `version` in file):
  - **`PAT-001A-CANONICAL-DUPLICATE`** → `issue_subfamily`: `canonical_duplicate` → default triage **`likely_recurring`** (still **`mapping_ready: false`** unless KB adds duplicate mapping later).
  - **`PAT-001B-CONTEXT-POOR-DUPLICATE`** → `context_poor_duplicate` → **`review_needed`**.
  - **`PAT-001C-REPLAY-SEMANTIC-DRIFT-DUPLICATE`** → `replay_semantic_drift_duplicate` → **`review_needed`**.
- Output includes **`issue_subfamily`** when the matched pattern defines it (duplicate subfamilies); `null` for timeout/file patterns.

## Round 2 success signals

1. **ISS-EVAL-001** moves from blanket duplicate **`review_needed`** (v0.1) to **`likely_recurring`** with **`canonical_duplicate`** (when rules match).
2. **ISS-EVAL-006**, **008**, **011** remain clearly in **`review_needed`** with the correct subfamily.

## Run

Same as v0.1:

```powershell
python src/run_pipeline.py
```

See also [`pipeline-v0.1.md`](pipeline-v0.1.md) for field definitions, [`round-2-plan-v0.1.md`](round-2-plan-v0.1.md) for rationale, and [`evaluation-pass-v0.2-round2.md`](evaluation-pass-v0.2-round2.md) for how to **prove** refinement (safety / precision / complexity gates).

## Version

v0.2
