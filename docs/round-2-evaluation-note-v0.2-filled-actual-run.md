# Round 2 evaluation note v0.2 — filled example (actual pipeline run)

**What this is:** The **first filled evidence** for the v0.2 note structure — not another template polish.

**Source:** Output from `python src/run_pipeline.py` against frozen `data/sample_issues.csv`, with **field values copied from code** (see JSON excerpt below). **Reviewer prose** is written in the **short, operational** style recommended for judgment-boundary validation; a **human evaluator** should still confirm or edit.

**Repo state (when generated):** `known_patterns.json` v0.2, `src/run_pipeline.py` v0.2, commit `2890516` (update if you rerun on a different commit).

**Important correction vs informal mocks:** For duplicate rows, **`mapping_ready` is `false`** in this KB — there is no duplicate-family mapping entry. Do **not** mark `mapping_ready: true` for **001** unless `kb_ticket_mapping.json` is intentionally extended and grounded.

---

## Pipeline excerpt (four rows only)

```json
{
  "ISS-EVAL-001": {
    "matched_pattern_id": "PAT-001A-CANONICAL-DUPLICATE",
    "issue_subfamily": "canonical_duplicate",
    "triage_label_candidate": "likely_recurring",
    "would_escalate_review": false,
    "mapping_ready": false,
    "missing_mapping_flag": true
  },
  "ISS-EVAL-006": {
    "matched_pattern_id": "PAT-001B-CONTEXT-POOR-DUPLICATE",
    "issue_subfamily": "context_poor_duplicate",
    "triage_label_candidate": "review_needed",
    "would_escalate_review": true,
    "mapping_ready": false,
    "missing_mapping_flag": true
  },
  "ISS-EVAL-008": {
    "matched_pattern_id": "PAT-001C-REPLAY-SEMANTIC-DRIFT-DUPLICATE",
    "issue_subfamily": "replay_semantic_drift_duplicate",
    "triage_label_candidate": "review_needed",
    "would_escalate_review": true,
    "mapping_ready": false,
    "missing_mapping_flag": true
  },
  "ISS-EVAL-011": {
    "matched_pattern_id": "PAT-001B-CONTEXT-POOR-DUPLICATE",
    "issue_subfamily": "context_poor_duplicate",
    "triage_label_candidate": "review_needed",
    "would_escalate_review": true,
    "mapping_ready": false,
    "missing_mapping_flag": true
  }
}
```

---

## Before / after audit table (filled)

**v0.1 reference:** Single pattern `PAT-001-DUPLICATE-KEY-FAMILY`, triage `review_needed` for all duplicate matches (see [`evaluator-summary-v0.1-round1.md`](evaluator-summary-v0.1-round1.md)).

| issue_id | v0.1 pattern | v0.2 pattern | v0.1 triage | v0.2 triage | v0.2 `would_escalate_review` | `mapping_ready` | Safe? | Reviewer note |
| -------- | ------------- | ------------ | ----------- | ----------- | ----------------------------- | ----------------- | ----- | --------------- |
| ISS-EVAL-001 | PAT-001-DUPLICATE-KEY-FAMILY | PAT-001A-CANONICAL-DUPLICATE | review_needed | likely_recurring | false | false | yes | Narrower first-pass posture; tied to canonical subfamily match. **Not** mapping-ready — KB still does not ground duplicate hints. |
| ISS-EVAL-006 | PAT-001-DUPLICATE-KEY-FAMILY | PAT-001B-CONTEXT-POOR-DUPLICATE | review_needed | review_needed | true | false | yes | Conservative protection preserved; no false recurring comfort. |
| ISS-EVAL-008 | PAT-001-DUPLICATE-KEY-FAMILY | PAT-001C-REPLAY-SEMANTIC-DRIFT-DUPLICATE | review_needed | review_needed | true | false | yes | Stays in review; replay / drift remains visible. |
| ISS-EVAL-011 | PAT-001-DUPLICATE-KEY-FAMILY | PAT-001B-CONTEXT-POOR-DUPLICATE | review_needed | review_needed | true | false | yes | Temporary `context_poor` placement; conservative. **Hypothesis:** mapping-uncertainty still mentally present — see 011 note in v0.2 template. |

