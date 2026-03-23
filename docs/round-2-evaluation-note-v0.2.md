# Round 2 Focused Evaluation Note v0.2

**Status — template frozen:** Do not revise this document’s structure or gates. New work belongs in **generalization evidence** and filled runs, not more template churn. See [`canonical-duplicate-generalization-next-v0.1.md`](canonical-duplicate-generalization-next-v0.1.md).

**Purpose:** Record a very small, focused rerun after `data/known_patterns.json` v0.2 and `src/run_pipeline.py` v0.2.

This round is not for scope expansion.  
It is for testing **one** judgment boundary only:

> Did duplicate subfamily refinement create a **justified precision gain**, or **only add complexity**?

---

## What this note is allowed to decide

This note may conclude **only one** of:

- duplicate refinement is **directionally working** and safe enough to **keep**
- duplicate refinement **needs another pass** before any presentation-layer work
- duplicate refinement **added complexity** without enough operational gain

This note is **not** for:

- expanding KB or ticket mapping
- broadening to other families
- evaluating email draft quality
- writing portfolio progress commentary

---

## Prerequisites

**Frozen input:** `data/sample_issues.csv`

**Run:**

```powershell
python src/run_pipeline.py
```

**Comparison baseline (v0.1):** Use pipeline behavior described in [`evaluator-summary-v0.1-round1.md`](evaluator-summary-v0.1-round1.md) (duplicate rows were all `review_needed` under the single duplicate family policy).

**Do not compare only mentally.** Record the **before / after** table below for the **four duplicate rows** in scope.

**Full audit framework:** [`evaluation-pass-v0.2-round2.md`](evaluation-pass-v0.2-round2.md)

---

## Round 2 pass / fail gates

### Fail immediately if any of these happen

- **ISS-EVAL-006** is narrowed into **false recurring comfort**
- **ISS-EVAL-008** is narrowed into **false recurring comfort**
- **ISS-EVAL-011** is narrowed into **false recurring comfort**
- Any risky duplicate row gains **mapping confidence** that is **not clearly grounded**
- **ISS-EVAL-001** appears improved only because of **sample-specific handling** rather than **explainable subfamily** logic

### Positive signal only if all of these hold

- **ISS-EVAL-001** gains a **narrower** first-pass posture through **explainable** duplicate subfamily logic
- **ISS-EVAL-006**, **ISS-EVAL-008**, and **ISS-EVAL-011** remain **conservatively protected** in `review_needed`
- The refined logic is still **easy to explain** and does **not** feel patchy or brittle

### Key judgment (not failure by default)

> If after rerun **001** still cannot be safely narrowed, but **006 / 008 / 011** are all protected, **that is not a failure.**  
> It means the **safety boundary is real** and the **precision boundary is not yet sharp enough.**  
> **Next step:** continue refining duplicate — **not** email draft scaffold.

---

## The four rows in scope

This note evaluates **only**:

| issue_id |
| -------- |
| ISS-EVAL-001 |
| ISS-EVAL-006 |
| ISS-EVAL-008 |
| ISS-EVAL-011 |

### Expected human posture *before* rerun

| issue_id | Human expected posture | Why |
| -------- | ---------------------- | --- |
| ISS-EVAL-001 | Narrower recurring *may* be justified | Candidate **canonical** duplicate |
| ISS-EVAL-006 | Remain `review_needed` | Context too poor |
| ISS-EVAL-008 | Remain `review_needed` | Replay / semantic drift risk |
| ISS-EVAL-011 | Remain `review_needed` unless evidence becomes unusually strong | Context-poor and/or **mapping-uncertain** flavor |

---

## Before / after audit table

Fill **after** rerun. **v0.1** = round 1 pipeline / summary; **v0.2** = current `run_pipeline.py` + patterns v0.2.

| issue_id | v0.1 pattern | v0.2 pattern | v0.1 triage | v0.2 triage | v0.2 `would_escalate_review` | `mapping_ready` | Safe? | Reviewer note |
| -------- | ------------- | ------------ | ----------- | ----------- | ----------------------------- | ----------------- | ----- | --------------- |
| ISS-EVAL-001 | | | | | | | | |
| ISS-EVAL-006 | | | | | | | | |
| ISS-EVAL-008 | | | | | | | | |
| ISS-EVAL-011 | | | | | | | | |

