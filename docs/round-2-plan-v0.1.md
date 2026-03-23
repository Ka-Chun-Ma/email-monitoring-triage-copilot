# Round 2 Plan v0.1

## What this round is really for

The most important thing about this plan is **not** “what impressive feature we add next.” It is **what single judgment boundary we refine** so the next iteration stays **tight**—like **builder iteration**, not slow **scope creep**.

Round 2 is **not expansion**. It is **precision** on the **highest-friction, highest-leverage** boundary the sample already exposed: **`duplicate_key_violation`**.

### Two mistakes this round is designed to avoid

| Trap | Why it backfires |
| ---- | ---------------- |
| **Seeing sparse mapping and rushing to add mappings** | If **triage granularity** is not stable yet, more mapping mostly creates **fake maturity**—suggestions look complete before judgment is. |
| **Seeing many `review_needed` and loosening rules** | “Relaxing” rules to reduce volume can **sink** replay / context-poor cases into **false safe recurring**—exactly what this project refuses to do. |

After patterns v0.2 + pipeline v0.2 are in place, run the **round-2 judgment test** documented in [`evaluation-pass-v0.2-round2.md`](evaluation-pass-v0.2-round2.md) (three gates, audit table, micro + full rerun). Use [`round-2-evaluation-note-v0.1.md`](round-2-evaluation-note-v0.1.md) as a short fill-in companion.

### Most natural next step (before more code)

Do **not** start with a large code change. Start with a **small human working note** that classifies duplicate rows into:

- **canonical** duplicate (stable operational meaning in context)  
- **context-poor** duplicate (familiar surface, not enough to act)  
- **replay / semantic-drift** duplicate (familiar wording, **different** operational meaning)  

Only after those labels are stable does it make sense to touch `known_patterns.json` and `run_pipeline.py`. See [`duplicate-subfamily-working-note-v0.1.md`](duplicate-subfamily-working-note-v0.1.md).

---

## Purpose

This document defines the focus of round 2 for `email-monitoring-triage-copilot`.

Round 1 showed that the current MVP is structurally useful and safety-conscious, but still too coarse in one key area:

- `duplicate_key_violation` is currently treated as a single family
- this is safe, but too blunt
- it pushes all duplicate-key cases into the same conservative posture
- this limits first-pass triage usefulness

The goal of round 2 is not to expand the entire system.
The goal is to refine one high-leverage judgment boundary.

---

## Why round 2 focuses on duplicate subfamily refinement

Round 1 evaluation suggests:

- family match, triage posture, and mapping readiness are correctly separated
- the current conservative stance is useful in ambiguous and risky cases
- the main friction is that duplicate-key cases are too broad as one family
- some duplicate-key rows may be stable enough for narrower treatment
- other duplicate-key rows clearly still require `review_needed`

This means the next highest-leverage step is:

- not broad mapping expansion
- not email draft scaffolding yet
- not more general automation

Instead, it is:
- refine `duplicate_key_violation` into smaller subfamilies
- preserve safety for replay and context-poor cases
- test whether at least one duplicate subfamily can become more operationally useful

---

## Round 2 objective

Refine the current `duplicate_key_violation` family into narrower subfamilies so that:

- clearly stable duplicate cases can be treated more usefully
- context-poor duplicate cases remain reviewable
- semantic-drift duplicate cases remain reviewable
- the system becomes less blunt without becoming unsafe

---

## Current problem statement

In v0.1:

- all duplicate-key matches are routed conservatively
- this protects against false comfort
- but it also reduces triage usefulness for canonical duplicate cases

The current family is carrying too many meanings at once:
- stable recurring-looking duplicate
- staging duplicate with insufficient context
- replay-style duplicate with changed operational meaning
- duplicate case with missing mapping readiness

This creates a valid safety posture, but a weak usefulness posture.

---

## Round 2 hypothesis

If the duplicate-key family is split into narrower subfamilies, then:

- at least one clearly canonical duplicate case may become eligible for a narrower recurring posture
- while replay-style and context-poor duplicate cases can remain safely in `review_needed`
- and overall reviewer effort may decrease without weakening the safety posture

---

## Proposed duplicate subfamilies

Round 2 should explore at least the following candidate subfamilies.

### 1. Canonical duplicate in stable load context
Characteristics:
- duplicate-key wording is canonical
- business key and target wording are present
- no replay indicators
- no missing-context indicators
- operational meaning appears stable and familiar

