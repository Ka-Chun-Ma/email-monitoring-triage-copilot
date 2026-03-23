# Canonical duplicate — next validation (generalization evidence) v0.1

## Where the project is now

The **template / audit / evidence** layer for round 2 is **complete enough to freeze**:

| Artifact | Role |
| -------- | ---- |
| [`round-2-evaluation-note-v0.2.md`](round-2-evaluation-note-v0.2.md) | Focused checklist (**frozen** — structure not to be rewritten) |
| [`evaluation-pass-v0.2-round2.md`](evaluation-pass-v0.2-round2.md) | Full audit framework |
| [`round-2-evaluation-note-v0.2-filled-actual-run.md`](round-2-evaluation-note-v0.2-filled-actual-run.md) | First **filled** evidence from a real `run_pipeline.py` run |
| [`round-2-evaluation-mock-scenarios.md`](round-2-evaluation-mock-scenarios.md) | Hypothetical B/C calibration |

That is **not** “two more docs” — it is the project’s first **auditable evidence file** for duplicate refinement. **Do not keep polishing these**; move on to the next validation question.

---

## The next question (higher value than more docs)

Round 2 showed **PAT-001A / canonical_duplicate** can narrow **ISS-EVAL-001** to `likely_recurring` **without** breaking safety on **006 / 008 / 011**.

The next risk is **not** email formatting — it is **generalization**:

> Is **canonical duplicate** logic **only** working for **001**, or does it **generalize** to other **canonical-shaped** duplicate alerts?

If narrowing logic **only** fits the one row in the sample, it is **case-specific**, not a **stable** judgment boundary.

---

## Recommended next step (not email scaffold yet)

**Before** email draft scaffold:

1. Add a **small batch** of **new duplicate-like rows** (e.g. **2–4** issues) to the frozen sample or to a **sidecar CSV** used only for this experiment — same columns as `data/sample_issues.csv`, with explicit `broad_category` / `why_this_category` for human review.
2. Include **mix**:
   - **1–2** rows that **should** hit **PAT-001A** (canonical-shaped, no replay/context-poor signals) if the rule is right.
   - **1–2** rows that **should not** be narrowed (context-poor, replay drift, or mapping-uncertain) — to confirm **no regression**.
3. Run `python src/run_pipeline.py` and record outcomes using the **same** v0.2 note style (short **before/after** or **expected vs observed** table).
4. **Pass** only if: canonical candidates **consistently** hit **001A** and **stay safe**; failures go to **review_needed** or correct B/C — **without** adding one-off `issue_id` hacks in code.

---

## What this step is *not*

- Not **KB mapping expansion** for its own sake.
- Not **email draft** — that would **package** judgment before **generalization** is proven.
- Not **more template edits** to v0.2.

---

## When email scaffold becomes reasonable

Only after:

1. Round 2 **safety** holds on the **original four** duplicate rows **and**
2. **Canonical duplicate** behavior shows **generalization** beyond **001** **and**
3. Triage vs mapping separation stays **honest** in the new rows.

Then presentation layer work is **packaging a twice-validated boundary**, not **decorating a risky guess**.

---

## Version

v0.1
