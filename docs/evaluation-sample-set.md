# Evaluation Sample Set

**Related:** MVP pass/fail criteria and Definition of Done are in [`docs/success-definition.md`](success-definition.md) (v1.2).

## Purpose
This document defines the fixed evaluation sample set used to assess whether the MVP is complete.

The goal is not to prove that the system is perfect.
The goal is to make sure the MVP is evaluated on a sample that is:
- representative enough to test the core workflow
- mixed enough to expose safety risks
- stable enough to support repeatable comparison
- small enough to review cheaply

## Evaluation principle
The sample set must be designed to test:
- structure completeness
- triage usefulness
- hint grounding integrity
- email draft consistency
- failure posture under ambiguity
- reviewer effort compared with a manual baseline

A sample set that is too clean, too small, or too biased toward known issues is not acceptable for MVP validation.

## Recommended size
The agreed sample set for MVP should contain 12 to 18 records.

This is large enough to include meaningful variety and small enough for manual review.

## CSV-first build philosophy (why the sample file leads)
The highest-leverage artifact is **`data/sample_issues.csv`**, not the JSON files.

- **Patterns should grow from real operational variation in the frozen rows**, not from imagined families written ahead of time.
- **Mappings must not precede stable pattern groups**, or you hard-code responsibility boundaries before you know what the sample actually demands.
- A good first CSV makes validation **falsifiable**: you are testing a useful triage skeleton against messy reality, not a rule set you already trained yourself to satisfy.

Version 1 of the CSV should prioritize **representativeness over completeness**. It is acceptable to be imperfect if the mix is honest.

## Required composition
The fixed evaluation sample set must include all categories below.

### 1. Known recurring issues
Purpose:
- test deterministic routing
- test grounded hint enrichment
- test whether recurring work is absorbed correctly

Recommended count:
- 5 to 6 records

Examples:
- duplicate key style validation failures
- known missing mapping cases already covered by mapping rules
- repeated monitoring workflow timeout patterns
- previously observed reference-file error families

### 2. Likely new issues
Purpose:
- test non-match behavior
- test conservative handling of unknown cases
- test whether novelty is surfaced rather than hidden

Recommended count:
- 3 to 4 records

Examples:
- unseen error phrasing
- new source system failure pattern
- new extract failure type
- unfamiliar integration problem

### 3. Ambiguous review-needed issues
Purpose:
- test uncertainty handling
- test whether the system avoids fake certainty
- test whether borderline issues remain reviewable

Recommended count:
- 3 to 4 records

Examples:
- messages partially resembling known patterns
- issues with incomplete context
- issues with conflicting signals
- repeated wording but changed operational meaning

### 4. Missing-mapping cases
Purpose:
- test whether the system explicitly flags missing grounded mappings
- test whether the system avoids inventing KB, ticket, or owner references

Recommended count:
- 1 to 2 records

Examples:
- issue_group matched but no KB/ticket/owner mapping exists
- valid pattern family without finalized ownership mapping

### 5. Safety challenge cases
Purpose:
- test dangerous edge cases
- test whether the system fails honestly
- test whether new issues are incorrectly downgraded into safe recurring

Recommended count:
- 1 to 2 records

Examples:
- message looks similar to a known issue but key token meaning has changed
- familiar module name but fundamentally different failure mode
- severity pattern clearly escalated compared with historical case
- partial token overlap that should not trigger a safe recurring label

**Why the last two categories matter most:** known recurring rows are necessary but often easy to satisfy. **Missing-mapping** and **dangerous look-alike** cases force the system to show whether it **fails conservatively and visibly** or **pretends to understand**—the difference between an honest MVP and a risky demo.

## Minimum sample quality rules
The agreed sample set should satisfy all of the following:
- includes at least one record from each required category
- includes both matched and unmatched records
- includes both straightforward and ambiguous records
- includes at least one case where a human would reasonably pause before deciding
- includes at least one case that could expose unsafe overconfidence

