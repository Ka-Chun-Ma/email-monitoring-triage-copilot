# Sample issues workflow (CSV → patterns → mapping)

This document is the **operational playbook** for building `data/sample_issues.csv` v1 and only then deriving JSON artifacts. It complements [`docs/evaluation-sample-set.md`](evaluation-sample-set.md).

## Core principle

You are not merely “preparing data for the system.” You are using the sample to answer:

> Which operational judgments are stable enough to delegate, and which are not?

---

## Step 1 — `data/sample_issues.csv` v1

**Goal:** strong representativeness, not perfection.

- **Pilot (v0.1):** **8 rows** (fast feedback on schema and mix).  
- **v1 agreed candidate:** **12 rows** with the distribution below (stress-test failure posture before freezing).  
- **Full validation round:** up to **12–15 rows** (avoid jumping to 18 in the first pass; **review quality beats count**).

### Required columns

| Column | Notes |
| ------ | ----- |
| `issue_id` | Stable identifier |
| `environment` | e.g. prod / nonprod |
| `detected_at` | ISO-8601 timestamp |
| `source_system` | Originating system or job family |
| `raw_message_text` | Verbatim or faithfully copied alert body |
| `object_affected` | Table, job, file, or object name |
| `module_or_domain` | Area (ETL, orchestrator, API, etc.) |
| `severity_hint` | As emitted by source (do not “fix” it in the CSV) |
| `broad_category` | **Evaluation-only** label (see enum below) |
| `why_this_category` | Short human rationale for the chosen `broad_category` (evaluation / review). |
| `would_match_family` | `yes` / `no` / `maybe` — whether the row would match a **pattern family** (not the same as final triage label or mapping readiness). |

These two columns separate **family match**, **triage posture**, and **mapping readiness** before you encode rules in JSON.

### `broad_category` enum (v1)

Use **only** these five values:

| Value | Meaning |
| ----- | ------- |
| `known_recurring` | Stable recurring family; wording/object/module should support deterministic patterns |
| `likely_new` | Novel phrasing or first-time failure; expect non-match or conservative handling |
| `review_needed` | Ambiguous; human would hesitate; **do not** force into a pattern early |
| `missing_mapping` | Family may be recognizable, but **no grounded KB/ticket/owner** yet (not the same as “unknown issue”) |
| `safety_challenge` | Look-alike to a known family but **different meaning or risk**; tests honest failure vs false confidence |

**Important:** `broad_category` is **evaluation scaffolding**, not production ground truth. It must not hard-code final triage logic.

### First batch of 8 rows (recommended distribution)

| Category | Count |
| -------- | ----- |
| `known_recurring` | 3 |
| `likely_new` | 2 |
| `review_needed` | 1 |
| `missing_mapping` | 1 |
| `safety_challenge` | 1 |

This mix surfaces schema friction early and stresses the **last two categories**, which decide whether the system is **safely honest**.

The repo ships **`data/sample_issues.csv`** as a **v1 candidate (12 rows)**; replace with your real alerts before calling it the agreed sample set.

### v1 candidate: 12-row target distribution

| Category | Count |
| -------- | ----- |
| `known_recurring` | 3 |
| `likely_new` | 2 |
| `review_needed` | 3 |
| `missing_mapping` | 2 |
| `safety_challenge` | 2 |

Include **2–3 non-prod** environments (`uat`, `test`, or `stage`) where possible. Rationale and gap analysis: [`docs/sample-issues-review-v0.1.md`](sample-issues-review-v0.1.md).

---

## Step 2 — Human review before rules

After the CSV is filled, answer **three questions** for each row or cluster:

1. **Known recurring:** Do these rows really look recurring? Are wording, object, and module **stable enough** to extract a pattern?
2. **Likely new:** Which of these are **dangerously similar** to a known issue? (Future false-match risk.)
3. **Your own hesitation:** Which cases would you **not** want the system to decide early? → Those belong in `review_needed`, not forced into `known_recurring`.

This is **pre-pattern human judgment labeling**, not passive data entry.

---

## Step 3 — Derive `known_patterns.json` from the CSV

- Do **not** aim for a complete pattern library in v1.
- **First version:** only **4–6 pattern families** that are the **most stable** recurring families seen in the sample.

Examples of families that often qualify (if your sample supports them):

- Duplicate key / duplicate business key  
- File not found / missing inbound file  
- Timeout / watchdog termination  
- Null / required field validation  
- Lock / refresh contention (only if wording is stable in your data)

### Do **not** put into patterns (v1)

- Highly variable wording  
- Needs heavy background context  
- You would still hesitate when reading it  
- Anything that could **eat genuinely new issues**

**Rule of thumb:** the pattern layer only consumes **high consensus, low ambiguity** families matchable by exact or near-exact rules—aligned with **deterministic-first**.

---

## Step 4 — Last: `kb_ticket_mapping.json`

This file should be **more conservative** than `known_patterns.json`.

- Not every pattern deserves a mapping in v1.
- Only add mappings for issue groups you believe are **stable enough** to ground hints.

### First-version fields only

Keep v1 small:

| Field | Purpose |
| ----- | ------- |
| `related_kb_id` | Grounded KB reference |
| `related_ticket_id` | Grounded ticket reference |
| `owner_hint` | Grounded owner or team hint |

**Defer** auto follow-up scripts, escalation logic, resolution recommendations, priority scores—those invite **premature completeness** and fake maturity.

---

## Three pitfalls to avoid

1. **Writing patterns before locking the sample** — patterns become imagined rules, not extracted workflow.  
2. **Treating `broad_category` as final triage truth** — it is for evaluation and review alignment only.  
3. **Filling mappings early** — sparse and honest beats “looks complete.”

---

## What “done” looks like for CSV v1

When you read the 12–15 (or first 8) rows, you can state clearly:

- Which rows **should** be handled deterministically in v1  
- Which should **deliberately not** be pattern-matched yet  
- Which are **missing mapping** vs **unknown / new**  
- Which rows are **safety tests** for look-alike risk  

If that is clear, the JSON artifacts **follow naturally**.

---

## Review sheet (manual baseline / MVP-assisted)

Use [`data/sample_issues_review_sheet.csv`](../data/sample_issues_review_sheet.csv) each time you run a **manual baseline** or **MVP-assisted** pass on the agreed sample:

| Column | Values / notes |
| ------ | -------------- |
| `issue_id` | Matches `sample_issues.csv` |
| `expected_triage_label` | `likely_recurring` \| `likely_new` \| `review_needed` (MVP triage contract) |
| `reviewer_agrees_with_broad_category` | `yes` \| `no` |
| `reviewer_notes` | Freeform comparison notes |

Keep **`broad_category`** and **`why_this_category` / `would_match_family`** on `sample_issues.csv`; use the review sheet for **per-round** human agreement and notes.

After `known_patterns.json` and `kb_ticket_mapping.json` v0.1 exist, validate the split with [`docs/pipeline-v0.1.md`](pipeline-v0.1.md) and `python src/run_pipeline.py`.

---

## Version

v1.2
