# Round 2 evaluation — mock scenarios (not real runs)

**Purpose:** Calibration only. These scenarios are **hypothetical** ways to fill [`round-2-evaluation-note-v0.2.md`](round-2-evaluation-note-v0.2.md) when **real** pipeline output differs.

**Do not** treat these as project state. For real evidence, use [`round-2-evaluation-note-v0.2-filled-actual-run.md`](round-2-evaluation-note-v0.2-filled-actual-run.md) (or your own filled note after rerun).

---

## Scenario B — “Not failure, but precision not ready” (hypothetical)

**Idea:** `001` still `review_needed` (e.g. escalate phrase fires, or canonical match not yet trusted), but **006 / 008 / 011** stay safe.

**Before / after (illustrative)**

| issue_id | v0.2 triage | Safe? | Reviewer note |
| -------- | ----------- | ----- | --------------- |
| ISS-EVAL-001 | review_needed | yes | Boundary improved conceptually; not enough to justify narrower posture yet. |
| ISS-EVAL-006 / 008 / 011 | review_needed | yes | Safety preserved. |

**Conclusion:** Option B — mixed; **continue duplicate refinement** (safety real, precision boundary still blunt).

**Decision:** [x] Continue duplicate refinement — *“Safety held, but 001 still does not support a convincingly narrower first-pass posture. Not failure — precision boundary needs work.”*

---

## Scenario C — “Fail / do not pass” (hypothetical)

**Idea:** Any of: **006 / 008 / 011** → `likely_recurring`; or **001** improvement looks **sample-hack**; or mapping looks **fabricated**; or ambiguity **hidden**.

**Conclusion:** Option C — not justified yet.

**Decision:** [x] Hold, simplify, or partially revert — *safety bar failed for this round; simplify duplicate logic before layering.*

---

## Tone guide (good vs weak notes)

| Stronger | Weaker |
| -------- | ------ |
| Narrower posture appears justified **as first-pass aid only**. | Looks good. |
| Conservative protection preserved; **no false recurring comfort**. | Seems fine. |
| Ambiguity **still visible**; placement acceptable but **not fully resolved**. | Probably okay. |

Judgment-boundary validation is **not** a vibe check.

---

## Version

v0.1
