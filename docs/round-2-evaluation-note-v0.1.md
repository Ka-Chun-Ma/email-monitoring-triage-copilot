# Round 2 Focused Evaluation Note v0.1

**Purpose:** Record a **very small, focused rerun** after `known_patterns.json` v0.2 and `run_pipeline.py` v0.2 — not to expand scope, but to answer whether duplicate subfamily refinement is **more useful** or **only more complex**.

**Prerequisites:** Frozen `data/sample_issues.csv`; run:

```powershell
python src/run_pipeline.py
```

Compare mentally (or paste JSON) against v0.1 behavior documented in [`evaluator-summary-v0.1-round1.md`](evaluator-summary-v0.1-round1.md).

---

## Two things to watch (before you judge “accuracy”)

### 1. ISS-EVAL-011 and `context_poor_duplicate`

**Current behavior:** The row is matched by **PAT-001B-CONTEXT-POOR-DUPLICATE** (not a separate `mapping_uncertain_duplicate` pattern).

**Why this is acceptable for now:** It is a **conservative, temporary** placement to avoid **overfitting** a new subfamily on one row while the sample is small.

**Human judgment from the working note:** [`duplicate-subfamily-working-note-v0.1.md`](duplicate-subfamily-working-note-v0.1.md) also noted a **mapping-uncertain** flavor for 011.

**What to observe on rerun:** After 011 is labeled `context_poor_duplicate`, does the reviewer experience **more clarity**, or does the **mapping-uncertainty signal** get **buried**?

- **011 is not “wrong” in v0.2 — it needs observation**, not a rushed schema change.

### 2. ISS-EVAL-001 and `canonical_duplicate` → `likely_recurring`

**Round 2 attempt:** **001** moves from blanket duplicate **`review_needed`** (v0.1) toward **`likely_recurring`** when **PAT-001A** matches.

**Highest-value validation:** Not whether the code runs, but whether **001** **deserves** that narrower first-pass posture **without false comfort**.

**Do not optimize for:** overall match count or label volume.

**Do optimize for:** whether the **posture change on 001** is **worth it** operationally and safely.

---

## Checklist A — ISS-EVAL-001

| Question | Your note |
| -------- | --------- |
| Is **001** now **more reasonably** seen as `likely_recurring` (given canonical subfamily + pipeline rules)? | |
| Does anything about **001** still feel too confident for your ops context? | |
| **False-comfort check:** If someone only skimmed output, would they misunderstand risk? | |

---

## Checklist B — ISS-EVAL-006, 008, 011

| issue_id | Still `review_needed`? | Subfamily shown | Any concern? |
| -------- | ------------------------ | ----------------- | ------------ |
| ISS-EVAL-006 | | context_poor_duplicate | |
| ISS-EVAL-008 | | replay_semantic_drift_duplicate | |
| ISS-EVAL-011 | | context_poor_duplicate | (see mapping-uncertainty watch above) |

---

## Checklist C — Duplicate handling overall (v0.1 vs v0.2)

| Question | Answer (yes / partly / no) | Notes |
| -------- | -------------------------- | ----- |
| Is duplicate handling **more useful** than v0.1? | | |
| Is it **not more dangerous** than v0.1 (no new false comfort on risky rows)? | | |
| Is complexity **paid for** by clearer operational meaning? | | |

---

## The one sentence this note must answer

> **Did duplicate subfamily refinement make the system more useful, or only more complex?**

- If **more useful** → consider continued duplicate refinement or selective mapping follow-up.
- If **only more complex** → pause code churn; tighten rules, sample, or evaluation before email draft scaffold.

---

## Optional: progress framing (for portfolio / self-review)

Not for pass/fail — rough ranges only:

| Lens | Indicative range | Comment |
| ---- | ------------------ | ------- |
| Methodology / core skeleton | ~75–80% | Round 2 refinement is in code, not only docs. |
| “Looks like a product” / demo layer | ~45–50% | Rerun evidence, round 2 summary, email scaffold, presentation still open. |

---

## Decision after this note

Fill one line:

- [ ] **Continue** duplicate refinement (specify: subfamily / guards / 011 treatment)
- [ ] **Proceed** toward email draft scaffold (only if A/B/C and the one-sentence answer support it)
- [ ] **Hold** — revert or simplify (document why)

**Evaluator / date:**  
**Pipeline / patterns version used:** v0.2  

---

## Version

v0.1 (template; fill after rerun)
