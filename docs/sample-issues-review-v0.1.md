# Review: `sample_issues.csv` v0.1 (pilot slice)

**Status:** design validation only — **not** yet the frozen agreed sample set for full MVP acceptance.  
**Scope:** eight-row starter (`ISS-EVAL-001` … `008`) plus guidance for upgrading to a **12-row v1 candidate** set.

## Executive judgment

v0.1 is a **valid starting point** for growing the first `known_patterns.json`, but it does **not** yet **stress-test failure posture** enough for full MVP validation. The current mix still leans slightly toward “proving the design direction” rather than “proving honest, conservative behavior under ambiguity.”

## What works well (three traits)

### 1. Intentional category mix

Distribution `known_recurring ×3`, `likely_new ×2`, `review_needed ×1`, `missing_mapping ×1`, `safety_challenge ×1` tests more than naive matching:

- how **unknown** cases are handled  
- how **missing mapping** is surfaced  
- how **false safe recurrence** is avoided  

That aligns with the project’s non-negotiables.

### 2. Strong safety challenge

`ISS-EVAL-008` is high value: surface form resembles duplicate-key recurrence, but the message states replay-specific semantics that differ from fact-table duplicate handling. It catches systems that label “duplicate key” as safe recurring without reading meaning.

**Recommendation:** keep this row in the agreed set.

### 3. Separation of pattern family vs mapping readiness

`ISS-EVAL-002` and `ISS-EVAL-007` share a **timeout** family pattern, but `007` is labeled `missing_mapping`. That validates two layers:

- pattern / family recognition  
- grounded KB / ticket / owner **separately**  

This matches the repo’s artifact order: **CSV → patterns → mapping**, not “recurring ⇒ full mapping.”

## Gaps before full agreed sample (coverage)

Treat v0.1 as **pilot slice**, not full agreed sample. Four gaps:

### 1. Too few `review_needed` rows (only one)

`review_needed` is a **core safety valve**, not edge noise. With a single row, validation mostly checks “recurring matches” and “obvious new,” not **which ambiguous cases must stay with humans**.

**Target for v1:** at least **three** `review_needed` rows, covering:

- familiar wording but **missing critical context**  
- same module/object but **clearly elevated severity**  
- **partial token overlap** with a different causal chain  

### 2. Too few `missing_mapping` rows (only one)

Honesty requires showing “matched family ≠ grounded reference.”

**Target for v1:** at least **two** `missing_mapping` rows from **different families** (e.g. timeout vs file vs duplicate-key path).

### 3. `likely_new` rows are “textbook new”

`ISS-EVAL-004` and `005` are legitimate but **obviously** new. Also add **1–2** rows that **look like** an old family but are **actually new** (false-match pressure), e.g.:

- timeout wording but **materially different** threshold or subsystem  
- duplicate-key surface form but **different object role** (replay / audit / quarantine)  
- file-missing wording but **permission / delay / partial handoff**  

### 4. Environment is all `prod`

Add **2–3** non-prod rows (`uat`, `test`, or `stage`) so evaluation is not single-track. Same message family can imply different operational posture by environment.

## Row-by-row notes (v0.1)

| ID | Verdict |
| -- | ------- |
| `ISS-EVAL-001` | Strong `known_recurring`; canonical **duplicate_key_violation** example. |
| `ISS-EVAL-002` | Strong `known_recurring`; **timeout_threshold_exceeded** family. |
| `ISS-EVAL-003` | Strong `known_recurring`; **reference_file_missing** family. |
| `ISS-EVAL-004` | Valid `likely_new`; should evolve toward a **disguised-new** variant (see CSV note). |
| `ISS-EVAL-005` | Valid `likely_new`; schema drift is typical “obvious new.” |
| `ISS-EVAL-006` | Good `review_needed`: familiar surface, insufficient context. |
| `ISS-EVAL-007` | Excellent: timeout family + **missing_mapping** separates match from mapping. |
| `ISS-EVAL-008` | High value `safety_challenge`; keep. |

## Upgrade path: 12-row v1 candidate (add four rows)

**Do not** expand to 18 yet; **add four** rows to reach **12** and **fill holes** (not uniform padding).

**Suggested v1 distribution (12 rows):**

| `broad_category` | Count |
| ---------------- | ----- |
| `known_recurring` | 3 |
| `likely_new` | 2 |
| `review_needed` | 3 |
| `missing_mapping` | 2 |
| `safety_challenge` | 2 |

**Suggested four additions:**

1. **`review_needed`** — same family wording as a recurring pattern but incomplete or **conflicting** narrative (must not be a safe automatic match).  
2. **`review_needed`** — same module/object as a known case but **severity or cause chain** clearly different.  
3. **`missing_mapping`** — second family (e.g. file or duplicate-key path) with **no grounded KB/owner yet**.  
4. **`safety_challenge` or non-prod** — second high-risk false-safe case **or** a **uat/test/stage** row to expose environment-driven posture.

## First `known_patterns.json` (from v0.1–v1 data)

Enough signal exists to draft **three** families (not a full library):

| Family | Example IDs | Note |
| ------ | ----------- | ---- |
| `duplicate_key_violation` | 001, 006, 008 | Good for **family match**, **not** for naïve “safe recurring” without extra signals (context gap + semantic drift). |
| `timeout_threshold_exceeded` | 002, 007 | Relatively stable; some rows can be deterministic recurring **plus** explicit missing-mapping handling. |
| `reference_file_missing` | 003 | Clean wording; start narrow, strengthen with more samples later. |

## `kb_ticket_mapping.json` conservatism

**Prefer early mapping** only for families that are **stable and low-ambiguity** in the sample, e.g.:

- `timeout_threshold_exceeded` (with care)  
- `reference_file_missing`  

Treat **`duplicate_key_violation`** as **mapping-conservative** until the sample proves consistent semantics: the same family already includes insufficient context and replay-style drift.

## Two layers of review data

**On `data/sample_issues.csv` (per row):** `why_this_category`, `would_match_family` — separates **family match** from triage posture (see above).

**On `data/sample_issues_review_sheet.csv` (per validation round):** minimal columns for **manual baseline vs MVP-assisted** comparison:

| Column | Purpose |
| ------ | ------- |
| `issue_id` | Join key to `sample_issues.csv` |
| `expected_triage_label` | Reviewer’s expected MVP output: `likely_recurring`, `likely_new`, or `review_needed` |
| `reviewer_agrees_with_broad_category` | `yes` / `no` — whether the row’s `broad_category` in the CSV still holds after review |
| `reviewer_notes` | Freeform: concerns, email placement, system vs manual delta |

Template: [`data/sample_issues_review_sheet.csv`](../data/sample_issues_review_sheet.csv).

## One-line summary

The best property of v0.1 is that it already forces **pattern match**, **triage judgment**, and **mapping readiness** apart — that is the builder-level move. Next: **add four rows** to make that separation **auditably** true under stress.

## Version

v0.1 (review notes; pairs with CSV v0.1 / v1 candidate process)