Potential posture:
- candidate for narrower recurring treatment
- still subject to mapping readiness rules

### 2. Context-poor or staging duplicate
Characteristics:
- duplicate-key wording present
- message lacks SQL, row-level, or sufficient source context
- staging language present
- message is familiar but not safe enough for confident routing

Potential posture:
- remain `review_needed`

### 3. Replay or semantic-drift duplicate
Characteristics:
- duplicate-key wording present
- replay, reinsert, audit, or changed logical behavior is indicated
- message looks familiar on the surface
- operational meaning is not the same as standard recurring duplicate handling

Potential posture:
- remain `review_needed`

---

## Explicit non-goals for round 2

Round 2 will NOT attempt to:

- redesign all pattern families
- expand mapping across all families
- add LLM-based triage
- introduce autonomous actions
- add email draft generation
- optimize UI or reporting layers

This round is intentionally narrow.

---

## Files expected to change

Round 2 is most likely to affect:

- `data/known_patterns.json`
- `src/run_pipeline.py`
- `data/sample_issues.csv` only if additional duplicate-focused sample rows are required
- evaluation notes or summary docs after rerun

Round 2 should avoid unnecessary changes to:
- `data/kb_ticket_mapping.json` except where duplicate refinement genuinely justifies later mapping discussion

---

## Sample impact

Round 2 should review the current duplicate-related sample rows first.

Likely relevant rows include:
- canonical duplicate-like case
- context-poor duplicate case
- replay-style duplicate case
- duplicate case with mapping ambiguity

Before adding new rows, first test whether the existing sample already supports meaningful refinement.

Add new sample rows only if:
- existing duplicate cases are insufficient to separate subfamilies cleanly
- or a missing duplicate subfamily is not represented at all

---

## Success signals for round 2

Round 2 is successful if one or more of the following becomes true without weakening safety:

### Signal 1
At least one clearly canonical duplicate row can move from blanket `review_needed` toward a narrower recurring posture.

### Signal 2
Context-poor duplicate rows still remain `review_needed`.

### Signal 3
Replay or semantic-drift duplicate rows still remain `review_needed`.

### Signal 4
Reviewer can explain the duplicate-family handling more clearly after refinement.

### Signal 5
Round 2 reduces friction in duplicate-family triage without introducing false comfort.

---

## Failure signals for round 2

Round 2 should be reconsidered if any of the following occur:

### Failure 1
Replay-style duplicate rows begin to look falsely safe.

### Failure 2
Context-poor duplicate rows are pushed out of `review_needed` without sufficient evidence.

### Failure 3
Subfamily rules become too brittle or too specific to one sample row.

### Failure 4
The refinement adds complexity without improving reviewer usefulness.

### Failure 5
Duplicate refinement creates pressure to fabricate mapping confidence that is not yet grounded.

---

## Evaluation questions for round 2

After refinement, ask:

1. Does the split make duplicate handling more useful?
2. Does it preserve caution in replay and context-poor cases?
3. Did any row become falsely comfortable?
4. Did reviewer effort actually decrease?
5. Is duplicate-family mapping still intentionally incomplete, and is that still correct?

---

## Recommended implementation order

### Step 1
Inspect current duplicate rows and assign provisional subfamily labels manually.

### Step 2
Update `known_patterns.json` to represent subfamily-level logic conservatively.

### Step 3
Update `run_pipeline.py` to route duplicate subfamilies differently where justified.

### Step 4
Re-run the frozen sample set.

### Step 5
Conduct a focused duplicate-family review.

### Step 6
Write a short round 2 evaluation note before expanding scope.

---

## Decision rule after round 2

If duplicate subfamily refinement produces:
- better usefulness
- no unacceptable safety regression
- and clearer reviewer reasoning

then the project can consider one of the following next:
- selective duplicate-family mapping discussion
- broader mapping expansion
- email draft scaffolding

If not, the project should:
- keep the safer coarse policy
- document why the refinement did not improve the design
- avoid premature expansion

---

## Summary

Round 2 is a focused judgment-refinement round.

It is not about making the system look more capable.
It is about testing whether one coarse family can be made more useful without losing honesty and safety.

That is enough for this round.

## Version
v0.1 (editorial: judgment-boundary framing and anti-patterns)