---

## Watchpoint 1 — ISS-EVAL-001

| Question | Your note |
| -------- | --------- |
| Does **001** now look more reasonably like `likely_recurring`? | Yes, as **first-pass** posture only; aligns with PAT-001A. |
| Explainable from subfamily logic, not row-specific hack? | Yes — match is from shared canonical rules, not a one-off `issue_id` branch in code. |
| False comfort if skimmed? | Some risk if reader ignores `mapping_ready: false` and `missing_mapping_flag: true`. Mitigation: reporting layer should keep triage and mapping separate. |
| Operationally useful, not only technically different? | Yes — reduces blanket `review_needed` for a row that reads as canonical duplicate, while risky rows stay under review. |

---

## Watchpoint 2 — ISS-EVAL-006 / 008 / 011

| issue_id | Expected posture | Observed v0.2 triage | Observed subfamily | Safe? | Concern |
| -------- | ---------------- | --------------------- | -------------------- | ----- | ------- |
| ISS-EVAL-006 | `review_needed` | `review_needed` | `context_poor_duplicate` | yes | none |
| ISS-EVAL-008 | `review_needed` | `review_needed` | `replay_semantic_drift_duplicate` | yes | none |
| ISS-EVAL-011 | `review_needed` | `review_needed` | `context_poor_duplicate` | yes | mapping-uncertainty flavor still there; label does not bury it if reviewer reads message + `missing_mapping_flag` |

---

## Duplicate handling overall

| Question | Answer | Notes |
| -------- | ------ | ----- |
| More useful than v0.1? | yes | `001` gets a narrower, explainable first-pass label. |
| Not more dangerous? | yes | `006` / `008` / `011` stay `review_needed`. |
| Bounded precision vs broad confidence? | yes | Change is localized to canonical subfamily; no fake mapping. |
| Explainable subfamilies? | yes | A / B / C remain short to describe. |
| Real judgment improvement vs prettier relabel? | partly → yes | **Human** should confirm on real ops review; this file is evidence-ready, not a substitute for that sign-off. |

---

## One-sentence answer

Duplicate subfamily refinement **narrowed** a **canonical** duplicate case (`001`) **without** granting **mapped** hints **and** without **relaxing** ambiguous duplicate rows — **bounded precision**, not a confidence sweep.

---

## Preliminary conclusion

**Option A — Directionally successful** (pending human sign-off)

Round 2 appears directionally successful because **ISS-EVAL-001** gained a narrower and explainable first-pass posture, while **ISS-EVAL-006**, **ISS-EVAL-008**, and **ISS-EVAL-011** remained conservatively protected.

---

## Decision after this note (draft)

| Choice | Why |
| ------ | --- |
| [x] Continue duplicate refinement | Optional: tighten reporting so `mapping_ready` / `missing_mapping_flag` stay visible next to `likely_recurring` for `001`; consider **generalization** evidence beyond one sample row before email scaffold. |
| [ ] Proceed toward email draft scaffold | |
| [ ] Hold, simplify, or partially revert | |

---

## Evaluator metadata

| Field | Value |
| ----- | ----- |
| Evaluator | *Automated field extract + draft prose — replace with human name* |
| Date | *fill on human review* |
| Pipeline / patterns | v0.2 |

---

## Sanity check (one question)

> If another reviewer **only** read this note tomorrow, would they think **duplicate problems are solved**?

**Target:** No — they should see **where** posture narrowed and **where** review and missing mapping still apply.

---

## Version

v0.1 (first filled actual run; revise after human rerun / new commit)