**Minimum fields to copy from pipeline JSON:** `matched_family`, `matched_pattern_id`, `issue_subfamily`, `triage_label_candidate`, `would_escalate_review`, `mapping_ready`, `missing_mapping_flag`, `related_kb_id`, `related_ticket_id`, `owner_hint`

---

## Watchpoint 1 — ISS-EVAL-001

Round 2 attempts to separate a **more canonical** duplicate from the broader duplicate bucket. This is the **highest-value** judgment test in the round.

| Question | Your note |
| -------- | --------- |
| Does **001** now look more reasonably like `likely_recurring`? | |
| Is that narrower posture **explainable** from subfamily logic, not row-specific handling? | |
| If someone **skimmed** the output, would they gain **false comfort**? | |
| Is the triage change **operationally useful**, not only technically different? | |

---

## Watchpoint 2 — ISS-EVAL-006 / 008 / 011

These rows are the **safety test**. The goal is **not** to make them look smarter — it is to keep them **conservatively protected**.

| issue_id | Expected posture | Observed v0.2 triage | Observed subfamily (`issue_subfamily`) | Safe? | Concern |
| -------- | ---------------- | --------------------- | --------------------------------------- | ----- | ------- |
| ISS-EVAL-006 | `review_needed` | | | | |
| ISS-EVAL-008 | `review_needed` | | | | |
| ISS-EVAL-011 | `review_needed` | | | | |

### Special note — ISS-EVAL-011

Current round-2 design may place **011** under **`context_poor_duplicate`**. Treat this as a **testable hypothesis**, not a defended conclusion.

**This rerun must answer:**

> Does this temporary placement create **more reviewer clarity**, or does it **bury** a meaningful **mapping-uncertainty** signal?

| Outcome | Description |
| ------- | ----------- |
| **Acceptable** | 011 stays conservative; reviewer still sees ambiguity clearly; **no** false recurring comfort |
| **Concerning** | 011 looks artificially cleaner; ambiguity harder to see; mapping uncertainty **hidden** behind duplicate language |

---

## Duplicate handling overall

Answer **after** rerun.

| Question | Answer (yes / partly / no) | Notes |
| -------- | ---------------------------- | ----- |
| Is duplicate handling **more useful** than v0.1? | | |
| Is it **not more dangerous** than v0.1? | | |
| Did round 2 create **bounded precision** gain rather than broad confidence gain? | | |
| Is added subfamily logic still **explainable** in simple terms? | | |
| Does this feel like **real judgment improvement**, not a prettier relabel? | | |

---

## The one sentence this note must answer

> Did duplicate subfamily refinement make the system **more useful** in a **bounded, safety-preserving** way, or did it only make the system **more complex**?

---

## Preliminary conclusion

Choose **one** and complete.

**Option A — Directionally successful**

Round 2 appears directionally successful because **ISS-EVAL-001** gained a narrower and explainable first-pass posture, while **ISS-EVAL-006**, **ISS-EVAL-008**, and **ISS-EVAL-011** remained conservatively protected.

**Option B — Mixed, needs another refinement pass**

Round 2 improved the conceptual boundary, but the rerun did not yet produce enough reliable operational gain to justify freezing duplicate logic and moving forward.

**Option C — Not justified yet**

Round 2 added complexity without enough trustworthy judgment improvement. Duplicate handling should remain conservative until a cleaner boundary is demonstrated.

---

## Decision after this note

Fill one line and explain why.

| Choice | Why |
| ------ | --- |
| [ ] Continue duplicate refinement | |
| [ ] Proceed toward email draft scaffold | |
| [ ] Hold, simplify, or partially revert | |

---

## Evaluator metadata

| Field | Value |
| ----- | ----- |
| Evaluator | |
| Date | |
| Pipeline version | v0.2 (`src/run_pipeline.py`) |
| Patterns version | v0.2 (`data/known_patterns.json`) |

---

## Filled examples (evidence, not more template work)

- **Actual run (first evidence file):** [`round-2-evaluation-note-v0.2-filled-actual-run.md`](round-2-evaluation-note-v0.2-filled-actual-run.md) — populated from real `run_pipeline.py` output; **human reviewer** should confirm and date.
- **Mock scenarios B / C (calibration only, not real state):** [`round-2-evaluation-mock-scenarios.md`](round-2-evaluation-mock-scenarios.md)

After **your** rerun, copy the template above or edit the filled file in place — the goal is **one** auditable filled note, not endless template edits.

---

## Version

v0.2
