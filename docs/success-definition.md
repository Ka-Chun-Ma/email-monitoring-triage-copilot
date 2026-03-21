# Success Definition

## Project
email-monitoring-triage-copilot

## One-line purpose
The system is designed to absorb repetitive consensus work so that human attention can be reserved for ambiguous, high-importance, or potentially non-routine cases.

## Problem this project is trying to solve
Daily monitoring work is repetitive, fragmented, and cognitively expensive.

The operational burden is not only detecting issues. A large part of the effort comes from:
- reading inconsistent issue messages
- deciding whether an issue is likely recurring or likely new
- finding candidate KB, ticket, and owner references
- rebuilding the same daily email structure every time
- carrying the final responsibility under uncertainty

This project exists to reduce repeated triage and packaging work without pretending that final judgment can be fully automated.

## Core hypothesis
A deterministic-first, human-in-the-loop workflow can reduce triage effort, improve output consistency, and protect expert judgment better than an AI-first or fully manual approach.

## MVP success statement
The MVP is successful if it can:
1. ingest sample monitoring issues reliably
2. normalize issue messages into a stable structure
3. produce a first-pass triage output with:
   - likely recurring
   - likely new
   - review needed
4. provide candidate KB, ticket, and owner hints when available
5. generate a consistent daily monitoring email draft scaffold
6. expose a minimal run log for review and observability

## What success does NOT require in MVP
The MVP does not need to:
- classify every issue perfectly
- automate final decisions
- send emails automatically
- update tickets automatically
- connect to internal enterprise systems
- use autonomous agents
- use multimodal understanding
- use a full RAG stack
- provide a polished UI

## Real-world value if successful
If successful, the project should:
- reduce repeated cognitive effort in first-pass triage
- reduce repeated formatting effort in daily email drafting
- make uncertainty visible instead of hidden
- improve consistency of monitoring communication
- preserve human ownership of exceptions and final calls

## Reviewer-facing success test
A human reviewer should be able to say:
- I do not need to re-invent the structure every day
- I can quickly see what is likely known, likely new, and still uncertain
- the system gives me useful hints without pretending to be authoritative
- the draft helps me review faster rather than creating extra cleanup work

## The fixed evaluation sample set must include:
- known recurring issues
- likely new issues
- ambiguous issues that should remain reviewable
- at least a small number of missing-mapping cases

## MVP acceptance criteria (Definition of Done)
The MVP is considered complete only if all criteria below are met on a fixed evaluation sample set.

**Agreed sample set:** composition and quality rules are defined in [`docs/evaluation-sample-set.md`](evaluation-sample-set.md). For each validation round, freeze the exact rows in `data/sample_issues.csv` (and keep pattern/mapping JSON in sync as described there).

### A. Input and normalization
- 100% of input records in the sample set are ingested without pipeline crash.
- 100% of ingested records produce a normalized message field.
- Source message and normalized message are both preserved for review.

### B. Triage and decision visibility
- 100% of normalized records receive exactly one triage label:
  - likely recurring
  - likely new
  - review needed
- 100% of triage results include a machine-readable reason field.
- 100% of triage results include a confidence field.
- Any record without strong deterministic support must be routed to `review needed` or low confidence.

### C. Hint enrichment integrity
- Candidate KB/ticket/owner hints are emitted only when grounded in known mappings.
- Missing mapping is explicitly flagged when no grounded mapping exists.
- If no grounded mapping exists, the system must emit an explicit missing-mapping state rather than a guessed reference.
- No fabricated references are allowed in output.

### D. Email draft quality gate
- A daily draft is generated for every successful run.
- Draft always includes these sections in this exact order:
  1. New issues
  2. Recurring issues
  3. Follow-up items
  4. Missing mappings / review needed
- Empty sections are still rendered with explicit "none" style placeholders to avoid ambiguity.

### E. Observability and auditability
- Every run outputs at least these metrics:
  - processed count
  - likely recurring count
  - likely new count
  - review needed count
  - missing mapping count
  - draft generated status
- Run output must make it possible to trace each final row back to source text and derived fields.

### F. Safety and failure posture
- No silent downgrade of genuinely new issues into safe recurring classification.
- Uncertainty is always visible in output when evidence is weak.
- System never performs autonomous external side effects such as auto-send or auto-ticket update.

## Exit decision checklist
Before declaring MVP complete, reviewers should confirm:
- [ ] All Definition of Done criteria above pass on the agreed sample set.
- [ ] No unacceptable failures from `docs/failure-modes.md` are observed.
- [ ] Scope remains within `docs/mvp-boundary.md`.
- [ ] At least one reviewer reports lower first-pass triage and email packaging effort compared with performing the same task manually on the same sample set.

## Why this reflects the AI Builder approach
This document does not start from model capability.
It starts from workflow pain, defines the success condition first, limits delegation scope, makes uncertainty visible, and requires observability before trust.

The project is intentionally designed as a deterministic-first, human-in-the-loop system.
Automation is used to absorb repetitive first-pass work, while final responsibility and ambiguous judgment remain with the human reviewer.

The system is designed to reduce consensus-style repetitive work so that human attention can be reserved for ambiguous, high-importance, or potentially non-routine cases.

This means the project is not AI-first and not demo-first.
Its intelligence comes from workflow design, schema, rules, grounded mappings, output contracts, and reviewability - not from asking a model to improvise judgment.

This reflects an AI Builder approach rather than a model-first or feature-first approach.

## Cheapest falsification signals
This MVP should be reconsidered if any of the following are observed on the agreed sample set:
- review-needed volume is so high that first-pass triage does not reduce reviewer effort
- missing-mapping volume is so high that hint enrichment provides little operational value
- known recurring issues frequently fail deterministic routing
- reviewers do not experience lower triage and packaging effort compared with the manual baseline

## Builder growth goals
This project is also successful if it helps the builder improve in these areas:
- defining workflow contracts
- separating deterministic logic from fuzzy reasoning
- designing delegation boundaries
- thinking in terms of assessment before trust
- building minimal observability before adding more autonomy
- preserving reusable playbooks for future workflow automation projects

## Version
v1.2