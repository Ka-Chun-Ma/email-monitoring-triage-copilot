# Duplicate Subfamily Working Note v0.1

## Purpose

This working note supports round 2 refinement for the `duplicate_key_violation` family (see [`round-2-plan-v0.1.md`](round-2-plan-v0.1.md)).

The **most valuable part is not the table itself.** It is the forced question:

> Do these duplicate cases share the **same operational meaning**, or only the **same surface wording**?

If that question is skipped, two failures are common:

1. **Collapse** canonical, context-poor, and replay-style rows into **one** “recurring” path just to lower `review_needed` count.  
2. **Overfit** a subfamily rule to **one** sample row so it works in the demo but **does not generalize**.

This note exists to separate human judgment **before** formalizing new pattern logic.

This is not the final pattern specification.
It is a temporary judgment aid used to:
- inspect duplicate-related sample rows
- identify meaningful subfamily boundaries
- test whether refinement is justified
- avoid hard-coding pattern logic too early

---

## Why this note exists

Round 1 showed that the current duplicate-key family is too coarse.

The current family includes more than one operational meaning:
- canonical recurring-looking duplicate
- context-poor duplicate
- replay or semantic-drift duplicate
- duplicate cases with uncertain mapping readiness

Treating them all the same is safe, but too blunt.
Refining them too quickly in code would also be risky.

This note exists to slow down and separate meanings first.

---

## Current duplicate-family design problem

The current `duplicate_key_violation` family can already match familiar wording.

That part is useful.

The problem is that family match alone is not enough to decide:
- whether the case is safely recurring
- whether it should remain review-needed
- whether grounded mapping should apply

In other words:

family match is already working better than triage granularity.

This note helps refine the second part without damaging the first.

---

## Candidate duplicate subfamilies

Round 2 currently assumes three working subfamilies.

These are working labels, not final schema commitments.

### 1. Canonical duplicate in stable load context
Working meaning:
- familiar duplicate-key wording
- stable load context
- no replay indicators
- no obvious missing-context warning
- looks like a standard recurring duplicate handling scenario

Working posture:
- possible candidate for narrower recurring treatment later
- not automatically mapping-ready by default

### 2. Context-poor or staging duplicate
Working meaning:
- duplicate-key wording is present
- but key context is incomplete
- staging language may be present
- SQL or row-level detail may be missing
- not safe enough for confident recurring treatment

Working posture:
- should remain `review_needed`

### 3. Replay or semantic-drift duplicate
Working meaning:
- duplicate-key wording is present
- but replay, reinsert, audit, or changed logical behavior is indicated
- surface family looks familiar
- operational meaning is different from ordinary duplicate handling

Working posture:
- should remain `review_needed`

---

## Very small human pass (do this before any code)

Re-read **only** these four rows in `data/sample_issues.csv`: **ISS-EVAL-001**, **006**, **008**, **011**.

For each row, you should be able to state **stably** (out loud or in one line of notes):

| Question | What you are deciding |
| -------- | ---------------------- |
| **Canonical?** | Is this a **standard** duplicate-in-load scenario your team would usually bucket with prior handling? |
| **Familiar surface only?** | Is wording familiar but **context too thin** to treat like production duplicate handling? |
| **Semantic drift?** | Does **replay / audit / reinsert** (or similar) change **meaning** even though “duplicate key” appears? |
| **Mapping uncertainty only?** | Is the ambiguity mostly **no KB/owner yet** (e.g. staging object)—and **not** necessarily a new subfamily until evidence grows? |

If you cannot separate these four comfortably, **do not** change `known_patterns.json` yet. The bottleneck is still judgment, not syntax.

**One-line purpose (what this pass is really for):**  
It is **not** “get the labels right.” It is to confirm **which rows in the duplicate family are only surface-similar** and **which actually share the same kind of safely handleable operational meaning**—before any rule or mapping change.

Then use the filled table below as the round 2 starting point.

---

## Working review table (initial labels — round 2 entry point)

Filled for **ISS-EVAL-001**, **006**, **008**, **011** only. Adjust later if the frozen sample or ops context changes.

| issue_id | proposed subfamily | why this subfamily | current safe posture | notes |
| -------- | -------------------- | ------------------- | -------------------- | ----- |
| ISS-EVAL-001 | `canonical_duplicate` | Standard duplicate-key wording in a normal load context. Business key and target are present. No replay indicators or missing-context warnings are visible. | **candidate for narrower recurring later** (not automatic mapping-ready) | Cleanest anchor row for a canonical duplicate subfamily; stability of meaning still does not imply grounded mapping by itself. |
| ISS-EVAL-006 | `context_poor_duplicate` | Duplicate-key wording is present, but the alert explicitly says that full SQL and source row context are not provided. Surface family is familiar, but evidence is too thin for safe recurring handling. | **`review_needed`** | Strong example of familiar wording without enough context; protects against false comfort. |
| ISS-EVAL-008 | `replay_semantic_drift_duplicate` | Duplicate-key wording is present, but replay / reinsert language changes the operational meaning. The message explicitly says it differs from normal fact-table duplicate handling. | **`review_needed`** | Strong semantic-drift trap; must stay clearly protected even if canonical duplicate handling is narrowed later. |
| ISS-EVAL-011 | `mapping_uncertain_duplicate` | Duplicate-family match is plausible, but the main unresolved issue is not only family recognition—grounded mapping readiness is still not established. This row should not be used as evidence that duplicate handling is stable enough for confident mapping. | **`review_needed`** | Keep separate from canonical for now; may later merge into a context-poor branch only if evidence strengthens—**or** stay as mapping-uncertain. Alternative working label: `context_poor_or_mapping_uncertain` if you prefer one bucket until you split further. |

