<!-- Volume skim: 40 rows in data/sample_issues_larger.csv (sample_issues x2, -VOL2). Same triage rules. -->

Subject: [DRAFT - human review required] Daily monitoring triage - 2025-03-10

Action required: review all sections. Items are provisional and may appear in multiple sections.

---

**This message is a draft scaffold only.** It does **not** state final resolution, root cause, or approved action.
**Human review is mandatory** before any operational follow-up.

---

## 1 - Likely recurring (14) (triage candidate)

*Triage label `likely_recurring` from the pipeline - **not** a guarantee of recurrence or closure.*

- **ISS-EVAL-001** - module: BW DTP load; family: duplicate_key_violation; pattern: PAT-001A-CANONICAL-DUPLICATE; triage candidate: likely_recurring
- **ISS-EVAL-002** - module: Orchestrator; family: timeout_threshold_exceeded; pattern: PAT-002-TIMEOUT-THRESHOLD-FAMILY; triage candidate: likely_recurring
- **ISS-EVAL-003** - module: SFTP intake; family: reference_file_missing; pattern: PAT-003-REFERENCE-FILE-MISSING-FAMILY; triage candidate: likely_recurring
- **ISS-EVAL-007** - module: Orchestrator; family: timeout_threshold_exceeded; pattern: PAT-002-TIMEOUT-THRESHOLD-FAMILY; triage candidate: likely_recurring
- **ISS-GEN-013** - module: BW DTP load; family: duplicate_key_violation; pattern: PAT-001A-CANONICAL-DUPLICATE; triage candidate: likely_recurring
- **ISS-GEN-014** - module: BW DTP load; family: duplicate_key_violation; pattern: PAT-001A-CANONICAL-DUPLICATE; triage candidate: likely_recurring
- **ISS-GEN-017** - module: BW DTP load; family: duplicate_key_violation; pattern: PAT-001A-CANONICAL-DUPLICATE; triage candidate: likely_recurring
- **ISS-EVAL-001-VOL2** - module: BW DTP load; family: duplicate_key_violation; pattern: PAT-001A-CANONICAL-DUPLICATE; triage candidate: likely_recurring
- **ISS-EVAL-002-VOL2** - module: Orchestrator; family: timeout_threshold_exceeded; pattern: PAT-002-TIMEOUT-THRESHOLD-FAMILY; triage candidate: likely_recurring
- **ISS-EVAL-003-VOL2** - module: SFTP intake; family: reference_file_missing; pattern: PAT-003-REFERENCE-FILE-MISSING-FAMILY; triage candidate: likely_recurring
- **ISS-EVAL-007-VOL2** - module: Orchestrator; family: timeout_threshold_exceeded; pattern: PAT-002-TIMEOUT-THRESHOLD-FAMILY; triage candidate: likely_recurring
- **ISS-GEN-013-VOL2** - module: BW DTP load; family: duplicate_key_violation; pattern: PAT-001A-CANONICAL-DUPLICATE; triage candidate: likely_recurring
- **ISS-GEN-014-VOL2** - module: BW DTP load; family: duplicate_key_violation; pattern: PAT-001A-CANONICAL-DUPLICATE; triage candidate: likely_recurring
- **ISS-GEN-017-VOL2** - module: BW DTP load; family: duplicate_key_violation; pattern: PAT-001A-CANONICAL-DUPLICATE; triage candidate: likely_recurring

## 2 - Review needed (24) (human judgment required)

*Triage label `review_needed` - escalation / judgment expected before any recurring posture.*

