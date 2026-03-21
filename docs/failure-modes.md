# Failure Modes

## Purpose
This document defines how the MVP can fail, which failures are acceptable in early versions, and which failures are unacceptable.

The goal is not to avoid all failure.
The goal is to fail in visible, honest, and controllable ways.

## Guiding principle
A safe MVP should prefer:
- visible uncertainty over fake certainty
- review-needed over silent misclassification
- partial usefulness over misleading automation

## Acceptable failure modes in MVP
These failures are acceptable in v1 if they are visible and reviewable:

### 1. Unmatched issues
Some issues may not match any known pattern.
This is acceptable if they are clearly surfaced as likely new or review needed.

### 2. Missing mappings
Some matched issue groups may not yet have KB, ticket, or owner mappings.
This is acceptable if missing mappings are explicitly flagged.

### 3. Conservative over-escalation
Some issues may be marked as review needed even if a human later decides they are known and harmless.
This is acceptable because it protects against silent under-classification.

### 4. Imperfect candidate hints
Suggested KB, ticket, or owner hints may be incomplete or only partially useful.
This is acceptable if the output makes it clear they are candidate hints, not final truth.

### 5. Minimal observability only
The first version may only expose basic run metrics such as counts and missing mappings.
This is acceptable as long as the run is not opaque.

## Unacceptable failure modes
These failures are not acceptable even in v1.

### 1. Silent misclassification of new issues as safe recurring issues
This is the most dangerous failure.
If a genuinely new issue is treated as a known recurring issue without sufficient caution, the reviewer may miss something important.

### 2. Misleading confidence
The system must not present weak guesses as if they are reliable conclusions.
High confidence should only appear when there is strong deterministic support.

### 3. Fake precision in KB, ticket, or owner suggestions
The system must not invent authoritative-looking references that are not grounded in known mappings.

### 4. Hidden uncertainty
If there is no match, weak evidence, or missing mapping, the output must show that uncertainty.
The system must not hide ambiguity to look more complete.

### 5. Drafts that increase review burden
If the generated email draft is noisy, poorly structured, or harder to review than a manual draft, the MVP is failing its purpose.

### 6. Tight coupling between raw input and derived judgment
If the project mixes source facts with derived conclusions in ways that make review or debugging difficult, the system becomes untrustworthy.

### 7. Opaque pipeline behavior
If the reviewer cannot tell how many issues were processed, how many were matched, and where uncertainty remains, the system is too opaque for operational use.

## Failure hierarchy
Not all failures are equal.

### Highest-risk failures
- new issues silently treated as known recurring
- invented or misleading suggestions
- hidden uncertainty

### Medium-risk failures
- weak triage reasoning
- overuse of review needed
- poor grouping quality

### Lower-risk failures
- imperfect wording
- missing optional hints
- conservative defaults that require human follow-up

## Design response to failure
The MVP should respond to failure by:
- surfacing uncertainty
- writing explicit review-needed states
- flagging missing mappings
- keeping humans in the final-decision loop
- logging enough information for diagnosis

## Operational rule
When in doubt, the system should fail toward:
- review needed
- missing mapping flag
- lower confidence
- human review

It should not fail toward:
- false certainty
- hidden ambiguity
- autonomous action

## Version
v1.0