**Source CSV columns (for traceability):** `ISS-EVAL-001` — `known_recurring`; `006` — `review_needed`; `008` — `safety_challenge`; `011` — `missing_mapping`. `would_match_family` on the sample CSV remains the evaluation scaffold from v1.

### Initial round-2 judgment
At this stage, only ISS-EVAL-001 looks like a possible candidate for a narrower recurring posture later.
ISS-EVAL-006 should remain protected as a context-poor duplicate.
ISS-EVAL-008 should remain protected as a replay / semantic-drift duplicate.
ISS-EVAL-011 should remain protected until duplicate-family mapping readiness is better understood.

---

## How to use this working table

For each duplicate-related row, ask:

1. Is this row only familiar on the surface, or also familiar in operational meaning?
2. Is the context strong enough to support a narrower recurring posture?
3. Does this row clearly belong to a stable subfamily, or is it still too ambiguous?
4. Would narrowing this row make the system genuinely more useful, or just more confident-looking?
5. If this row were misclassified as safe recurring, what is the risk?

Do not optimize for elegance.
Optimize for safe separation of meanings.

---

## Practical classification hints

### Likely canonical duplicate indicators
These are weak working clues, not final rules:
- normal load context
- standard duplicate-key wording
- business key and target wording both present
- no replay language
- no missing-context language
- no special caution phrases

### Likely context-poor duplicate indicators
Examples:
- "full SQL ... not provided"
- "source row context not provided"
- staging wording without enough detail
- message too thin to support safe reuse of prior handling logic

### Likely replay / semantic-drift indicators
Examples:
- "replay"
- "reinserted same logical row"
- "differs from fact-table duplicate handling"
- wording that implies changed operational meaning despite family similarity

---

## What this note is trying to prevent

This note exists to prevent the following mistakes:

### Mistake 1
Treating every duplicate-family row as equally safe once the family match succeeds.

### Mistake 2
Overfitting a subfamily rule to one example row without stable operational meaning.

### Mistake 3
Using mapping availability as a shortcut for triage confidence.

### Mistake 4
Expanding duplicate handling before replay and context-poor rows are clearly protected.

---

## Suggested round 2 workflow

### Step 1
Review all duplicate-related sample rows manually using this note.

### Step 2
Assign a provisional subfamily label to each duplicate-related row.

### Step 3
Write down any row that still feels hard to place.

### Step 4
Only after that, update `data/known_patterns.json`.

### Step 5
Then update `src/run_pipeline.py`.

### Step 6
Re-run the frozen sample set and compare whether usefulness improved without safety regression.

---

## Success condition for this note

This note has done its job if it helps the builder answer:

- Which duplicate rows are truly canonical?
- Which duplicate rows are still too ambiguous?
- Which duplicate rows are semantic-drift traps?
- Is there enough evidence to justify subfamily refinement?

If those answers are still unclear, the correct next move is not more code.
The correct next move is more careful sample thinking.

---

## Open questions

Use this section to record unresolved judgment questions.

- **ISS-EVAL-011:** Working label is **`mapping_uncertain_duplicate`** (vs `context_poor_or_mapping_uncertain`). Revisit after round 2 pattern experiments: merge vs keep separate?
- **ISS-EVAL-001:** Is one canonical row enough to justify a narrower recurring path in code, or do you want another canonical example before changing `run_pipeline.py`?
- Are any duplicate-related cases **missing** from the frozen sample that would change subfamily boundaries?

---

## Interim conclusion

The duplicate-key family should not be refined just to reduce `review_needed` volume.

It should only be refined if:
- at least one stable canonical subfamily becomes genuinely useful
- and replay / context-poor cases remain clearly protected

That is the standard for round 2.

## Implementation note (patterns + pipeline)

- `data/known_patterns.json` **v0.2** encodes **PAT-001A / B / C** (see file `version` and `issue_subfamily` fields).
- `src/run_pipeline.py` **v0.2** routes triage by matched sub-pattern and emits **`issue_subfamily`** in JSON output. Details: [`pipeline-v0.2.md`](pipeline-v0.2.md).
- After rerun, capture **001 / 011** watch points and A/B/C checks in [`round-2-evaluation-note-v0.1.md`](round-2-evaluation-note-v0.1.md).

## Version
v0.1.2 (working labels + v0.2 pattern/pipeline reference)
