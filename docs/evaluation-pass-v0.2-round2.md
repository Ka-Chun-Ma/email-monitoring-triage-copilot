# Evaluation Pass v0.2 — Round 2 (Duplicate Refinement Judgment Test)

**Companion:** Shorter fill-in checklist: [`round-2-evaluation-note-v0.2.md`](round-2-evaluation-note-v0.2.md). First **filled** duplicate-row evidence: [`round-2-evaluation-note-v0.2-filled-actual-run.md`](round-2-evaluation-note-v0.2-filled-actual-run.md). This document is the **full audit framework** for the same pass.

---

## What this round is really for

This round is **not** for expanding scope.

It is a **focused judgment refinement** pass on one known bottleneck:

> `duplicate_key_violation` was previously too coarse to distinguish safer canonical recurring cases from cases that should remain under review.

The goal of round 2 is to test whether **duplicate subfamily refinement** improves triage **usefulness** without weakening **safety posture**.

The bottleneck is **not** “what to build next.” It is **how to prove round 2 did not only add complexity**.

---

## Current recommendation (before you rerun)

**Do not start the email draft scaffold yet.**

Email output is not unimportant — but **core value is not yet proven** on a lower layer:

> Can the system move the duplicate family from **“coarse but safe”** to **“finer but still safe”**?

If that is not stable, an email scaffold mainly **packages unstable judgment more prettily**. That raises **demo feel** and lowers **builder value**.

So this round’s success standard should be simple:

> **Bounded precision gain** on duplicate handling — **not** scope gain.

---

## Scope of this round

### In scope

- Duplicate-focused rerun on: **ISS-EVAL-001**, **006**, **008**, **011**
- Compare **round 1** (evaluator summary / v0.1 pipeline behavior) vs **round 2** (`known_patterns.json` v0.2, `run_pipeline.py` v0.2)
- Assess whether subfamily refinement creates **justified** precision gain

### Out of scope

- Expanding KB / ticket mapping coverage (except observing `mapping_ready` honestly)
- Email draft generation
- Broadening to other families beyond sanity check
- Presentation / demo layer work

---

## Round-2 design intent (patterns)

The duplicate family was refined into:

| Pattern | Subfamily | Default triage intent |
| ------- | --------- | --------------------- |
| `PAT-001A-CANONICAL-DUPLICATE` | `canonical_duplicate` | Narrower **likely_recurring** candidate (still not auto-mapping) |
| `PAT-001B-CONTEXT-POOR-DUPLICATE` | `context_poor_duplicate` | **review_needed** |
| `PAT-001C-REPLAY-SEMANTIC-DRIFT-DUPLICATE` | `replay_semantic_drift_duplicate` | **review_needed** |

**Design intent:**

- Only **canonical** may support a narrower recurring posture.
- **Context-poor** and **replay / semantic drift** stay **review_needed**.
- **Mapping readiness** stays **independent** from triage posture (no “familiar family ⇒ guessed KB”).

---

## 1) Round-2 rerun check framework (three layers)

### A. Safety non-regression (most important)

Confirm round 2 did **not** trade safety for cleverness.

**Must hold:**

- **006** must **not** be misclassified as `likely_recurring`
- **008** must **not** be misclassified as `likely_recurring`
- **011** must **not** be misclassified as `likely_recurring`
- Where context is thin, semantics drift, or mapping is uncertain → **review_needed**
- Mapping must **not** be “filled in” just because the family looks familiar

**Question this answers:** Did round 2 **preserve v0.1 safety posture** on risky duplicate rows?

### B. Narrow precision gain

**Check:**

- **001** moves from blanket **review_needed** (v0.1 duplicate policy) toward a **narrower, explainable** `likely_recurring` **because** of explicit **subfamily** match — not because of a **sample-specific hack**, and **not** by secretly **binding** triage to mapping.

**Question this answers:** Is there real **judgment gain**, not a one-off override?

### C. Complexity justification

**Ask:**

- Do **PAT-001A / B / C** make behavior **more explainable**?
- Can each subfamily say **why a row lands in that bucket**?
- Are rules still **short, stable, maintainable**?
- Did refinement add **brittle** heuristics?

