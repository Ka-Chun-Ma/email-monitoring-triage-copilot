# Review Sheet Guide v0.1

## Role in the repo

This guide tells you **how to fill** `data/sample_issues_review_sheet.csv` during the first evaluation round. It is the practical companion to [`evaluation-pass-v0.1.md`](evaluation-pass-v0.1.md), which defines **manual baseline → pipeline → MVP-assisted** and the **single bottleneck question** that decides the next sprint.

The goal is **not** to make review more formal. The goal is to avoid a filled sheet that is:

- **too vague** (“looks fine” / “ok”) — no comparability  
- **too long** — indistinguishable from a full incident write-up  
- **purely subjective** — no way to compare Stage A vs Stage B  

Keep notes **short and comparable** so you can see deltas, not vibes.

---

## Purpose

This guide explains how to use `data/sample_issues_review_sheet.csv` during the first evaluation pass.

The review sheet is not a production artifact.
It is a lightweight evaluation artifact used to compare:

- manual baseline handling
- MVP-assisted handling

on the same fixed sample set.

Its purpose is to make reviewer judgment visible and comparable, not to force false precision.

---

## Review sheet file

Use:

- `data/sample_issues_review_sheet.csv`

Current minimum columns:

- `issue_id`
- `expected_triage_label`
- `reviewer_agrees_with_broad_category` (`yes` \| `no` \| `partly`)
- `reviewer_notes`

---

## Two rounds: manual baseline vs MVP-assisted

Fill the sheet **twice** for the same `issue_id` rows (same frozen `data/sample_issues.csv`):

| Round | When | What you use |
| ----- | ---- | -------------- |
| **Stage A** | Manual baseline | Issue text + CSV columns only — **no** pipeline JSON |
| **Stage B** | MVP-assisted | Same issues + `python src/run_pipeline.py` output |

**Practical options:**

1. **Two files** (recommended for clarity): copy the template to e.g. `data/sample_issues_review_sheet_manual_baseline.csv` and `data/sample_issues_review_sheet_mvp_assisted.csv`.  
2. **One file**: add a column `round` with values `manual_baseline` / `mvp_assisted`, or prefix each `reviewer_notes` line with `A:` / `B:` (only if you can keep rows legible).

Do not change `issue_id` values between rounds.

---

## What each column means

### 1. issue_id
The unique identifier of the sample issue.

Use this to match the review row back to:
- `data/sample_issues.csv`
- pipeline output
- manual notes

Do not change this value.

---

### 2. expected_triage_label
This is the reviewer's best judgment about what the safe first-pass triage should be.

Use one of:

- `likely_recurring`
- `likely_new`
- `review_needed`

This field should reflect reviewer judgment, not pipeline output copying.

### How to think about it
Ask:
- If I were handling this manually, what is the safest reasonable first-pass triage?
- Is this familiar enough to treat as likely recurring?
- Is this clearly new?
- Or is it too ambiguous to trust without review?

### Important note
This field is not asking for final business truth.
It is asking for the safest useful first-pass triage posture.

---

### 3. reviewer_agrees_with_broad_category
This indicates whether the reviewer still agrees with the sample set's current broad category label.

Use one of:

- `yes`
- `no`
- `partly`

### How to think about it
Ask:
- Does the existing `broad_category` still feel right after review?
- Is it directionally right but slightly off?
- Would I relabel this if I were curating the sample set today?

### Suggested meaning
- `yes` = the broad category still looks correct
- `partly` = the broad category is close but incomplete or too simplified
- `no` = the broad category looks wrong and should be reconsidered

### When `partly` is useful
Use `partly` when:
- the family match feels right but triage posture should differ
- the category captures the surface form but misses the risk posture
- the case sits between likely recurring and review needed

---

### 4. reviewer_notes
Use this field to record short, useful review observations.

Do not try to write long essays.
One to three short sentences is enough.

### Good things to include
- why the case feels safe or unsafe
- whether family match is useful
- whether the issue is ambiguous
- whether the pipeline output helped
- whether the hint output was useful, weak, or misleading
- whether the case should stay in the current category

