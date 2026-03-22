# Evaluator Summary — Round 1 (v0.1)

Filled using [`evaluator-summary-template-v0.1.md`](evaluator-summary-template-v0.1.md). Review rows: [`data/sample_issues_review_sheet_manual_baseline.csv`](../data/sample_issues_review_sheet_manual_baseline.csv), [`data/sample_issues_review_sheet_mvp_assisted.csv`](../data/sample_issues_review_sheet_mvp_assisted.csv). Pipeline: `src/run_pipeline.py` v0.1.

## Evaluation pass
- Evaluation version: **v0.1**
- Evaluation date: **2026-03-21**
- Reviewer: **Simulated first-round pass (methodology-aligned; replace with human reviewer name)**
- Sample set version: **12-row frozen `data/sample_issues.csv` (v1 candidate)**
- Pipeline version: **v0.1** (`run_pipeline.py`)

---

## 1. Manual baseline summary

### Total review effort
- Manual baseline review time: **~28 minutes** (estimated for 12 rows: triage + mental grouping + noting risk)
- Manual packaging estimate: **~22 minutes** (outline sections for daily monitoring email)
- Overall perceived cognitive load: **medium**

### What felt easy
- **Straightforward:** ISS-EVAL-002 (canonical timeout), ISS-EVAL-003 (clean file path), ISS-EVAL-005 (obvious new API drift).
- **Easy to group manually:** recurring-style timeout and file-missing “shapes” were recognizable without tooling.

### What felt hard
- **Ambiguous:** ISS-EVAL-006, 009, 010, 012 — conflicting context, environment, or cause chain.
- **Caution:** ISS-EVAL-004 (new job under timeout wording), ISS-EVAL-007 (timeout without mapping), ISS-EVAL-008 (replay vs fact duplicate), ISS-EVAL-011 (staging duplicate without mapping).
- **Surface familiar, risky underneath:** ISS-EVAL-008, 009, 012.

### Manual baseline observations
- **Most time:** reconciling “looks like a known family” with “safe to bucket for email” (duplicate and file families).
- **Repeated mental work:** separating **family resemblance** from **safe recurring label** and from **grounded KB/ticket**.
- **Hardest uncertainty:** duplicate-key and file-missing rows where semantics or environment change handling.

---

## 2. MVP-assisted review summary

### Total review effort
- MVP-assisted review time: **~14 minutes** (read pipeline JSON + validate per row)
- MVP-assisted packaging estimate: **~12 minutes** (families and labels pre-sorted; still need human pass for edge rows)
- Overall perceived cognitive load: **low–medium**

### Where the MVP clearly helped
- **Family match:** Grouping timeout vs file vs duplicate **reduced scan time** once the JSON was trusted.
- **Triage candidates:** Mostly aligned; **escalate phrases** correctly pushed **004, 009, 010, 012** to `review_needed`.
- **Grounded hints:** **002 and 003** benefited from **KB / runbook / owner** when mapping applied.
- **Structure:** Less rebuilding of “what family is this?” from scratch.

### Where the MVP helped only a little
- **ISS-EVAL-001:** Same family as other duplicates but **manual** still treats as **likely recurring** for first-pass; pipeline **always** emits `review_needed` for duplicate family (policy). Helpful for safety narrative; **adds friction** vs operational “known good” row.
- **ISS-EVAL-007:** Pipeline says **likely_recurring** + **mapping_ready false**; manual emphasis was **review until mapping exists** — **triage vs missing-mapping** tension is visible but not identical to manual.

### Where the MVP may have created risk or false comfort
- **Low risk in this sample:** escalate paths and blocked mappings were mostly honest.
- **Watch:** if readers **only** see `matched_family` and skip **triage_label_candidate** and **mapping_ready**, they could misread **007** (recurring label with no mapping).

---

## 3. Comparison summary

### Triage effort comparison
- Was first-pass triage easier with MVP assistance? **partly**
- **Why?** Faster **scan and grouping**; tension on **001** and **007** where manual and pipeline priorities differ slightly.