**Question this answers:** Is **finer** **worth** the cost — or did complexity rise without generalization?

**Failure mode to watch:** Evaluation looks a bit better, but the system becomes **harder to maintain** and **does not generalize**.

---

## 2) How to run this pass (two layers)

### Layer 1 — Duplicate-focused micro-rerun (main stage)

Inspect **only** these four rows:

`ISS-EVAL-001`, `ISS-EVAL-006`, `ISS-EVAL-008`, `ISS-EVAL-011`

Compare **round 1 vs round 2** on (from `python src/run_pipeline.py` JSON):

| Field | Use |
| ----- | --- |
| `matched_family` | Should remain `duplicate_key_violation` for all four |
| `matched_pattern_id` | `PAT-001A` / `PAT-001B` / `PAT-001C` |
| `issue_subfamily` | `canonical_duplicate` / `context_poor_duplicate` / `replay_semantic_drift_duplicate` |
| `triage_label_candidate` | Primary judgment output |
| `would_escalate_review` | Aligns with `review_needed` |
| `mapping_ready` | Still independent; duplicate rows typically **false** in v0.2 KB |
| `missing_mapping_flag` | Honest when no grounded mapping |
| `related_kb_id`, `related_ticket_id`, `owner_hint` | Must not appear “fabricated” for duplicate |

**What matters:** Whether changes match **design intent**, not merely “fields changed.”

### Layer 2 — Full-set sanity rerun (guardrail)

Run all **12** rows once.

**Confirm:**

- Non-duplicate families (timeout, file) behave as before round 2
- No accidental regression on **005** (no match), **002/003/004/007/009/010/012**

This is **not** the main stage — it catches **side effects** from duplicate ordering or shared code paths.

---

## 3) Audit table (judgment must be auditable)

| Issue | Human expected posture | Expected subfamily behavior | Round-2 desired result | **Fail condition** |
| ----- | ------------------------ | ---------------------------- | ---------------------- | ------------------ |
| **001** | Narrower recurring *possible* | Canonical duplicate | May move to `likely_recurring`, with **explainable** match — not mapping overconfidence | Still blanket review **without** structural reason, or recurring by **hack** |
| **006** | Remain conservative | Context-poor duplicate | Stay `review_needed` | Misclassified as `likely_recurring` |
| **008** | Remain conservative | Replay / semantic-drift duplicate | Stay `review_needed` | Misclassified as `likely_recurring` |
| **011** | Remain conservative | Context-poor **or** mapping-uncertain (may stay ambiguous) | Stay `review_needed` unless evidence is unusually strong | False recurring **or** false mapping confidence |

**On 011:** It does **not** have to be forced into a perfect subfamily label. Sometimes good refinement means **knowing when not to over-classify**. If **011** still feels like **mapping-uncertain** more than a clean A/B/C hit, **conservative** is acceptable.

---

## 4) Pass criteria (three gates — no KPI theater)

### Gate 1 — Safety pass

**006 / 008 / 011** all remain **`review_needed`** with **no false grounded mapping**.

If **any** of these becomes `likely_recurring`, this round **does not pass**.

### Gate 2 — Precision pass

**001** gains a **narrower, explainable** judgment via **subfamily** match — not blanket review without reason.

If **001** still cannot be safely narrowed, that is **not automatically failure** — it may mean:

- Subfamily rules are still too weak, **or**
- Canonical definition is still unclear, **or**
- Sample is insufficient for a stable narrower recurring path

### Gate 3 — Complexity pass

You can explain each subfamily’s boundary in **short** prose — ideally **2–4 main cues** per bucket.

If the explanation needs **many patches and exceptions**, refinement is **at risk**.

---

## 5) Evaluation questions (three)

1. **Safety non-regression:** Did refinement preserve conservative handling for ambiguous duplicate cases?
2. **Precision gain:** Did refinement allow a **narrowly justified** improvement for canonical duplicate?
3. **Complexity justification:** Is new logic **explainable and bounded**, not brittle or overfit?

---

## 6) Expected behavior before rerun (design intent)