### Example note styles
- "Looks like timeout family, but first production run means this should stay review_needed."
- "Family match is useful. Mapping absent feels correct."
- "Surface wording looks familiar, but ACL regression changes handling."
- "Broad category still seems correct. Pipeline helped me group this faster."

---

## How to fill the review sheet during Stage A: Manual baseline

During manual baseline:

- do not use pipeline output
- review the sample issue directly
- fill `expected_triage_label` from your own judgment
- fill `reviewer_agrees_with_broad_category`
- use `reviewer_notes` to explain uncertainty, caution, or likely grouping logic

### What to focus on
- Did the case feel familiar or unfamiliar?
- Did it feel safe to treat as recurring?
- Did it feel obviously new?
- Did it feel ambiguous but important?

---

## How to fill the review sheet during Stage B: MVP-assisted review

During MVP-assisted review:

- use the same issue rows
- review pipeline output alongside the sample issue
- update `reviewer_notes` to reflect whether the MVP output helped

### What to focus on
- Did `matched_family` help?
- Did `triage_label_candidate` feel useful?
- Did `would_escalate_review` make sense?
- Was `mapping_ready` helpful, too sparse, or misleading?
- Did the pipeline reduce effort or just restate the obvious?

### Good MVP-assisted note examples
- "Pipeline family match helped. Review_needed still appropriate."
- "Hint was grounded and useful."
- "Mapping absent is correct and safer than guessing."
- "Pipeline output added little value here because ambiguity remained unchanged."
- "This case risks false comfort if treated as standard recurring."

---

## What this review sheet is NOT for

This sheet is not for:
- forcing perfect label agreement
- pretending the reviewer always knows the final truth
- replacing detailed root-cause analysis
- recording every possible thought

It is only for making first-pass review judgment visible enough to compare:
- manual handling
- MVP-assisted handling

---

## Suggested review habits

### Keep notes short
Use short notes.
This is a comparison tool, not a full incident report.

### Prefer safety language over certainty theater
If unsure, say:
- "still ambiguous"
- "needs review"
- "family match helpful but not enough"
- "looks familiar but meaning may differ"

### Watch for false comfort
Be especially alert when:
- wording looks familiar
- family match succeeds
- but implications may differ

This is where the MVP may look helpful while still being risky.

---

## Quick examples

### Example A
Issue:
Canonical timeout threshold exceeded for a known nightly job.

Suggested review sheet:
- `expected_triage_label`: `likely_recurring`
- `reviewer_agrees_with_broad_category`: `yes`
- `reviewer_notes`: `Looks like a stable recurring timeout family case. Candidate mapping would likely help.`

### Example B
Issue:
Duplicate key violation with missing SQL context.

Suggested review sheet:
- `expected_triage_label`: `review_needed`
- `reviewer_agrees_with_broad_category`: `yes`
- `reviewer_notes`: `Family looks familiar, but context is incomplete. Not safe to treat as standard recurring.`

### Example C
Issue:
Reference file missing wording, but portal indicates upload completed.

Suggested review sheet:
- `expected_triage_label`: `review_needed`
- `reviewer_agrees_with_broad_category`: `partly`
- `reviewer_notes`: `Surface wording matches file-missing family, but implications differ. Pipeline should not create false comfort.`

### Example D
Issue:
Undocumented connector error code with no runbook entry.

Suggested review sheet:
- `expected_triage_label`: `likely_new`
- `reviewer_agrees_with_broad_category`: `yes`
- `reviewer_notes`: `Clearly unfamiliar. No grounded hint expected.`

---

## Minimum standard for a useful filled review sheet

A filled review sheet is useful if:
- every issue has an `expected_triage_label`
- every issue has a `reviewer_agrees_with_broad_category` value
- most issues have a short meaningful note
- the notes help explain where manual and MVP-assisted handling differ

---

## After both stages: evaluator summary

Consolidate findings using [`evaluator-summary-template-v0.1.md`](evaluator-summary-template-v0.1.md). A filled example (simulated round 1) is in [`evaluator-summary-v0.1-round1.md`](evaluator-summary-v0.1-round1.md).

---

## Version
v0.1