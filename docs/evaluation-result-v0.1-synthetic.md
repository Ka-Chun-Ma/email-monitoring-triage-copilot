# Evaluation result notes — synthetic pass (frozen sample)

**Purpose:** Illustrate the [`evaluation-pass-v0.1.md`](evaluation-pass-v0.1.md) workflow using the current frozen `data/sample_issues.csv`, `src/run_pipeline.py` output, and filled review sheets.

**Not a human-subject study** — labels below are **synthetic reviewer judgments** for repo demonstration. Replace with your own baseline and MVP-assisted sheets for a real round.

## Artifacts

| File | Role |
| ---- | ---- |
| `data/sample_issues_review_sheet_manual_baseline.csv` | Stage A (no pipeline) |
| `data/sample_issues_review_sheet_mvp_assisted.csv` | Stage B (with pipeline output) |

## Pipeline snapshot (v0.1)

- `mapping_ready == true`: **2 / 12** (`ISS-EVAL-002`, `ISS-EVAL-003`)
- `triage_label_candidate == review_needed`: **8 / 12**
- **Triage vs manual `expected_triage_label` mismatch:** **1 / 12** — `ISS-EVAL-001` (manual `likely_recurring`, pipeline `review_needed`)

## The one bottleneck question (v0.1)

> **Is the largest bottleneck triage too conservative, or mapping too thin?**

**Answer for this frozen set and current code:**

### **Primary bottleneck: triage policy is too conservative (by design), not mapping sparsity alone**

**Reasoning:**

1. **Mapping is intentionally thin** — only timeout and file families have `kb_ticket_mapping.json` entries; duplicate is **deliberately unmapped** (`intentional_missing_mappings`). So “mapping is sparse” is **expected** in v0.1, not an accident.
2. The **clearest structural delta** between a reasonable manual first-pass and the pipeline is **`ISS-EVAL-001`**: canonical **known_recurring** duplicate on `ZSALES01`, where a reviewer still labels **`likely_recurring`**, but the pipeline applies **duplicate_key v0.1 rule** → **`review_needed` always**. That is a **triage-layer** choice, not fixable by adding KB rows for duplicate without first splitting subfamilies or relaxing guardrails.
3. Rows **`ISS-EVAL-007`**, **`ISS-EVAL-011`** show **mapping_ready false** while family matches — that is **honest missing mapping**, which the JSON already encodes. The pain there is **not** “we forgot to type KB IDs” but **when** it is safe to attach grounded refs.

### **Secondary: mapping expansion**

After triage is **selectively** less conservative (e.g. **canonical duplicate subfamily** with strict gates), **then** add **grounded** mappings for that subfamily—still without pretending object-level maturity for the whole duplicate family.

### **Suggested next step (fork)**

| Bottleneck | Next move |
| ---------- | --------- |
| **Triage (primary)** | Define **safe recurring subfamily** for duplicate (e.g. prod + canonical object + no escalate phrases) **or** accept `review_needed` for all duplicate matches until subfamily work ships. |
| **Mapping (secondary)** | Expand **`kb_ticket_mapping.json`** only for families already stable; keep **`do_not_apply_if_contains_any`** and intentional missing states. |

## Version

v0.1 (synthetic illustration)