### Packaging effort comparison
- Was packaging preparation easier with MVP assistance? **yes**
- **Why?** Pre-labeled families and explicit mapping rows for **002/003** reduce re-derivation of structure.

### Uncertainty visibility comparison
- Did the MVP make uncertainty more visible? **yes**
- **Why?** **`missing_mapping_flag`** and absent hints when guards fire match the “do not pretend” rule set.

### Overall comparison judgment
- Compared with manual baseline, the MVP currently feels: **structurally promising but still too conservative** on **duplicate_key** (by design in v0.1), and **useful** on **timeout/file** when mapping applies.

---

## 4. Pattern and mapping observations

### Family match usefulness
- **Useful:** `timeout_threshold_exceeded`, `reference_file_missing` for orientation.
- **Broad:** `duplicate_key_violation` — correctly spans multiple postures; **needs subfamilies** if any row should ever be `likely_recurring` with guardrails.
- **Subfamily refinement:** Duplicate: separate **fact canonical** vs **staging** vs **replay** when data supports it.

### Triage posture observations
- **`review_needed` justified:** 004, 006, 008–012, and duplicate-policy rows.
- **`review_needed` vs manual:** **001** — pipeline more conservative than manual baseline.
- **`likely_recurring` felt safe:** **002, 003** with mapping.
- **`likely_recurring` too optimistic:** **007** from pipeline vs manual **review_needed** emphasis — **bottleneck question** applies here.

### Mapping usefulness observations
- **Hints mattered** where applied (**002, 003**).
- **Missing mappings** surfaced **honestly** when guards or intentional lists blocked application.
- **Next bottleneck (this pass):** **both** — **triage conservatism on duplicate family** (001 vs policy) and **mapping sparsity** (007, duplicate family overall). Primary fork: **refine duplicate subfamilies / triage rules** *or* **expand mapping only after subfamilies are stable**.

---

## 5. Safety and failure posture observations

### Safety posture
- Did the MVP behave conservatively in ambiguous cases? **yes**
- Did it avoid fabricated certainty? **yes**
- Did it make missing mapping visible? **yes**

### Watchlist
- **False comfort:** **001** if team reads “duplicate family” as “same as always” — mitigated by **review_needed** from pipeline.
- **Semantic drift:** **008**
- **Same family different meaning:** **004, 010**
- **Must stay human-reviewed:** **006, 008–012**

### Unacceptable failures observed
- Were any unacceptable failures from `docs/failure-modes.md` observed? **no**

---

## 6. Most important conclusion from this pass

### What is the single most important thing learned?
- **Three layers are operational:** family match, triage label, and mapping can **diverge** on the same row (e.g. **001**, **007**) — this is a **feature**, not noise, if the UI/reporting keeps all three visible.

### What is the MVP currently best at?
- **Timeout and file families** when **escalate guards** and **mapping guards** align with the message text.

### What is the MVP currently weakest at?
- **Duplicate-key family:** **one-size review_needed** is safe but may **over-correct** on **clearly canonical prod fact** rows until **subfamilies** exist.

---

## 7. Recommended next step

### Recommended next step:
- **refine subfamilies** (duplicate_key_violation first: e.g. fact-table canonical vs replay vs staging-context-poor), *then* reassess mapping — **expand grounded mappings selectively** only for subfamilies that stay stable across the sample.

### Why this is the highest-leverage next step:
- **Mapping expansion** without **subfamily separation** risks looking “complete” while **duplicate** remains the riskiest family in the set.

---

## 8. Pass judgment for v0.1

### Is this evaluation pass encouraging?
- **partly**

### Why?
- **Pipeline proves separation of concerns** and **honest missing mapping**; **duplicate policy** needs iteration to recover **operational recurring** rows without weakening safety rows.

### Should the project continue on the current path?
- **yes, but with targeted refinement**

### Final evaluator note
- Replace this simulated pass with a **human reviewer** on the same frozen CSV; keep **two review sheets** (manual vs MVP) and **one summary** per round. Re-run after any change to `known_patterns.json` / triage rules.

---

## Version
v0.1 (round 1)