| issue_id | Expected |
| -------- | -------- |
| **ISS-EVAL-001** | Candidate for **canonical**; may move from blanket **review_needed** to narrower **likely_recurring** if match is structurally grounded (not sample hack) |
| **ISS-EVAL-006** | **review_needed** — poor context |
| **ISS-EVAL-008** | **review_needed** — semantic drift / replay |
| **ISS-EVAL-011** | **review_needed** unless evidence is unusually strong; may remain **context-poor** or **mapping-uncertain** in human language |

---

## 7) Observed round-2 behavior (fill after rerun)

Paste or summarize pipeline JSON for the four rows.

For **each** of **001 / 006 / 008 / 011**, record:

- `matched_family`
- `matched_pattern_id`
- `issue_subfamily`
- `triage_label_candidate`
- `would_escalate_review`
- `mapping_ready`
- `missing_mapping_flag`
- `related_kb_id`, `related_ticket_id`, `owner_hint`

**Date / reviewer / commit:**  

---

## 8) Assessment

### 8.1 Safety non-regression

[Did **006 / 008 / 011** stay safely under review? Any mapping leakage?]

### 8.2 Precision gain

[Did **001** gain a **justified** narrower classification via **PAT-001A**, not a hack?]

### 8.3 Complexity justification

[Are A/B/C explainable in 2–4 cues each? Any brittle patch?]

---

## 9) Preliminary conclusion (pick or adapt)

### If results align with design intent

> Round 2 appears **directionally successful**. The refinement does not over-automate ambiguous duplicate cases, while creating room for a **narrower** handling of a **more canonical** duplicate pattern. This supports **deterministic-first** and **human-in-the-loop** posture.

### If mixed

> Round 2 **improves the conceptual boundary**, but the rerun does not yet show **enough reliable gain** to justify added complexity. More refinement is needed before treating **canonical duplicate** as a **stable** narrower recurring pathway.

### If poor

> Round 2 **increased pattern complexity** without a **reliable** judgment improvement. Prefer **reverting** to the **coarser conservative** duplicate posture until a **cleaner** boundary can be defined.

---

## 10) Possible round-2 interpretation (before you fill Section 7)

### Ideal outcome

- **001** hits **PAT-001A**, `likely_recurring`, **without** overconfident mapping
- **006** hits **PAT-001B**, stays `review_needed`
- **008** hits **PAT-001C**, stays `review_needed`
- **011** stays `review_needed` (whether B or conservative fallback)

**Verdict:** Round 2 **succeeds**; consider **freezing** duplicate logic and planning the **next layer** (only if gates hold).

### Acceptable but not great

- **006 / 008 / 011** safe
- **001** still cannot be safely narrowed → stays `review_needed`

**Verdict:** Safety boundary **OK**; **precision** boundary still unclear → **continue duplicate refinement**, not email scaffold.

### Failing outcome

- Any of **006 / 008 / 011** → `likely_recurring`, **or**
- **001** improvement looks **sample-specific**, **or**
- Triage and mapping **blur** again, **or**
- Logic explodes in complexity for these four rows only

**Verdict:** **Roll back** to coarser safe duplicate posture; **redefine** canonical signals from evidence.

---

## 11) Recommended next step (choose one)

| Option | When |
| ------ | ---- |
| **Continue duplicate refinement** | **001** not stably narrowable; **011** exposes a new fuzzy edge; A/B/C still do not describe reality; rules feel like “I knew the answer, then I wrote the regex” |
| **Freeze duplicate + move toward email draft scaffold** | **Only if:** **006/008/011** protected; **001** narrow path is **credible** (not hard-coded); triage vs mapping **clear**; you can state in one sentence **where the system only assists vs where it may suggest narrower recurring** |
| **Hold / simplify** | Gates fail or complexity unjustified |

---

## 12) Builder judgment (why this project is not an “AI demo”)

The valuable question is **not** “what can the model print?”

It is: **which parts of the workflow are trustworthy enough to delegate**, and **which must stay human-owned**.

Deferring email scaffold until duplicate judgment is **honest and bounded** is a **feature** of builder discipline — not a delay.

---

## Version

v0.1