## Sample set fields
Each record in the evaluation sample set should include, at minimum:
- issue_id
- environment
- detected_at
- source_system
- raw_message_text
- object_affected
- module_or_domain
- severity_hint
- **broad_category** (evaluation / review only; labels one of the five composition categories above so humans can audit coverage and expected posture)

`broad_category` may stay out of the core runtime schema if you prefer, but it is valuable **now** for cross-checking agreed-sample coverage and acceptance.

Optional fields may be included if useful for manual review, but the fixed evaluation set should not depend on hidden metadata that the MVP pipeline does not receive.

## Ground truth review sheet
For evaluation, reviewers should maintain a simple review sheet with at least:
- issue_id
- expected broad category
  - known recurring
  - likely new
  - ambiguous / review-needed
  - missing-mapping
  - safety challenge
- expected concern
- manual triage notes
- manual email placement
- reviewer comments on system usefulness

The purpose of this sheet is not to force pixel-perfect accuracy.
It is to support structured comparison between manual handling and MVP-assisted handling.

## Manual baseline
The same agreed sample set must be used for both:
- manual baseline review
- MVP-assisted review

This matters because effort comparison is otherwise too subjective.

The manual baseline should capture:
- approximate time to complete first-pass triage
- approximate time to package the daily email structure
- reviewer perception of cognitive load
- reviewer perception of uncertainty handling

## MVP-assisted review
The MVP-assisted review should capture:
- approximate time to review triage output
- approximate time to refine the generated draft
- whether hints were useful, noisy, or misleading
- whether uncertainty was made visible in the right places
- whether the system reduced structure-rebuilding effort

## Suggested evaluation flow
Use the following sequence:

1. Freeze the agreed sample set.
2. Run a manual baseline on that exact sample set.
3. Run the MVP on that exact sample set.
4. Compare:
   - output completeness
   - review effort
   - email packaging effort
   - visibility of uncertainty
   - presence or absence of unacceptable failures
5. Record reviewer observations.
6. Decide pass / fail against `docs/success-definition.md`, `docs/failure-modes.md`, and `docs/mvp-boundary.md`.

## Pass interpretation
The sample set supports an MVP pass only when:
- the Definition of Done is met
- no unacceptable failure mode is observed
- reviewers find the system easier to review than rebuilding structure manually
- the system preserves caution in ambiguous or risky cases

## Fail interpretation
The sample set should trigger reconsideration if:
- many records route to `review needed` without reducing reviewer effort
- known recurring issues often fail deterministic routing
- hint enrichment is frequently absent or unusable
- generated drafts require heavy cleanup
- uncertainty is hidden or presented with misleading confidence
- safety challenge cases are treated too confidently

## Change control
Once agreed for a validation round, the evaluation sample set should remain fixed for that round.

If the sample set changes, the evaluation round should be treated as a new round rather than a continuation of the previous one.

## Canonical artifacts (agreed sample set v1)
To move from methodology to runnable, testable validation, freeze each round using these files in the repo:

| Artifact | Role |
| -------- | ---- |
| `data/sample_issues.csv` | **Source of truth** for the 12–18 acceptance rows (one row per issue). Include a `broad_category` column for human review (values aligned with this document’s categories). |
| `data/known_patterns.json` | Deterministic pattern definitions matched against normalized text (drives recurring vs new vs review). |
| `data/kb_ticket_mapping.json` | Grounded KB / ticket / owner hints keyed by pattern or group (no invented references). |

**Suggested build order:** (1) lock rows and `broad_category` in `data/sample_issues.csv`, (2) derive or align `known_patterns.json`, (3) align `kb_ticket_mapping.json` to matched groups. Until these exist, treat the sample set as **not yet frozen** for that round.

**After the CSV exists:** decide which recurring families deserve extraction into `known_patterns.json`, which rows should **deliberately remain unmatched** by v1 patterns, and which groups are stable enough to justify entries in `kb_ticket_mapping.json`. The CSV tells you what the JSON shapes must support; the reverse is not true.

## Version
v1.2