- **ISS-EVAL-004** - module: Orchestrator; family: timeout_threshold_exceeded; pattern: PAT-002-TIMEOUT-THRESHOLD-FAMILY; triage candidate: review_needed
- **ISS-EVAL-006** - module: BW staging; family: duplicate_key_violation; pattern: PAT-001B-CONTEXT-POOR-DUPLICATE; triage candidate: review_needed
- **ISS-EVAL-008** - module: BW DTP load; family: duplicate_key_violation; pattern: PAT-001C-REPLAY-SEMANTIC-DRIFT-DUPLICATE; triage candidate: review_needed
- **ISS-EVAL-009** - module: SFTP intake; family: reference_file_missing; pattern: PAT-003-REFERENCE-FILE-MISSING-FAMILY; triage candidate: review_needed
- **ISS-EVAL-010** - module: Orchestrator; family: timeout_threshold_exceeded; pattern: PAT-002-TIMEOUT-THRESHOLD-FAMILY; triage candidate: review_needed
- **ISS-EVAL-011** - module: BW DTP load; family: duplicate_key_violation; pattern: PAT-001B-CONTEXT-POOR-DUPLICATE; triage candidate: review_needed
- **ISS-EVAL-012** - module: SFTP intake; family: reference_file_missing; pattern: PAT-003-REFERENCE-FILE-MISSING-FAMILY; triage candidate: review_needed
- **ISS-GEN-015** - module: BW staging; family: duplicate_key_violation; pattern: PAT-001B-CONTEXT-POOR-DUPLICATE; triage candidate: review_needed
- **ISS-GEN-016** - module: BW DTP load; family: duplicate_key_violation; pattern: PAT-001C-REPLAY-SEMANTIC-DRIFT-DUPLICATE; triage candidate: review_needed
- **ISS-GEN-018** - module: BW DTP load; family: duplicate_key_violation; pattern: PAT-001B-CONTEXT-POOR-DUPLICATE; triage candidate: review_needed
- **ISS-GEN-019** - module: BW DTP load; family: duplicate_key_violation; pattern: PAT-001B-CONTEXT-POOR-DUPLICATE; triage candidate: review_needed
- **ISS-GEN-020** - module: BW DTP load; family: duplicate_key_violation; pattern: PAT-001C-REPLAY-SEMANTIC-DRIFT-DUPLICATE; triage candidate: review_needed
- **ISS-EVAL-004-VOL2** - module: Orchestrator; family: timeout_threshold_exceeded; pattern: PAT-002-TIMEOUT-THRESHOLD-FAMILY; triage candidate: review_needed
- **ISS-EVAL-006-VOL2** - module: BW staging; family: duplicate_key_violation; pattern: PAT-001B-CONTEXT-POOR-DUPLICATE; triage candidate: review_needed
- **ISS-EVAL-008-VOL2** - module: BW DTP load; family: duplicate_key_violation; pattern: PAT-001C-REPLAY-SEMANTIC-DRIFT-DUPLICATE; triage candidate: review_needed
- **ISS-EVAL-009-VOL2** - module: SFTP intake; family: reference_file_missing; pattern: PAT-003-REFERENCE-FILE-MISSING-FAMILY; triage candidate: review_needed
- **ISS-EVAL-010-VOL2** - module: Orchestrator; family: timeout_threshold_exceeded; pattern: PAT-002-TIMEOUT-THRESHOLD-FAMILY; triage candidate: review_needed
- **ISS-EVAL-011-VOL2** - module: BW DTP load; family: duplicate_key_violation; pattern: PAT-001B-CONTEXT-POOR-DUPLICATE; triage candidate: review_needed
- **ISS-EVAL-012-VOL2** - module: SFTP intake; family: reference_file_missing; pattern: PAT-003-REFERENCE-FILE-MISSING-FAMILY; triage candidate: review_needed
- **ISS-GEN-015-VOL2** - module: BW staging; family: duplicate_key_violation; pattern: PAT-001B-CONTEXT-POOR-DUPLICATE; triage candidate: review_needed
- **ISS-GEN-016-VOL2** - module: BW DTP load; family: duplicate_key_violation; pattern: PAT-001C-REPLAY-SEMANTIC-DRIFT-DUPLICATE; triage candidate: review_needed
- **ISS-GEN-018-VOL2** - module: BW DTP load; family: duplicate_key_violation; pattern: PAT-001B-CONTEXT-POOR-DUPLICATE; triage candidate: review_needed
- **ISS-GEN-019-VOL2** - module: BW DTP load; family: duplicate_key_violation; pattern: PAT-001B-CONTEXT-POOR-DUPLICATE; triage candidate: review_needed
- **ISS-GEN-020-VOL2** - module: BW DTP load; family: duplicate_key_violation; pattern: PAT-001C-REPLAY-SEMANTIC-DRIFT-DUPLICATE; triage candidate: review_needed

### Unmatched / likely new (2) (still requires human review)

*No stable family match - not treated as recurring.*

- **ISS-EVAL-005** - module: API gateway; family: -; pattern: -; triage candidate: likely_new
- **ISS-EVAL-005-VOL2** - module: API gateway; family: -; pattern: -; triage candidate: likely_new

## 3 - No grounded KB / ticket / owner mapping (33)

*`missing_mapping_flag` from pipeline: matched family exists but **no** grounded KB / ticket / owner link in current mapping data. **Does not** invite automation or silent routing.*
*Below is a **summary** (same rows as in §1/§2 where applicable; IDs only, no repeated detail lines).*

**Likely recurring + missing mapping (9):** ISS-EVAL-001, ISS-EVAL-007, ISS-GEN-013, ISS-GEN-014, ISS-GEN-017, ISS-EVAL-001-VOL2, ISS-GEN-013-VOL2, ISS-GEN-014-VOL2, ISS-GEN-017-VOL2

**Review needed + missing mapping (24):** ISS-EVAL-004, ISS-EVAL-006, ISS-EVAL-008, ISS-EVAL-009, ISS-EVAL-010, ISS-EVAL-011, ISS-EVAL-012, ISS-GEN-015, ISS-GEN-016, ISS-GEN-018, ISS-GEN-019, ISS-GEN-020, ISS-EVAL-004-VOL2, ISS-EVAL-006-VOL2, ISS-EVAL-008-VOL2, ISS-EVAL-009-VOL2, ISS-EVAL-010-VOL2, ISS-EVAL-011-VOL2, ISS-EVAL-012-VOL2, ISS-GEN-015-VOL2, ISS-GEN-016-VOL2, ISS-GEN-018-VOL2, ISS-GEN-019-VOL2, ISS-GEN-020-VOL2

---

**Overlap note:** The same issue may appear in more than one section (e.g. likely recurring **and** missing mapping). That is expected; sections answer different questions.

**Stop:** Do not treat this draft as closure. Next step is always human review.
