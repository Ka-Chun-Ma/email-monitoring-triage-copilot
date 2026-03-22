# Evaluation Pass v0.1

## What this document is (and is not)

This is **not** another abstract methodology note. It connects the governance + artifact stack to **the first hands-on evaluation round**: same frozen sample, two passes (manual then MVP-assisted), comparable records.

It is meant to help you avoid two common mistakes:

| Mistake | Why it misleads |
| -------- | ---------------- |
| **“The pipeline runs, so the MVP must be valuable.”** | Runnable code proves wiring, not usefulness, safety posture, or reviewer effort reduction. |
| **“`review_needed` is high, so the system is useless.”** | High review routing can be appropriate conservatism. The question is whether the reviewer still reaches **safe first-pass triage faster**, with **clearer structure** and **honest uncertainty**—not raw label counts. |

**What to look at instead:**

- Whether the reviewer **enters safe first-pass triage faster** than pure manual handling  
- Whether **structure is easier to reuse** (grouping, families, packaging mental model)  
- Whether **uncertainty is surfaced honestly** (no false comfort from family match)  
- **Which layer deserves the next optimization** (patterns / triage policy / mapping / packaging)

---

## Recommended order (best use of your time)

1. Keep this file and the frozen sample set in `docs/` / `data/` as-is.  
2. Run **Stage A — manual baseline** on `data/sample_issues.csv` **without** pipeline output.  
3. Run the **current pipeline**: `python src/run_pipeline.py` (see [`pipeline-v0.1.md`](pipeline-v0.1.md)).  
4. Run **Stage B — MVP-assisted** review using the same rows.  
5. Record both passes in `data/sample_issues_review_sheet.csv` using [`review-sheet-guide-v0.1.md`](review-sheet-guide-v0.1.md) (short, comparable notes—not essays).  
6. Answer **one decision question** (below). That answer drives the next sprint.

---

## The one decision question for v0.1

After both stages, answer:

> **Is the largest bottleneck in v0.1 that triage policy is too conservative, or that grounded mapping is too sparse?**

| If the bottleneck is… | Reasonable next moves |
| --------------------- | --------------------- |
| **Triage too conservative** | Refine **subfamilies** and guardrails in `known_patterns.json` / triage rules; split families where one label hides multiple operational meanings. |
| **Mapping too sparse** | Expand **`kb_ticket_mapping.json`** selectively for families that are already stable; keep `do_not_apply` guards. |
| **Structure is good but packaging is still costly** | Consider **email draft scaffold** (after pattern vs mapping separation is trusted). |

You may still choose evaluation redesign if the pass is inconclusive—this question is the default fork.

---

## Purpose

This document defines the first evaluation pass for `email-monitoring-triage-copilot`.

The goal of this pass is not to prove that the system is production-ready.
The goal is to compare:

- manual baseline handling
- MVP-assisted handling

on the same fixed evaluation sample set.

This pass is intended to answer whether the current deterministic-first prototype is already useful for:
- first-pass triage
- review posture
- hint usefulness
- packaging readiness

It is also intended to reveal whether the current policy is:
- appropriately conservative
- too optimistic
- or too conservative to reduce reviewer effort

---

## Scope of this evaluation pass

This pass evaluates the current MVP behavior for:

1. family matching
2. triage label candidate generation
3. mapping readiness and grounded hint behavior
4. reviewer effort in first-pass triage
5. reviewer effort in packaging preparation

This pass does not evaluate:

- final business correctness in all real-world scenarios
- full production integration
- automated outbound actions
- UI or dashboard quality
- LLM-enhanced reasoning
- email draft generation quality beyond packaging readiness observations

---

## Fixed sample set

Use the agreed frozen sample set in:

- `data/sample_issues.csv`

Do not change the sample set during this evaluation pass.

If the sample set changes, this must be treated as a new evaluation round rather than a continuation of v0.1.

---

## Evaluation artifacts

The following artifacts are used in this pass:

