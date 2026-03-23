# Case study — email-monitoring-triage-copilot (v0.1)

**Audience:** Portfolio reviewers, hiring managers, technical peers.  
**Scope:** Describes **design and evidence** in this repository. **Frozen** implementation files are **not** modified for storytelling; this document is **packaging only**.

---

## Problem

Operations and data teams often face a **high volume** of monitoring alerts and email threads. **Surface-level similarity** (e.g. “duplicate key” wording) is easy to match; **operational meaning** (safe recurring vs. ambiguous vs. replay semantics) is not. Naive automation risks **false reassurance** — treating a familiar label as “handled” when context is missing or semantics differ.

This project asks: can we **structure triage** in a **deterministic-first**, **human-in-the-loop** way that **separates** (1) family match, (2) triage posture, and (3) grounded KB/ticket/owner mapping — without pretending that match equals resolution?

---

## Deterministic-first design

The pipeline (`src/run_pipeline.py`) implements a **three-layer** flow:

1. **Family match** — `data/known_patterns.json` (rule-based, auditable).
2. **Triage candidate** — not every family match implies `likely_recurring`; safety and review paths stay explicit.
3. **Grounded mapping** — `data/kb_ticket_mapping.json`; family match **does not** automatically yield KB/ticket/owner; **missing mapping** is an honest output.

JSON output is **stable** for the **evaluation and scaffold flows** used in this repository, **without** mixing layers.

---

## Round 2 — duplicate refinement

The **`duplicate_key_violation`** family was split into **sub-patterns** (v0.2): canonical vs. context-poor vs. replay/semantic drift (`PAT-001A`–`PAT-001C`). The goal was **precision** on a high-friction boundary, **not** maximizing automated closure.

Evaluation artifacts (template **frozen** after use) include:

- [`round-2-evaluation-note-v0.2.md`](round-2-evaluation-note-v0.2.md) — focused checklist  
- [`evaluation-pass-v0.2-round2.md`](evaluation-pass-v0.2-round2.md) — full audit framework  
- [`round-2-evaluation-note-v0.2-filled-actual-run.md`](round-2-evaluation-note-v0.2-filled-actual-run.md) — filled evidence from a real pipeline run  

---

## Generalization evidence

Beyond the fixed evaluation sample, **additional duplicate-like rows** were added to test whether **canonical** duplicate logic (**PAT-001A**) **generalizes** — not only for a single row.

- [`canonical-duplicate-generalization-batch-v0.1-evidence.md`](canonical-duplicate-generalization-batch-v0.1-evidence.md)  
- [`canonical-duplicate-generalization-batch-v0.2-boundary-evidence.md`](canonical-duplicate-generalization-batch-v0.2-boundary-evidence.md)  

Procedure and framing: [`canonical-duplicate-generalization-next-v0.1.md`](canonical-duplicate-generalization-next-v0.1.md).

---

## Constrained email scaffold

A **presentation-only** generator (`src/email_scaffold.py`, **checkpoint frozen**) consumes **pipeline JSON only**. It emits a **draft** email with:

- **§1** — likely recurring (detail lines; **not** final resolution)  
- **§2** — review needed + unmatched / likely new  
- **§3** — **summary** of mapping gaps (counts + issue IDs by subgroup), not a full repeat of §1/§2  

Disclaimers emphasize **human review** and **no** implied closure. Sample outputs: [`email-scaffold-sample-output-v0.1.md`](email-scaffold-sample-output-v0.1.md), [`email-scaffold-larger-output-v0.1.md`](email-scaffold-larger-output-v0.1.md).

---

## Frozen checkpoint

[`email-scaffold-checkpoint-v0.1.md`](email-scaffold-checkpoint-v0.1.md) records **what the scaffold proves**, **what it does not prove**, **limitations**, and **possible future phases**. The checkpoint **closes** casual churn on scaffold logic until a **new** phase is explicitly opened.

---

## Resume-ready summary (snippet)

Copy or adapt (1–2 sentences + bullets for a resume or LinkedIn **Projects** line):

**email-monitoring-triage-copilot** — Built a **deterministic-first**, **human-in-the-loop** triage **prototype** in Python, separating **pattern match**, **triage posture**, and **grounded KB mapping** for monitoring-style alerts. Led **round-2** refinement of **duplicate-key** handling (canonical vs. context-poor vs. replay semantics) with **auditable evaluation gates** and **generalization evidence**; shipped a **frozen** **email draft scaffold** that surfaces recurring vs. review vs. mapping gaps **without** implying resolution.

- Three-layer pipeline (JSON); conservative KB mapping; explicit `missing_mapping`  
- Duplicate subfamilies (v0.2) + generalization batches + frozen evaluation templates  
- Email scaffold (v0.1 checkpoint): review-first copy, §3 mapping-gap summary  

---

## Version

v0.1 — portfolio case study (**Phase 6 — packaging**); narrative only; implementation unchanged.