- `data/sample_issues.csv`
- `data/known_patterns.json`
- `data/kb_ticket_mapping.json`
- `src/run_pipeline.py`
- `data/sample_issues_review_sheet.csv`
- `docs/success-definition.md`
- `docs/failure-modes.md`
- `docs/mvp-boundary.md`
- `docs/evaluation-sample-set.md`
- `docs/pipeline-v0.1.md`

---

## Evaluation questions

This pass is intended to answer the following questions:

### Q1. Is the current family matching useful?
Can the system correctly identify familiar issue families without collapsing distinct meanings into one safe handling path?

### Q2. Is the triage posture useful?
Does the current triage behavior help the reviewer focus faster, or does it produce too many `review_needed` outcomes to be operationally helpful?

### Q3. Are grounded hints useful?
Do the current mapping-ready outputs provide meaningful candidate references, or are they too sparse to materially help?

### Q4. Is the system failing honestly?
When the system is uncertain, does it surface uncertainty clearly instead of hiding it?

### Q5. Is the MVP already reducing effort?
Compared with the manual baseline, does the MVP reduce:
- first-pass triage effort
- packaging reconstruction effort

---

## Evaluation design

This pass has two stages:

### Stage A. Manual baseline
A reviewer handles the sample set manually without using pipeline output.

### Stage B. MVP-assisted review
The reviewer handles the same sample set using pipeline output from `src/run_pipeline.py`.

The same reviewer may perform both stages, but should record observations carefully and explicitly.

---

## Stage A. Manual baseline procedure

### Objective
Establish how much effort is required to process the sample set without MVP assistance.

### Steps
1. Open the frozen sample set.
2. Ignore pipeline output.
3. For each issue:
   - decide a broad triage posture manually
   - note whether it appears familiar or unfamiliar
   - note whether a known reference or owner would likely help
4. Manually outline how the issues would be grouped for a daily monitoring update.
5. Record:
   - approximate elapsed time
   - perceived cognitive load
   - which cases were easy
   - which cases were ambiguous
   - which cases required caution

### Record in review sheet
Use `data/sample_issues_review_sheet.csv` to capture (see [`review-sheet-guide-v0.1.md`](review-sheet-guide-v0.1.md)):
- `issue_id`
- `expected_triage_label`
- `reviewer_agrees_with_broad_category`
- `reviewer_notes`

### Manual baseline metrics to capture
At minimum record:
- total review time in minutes
- estimated packaging time in minutes
- count of cases felt immediately obvious
- count of cases felt ambiguous
- count of cases where reviewer wanted additional context before deciding

---

## Stage B. MVP-assisted review procedure

### Objective
Measure whether the MVP output reduces reviewer effort while preserving safety.

### Steps
1. Run `src/run_pipeline.py` on the frozen sample set.
2. Review the output fields for each issue:
   - `matched_family`
   - `matched_pattern_id`
   - `would_escalate_review`
   - `triage_label_candidate`
   - `related_kb_id`
   - `related_ticket_id`
   - `owner_hint`
   - `mapping_ready`
   - `missing_mapping_flag`
3. For each issue, decide:
   - whether the triage candidate is useful
   - whether the family match is helpful
   - whether the hint output is useful, weak, or misleading
   - whether the issue still needs human review
4. Record:
   - approximate elapsed time
   - perceived cognitive load
   - where the MVP clearly helped
   - where the MVP added little value
   - where the MVP may have created false comfort or confusion
5. Manually outline how the pipeline output would support packaging for a daily monitoring update.

### Record in review sheet
Use `data/sample_issues_review_sheet.csv` to capture (see [`review-sheet-guide-v0.1.md`](review-sheet-guide-v0.1.md)):
- `issue_id`
- `expected_triage_label`
- `reviewer_agrees_with_broad_category`
- `reviewer_notes`

In `reviewer_notes`, explicitly note whether MVP assistance:
- saved time
- clarified the case
- left the case unchanged
- or created confusion

### MVP-assisted metrics to capture
At minimum record:
- total review time in minutes
- estimated packaging time in minutes
- count of issues where matched family was helpful
- count of issues where triage candidate was helpful
- count of issues where mapping hint was useful
- count of issues where reviewer still needed substantial manual reasoning
- count of issues where system output felt misleading or too confident

---

## Comparison criteria

After both stages, compare the two workflows on:

### 1. Triage effort
Did MVP assistance reduce the effort needed to establish a safe first-pass triage posture?

### 2. Packaging effort
Did MVP assistance reduce the effort needed to mentally reconstruct the daily monitoring structure?

### 3. Uncertainty visibility
Did the MVP make uncertainty clearer, or did it hide ambiguity behind familiar family labels?

### 4. Hint usefulness
Did grounded hints help enough to justify their presence, even if sparse?

### 5. Safety posture
Did the MVP behave conservatively in risky or ambiguous cases?

---

## Suggested reviewer summary template

After the pass, write a short summary using this template:

### Manual baseline summary
- Total review time:
- Estimated packaging time:
- Main sources of effort:
- Most ambiguous issue types:

### MVP-assisted summary
- Total review time:
- Estimated packaging time:
- Where MVP clearly helped:
- Where MVP did not help enough:
- Where MVP may have been too conservative:
- Where MVP may have risked false comfort:

### Decision summary
- Did MVP reduce first-pass triage effort?
- Did MVP reduce packaging effort?
- Did MVP surface uncertainty honestly?
- Should the next step focus on:
  - subfamily refinement
  - mapping expansion
  - email draft scaffolding
  - evaluation redesign

---

## Pass / fail interpretation

### This evaluation pass is encouraging if:
- the reviewer experiences lower first-pass triage effort than the manual baseline
- the reviewer experiences lower packaging effort than the manual baseline
- familiar families are surfaced usefully
- risky and ambiguous cases remain visible and reviewable
- no unacceptable failure mode is observed

### This evaluation pass should trigger redesign discussion if:
- `review_needed` volume is so high that the reviewer gains little practical time savings
- matched families often fail to add useful structure
- mapping hints are too sparse to be operationally meaningful
- familiar family labels create false comfort in ambiguous cases
- reviewer effort is not materially lower than the manual baseline

---

## What not to conclude too early

Do not conclude the following from v0.1 alone:

- that the MVP is already production-ready
- that more patterns automatically mean better triage
- that more mappings automatically mean better usefulness
- that low automation rate means the design is wrong
- that conservative review routing is a failure by default

This pass is primarily about:
- safety
- usefulness
- structure
- and next-step prioritization

---

## Likely next-step decision paths

Depending on the evaluation result, use the following logic:

### If matched families help, but `review_needed` is too high
Next step: refine subfamilies, especially where one family contains multiple meanings.

### If triage is useful, but hints are too sparse
Next step: expand grounded mapping coverage selectively.

### If structure helps, but packaging is still manual-heavy
Next step: add email draft scaffolding.

### If false comfort appears in risky cases
Next step: tighten safety guardrails before adding more automation.

---

## Example filled artifacts (round 1)

Simulated pass (for structure only — replace with a human reviewer’s run):

- [`data/sample_issues_review_sheet_manual_baseline.csv`](../data/sample_issues_review_sheet_manual_baseline.csv)
- [`data/sample_issues_review_sheet_mvp_assisted.csv`](../data/sample_issues_review_sheet_mvp_assisted.csv)
- [`evaluator-summary-v0.1-round1.md`](evaluator-summary-v0.1-round1.md) (from [`evaluator-summary-template-v0.1.md`](evaluator-summary-template-v0.1.md))

---

## Decision log for v0.1 pass

Fill in after the evaluation pass:

- Evaluation date:
- Reviewer:
- Sample set version:
- Manual baseline time:
- MVP-assisted time:
- Manual packaging estimate:
- MVP-assisted packaging estimate:
- Unacceptable failures observed: yes / no
- Most useful MVP behavior:
- Least useful MVP behavior:
- Recommended next step:

---

## Version
v0.1