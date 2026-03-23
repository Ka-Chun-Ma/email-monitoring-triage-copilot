# Email scaffold — checkpoint v0.1

**Status:** **Frozen** constrained presentation checkpoint. **No** change to `src/email_scaffold.py`, triage rules, or KB scope unless a **new** phase is explicitly opened.

---

## What this prototype proves

- Pipeline JSON can be turned into a **daily-style draft** that **does not** equate triage with **resolution** or **ownership**.
- **§1 / §2** carry **detail lines**; **§3** stays a **mapping-gap summary** (counts + issue IDs by subgroup) so the same rows are **not** fully repeated three times.
- **Overlap** (same issue in more than one section) is **stated**, not hidden.
- **Small** (20-row) and **volume-stress** (40-row) outputs were **skim-reviewed** enough to accept **v0.1** as a **checkpoint**, not as production mail.

---

## What it does not prove

- **Production** readiness for busy inboxes, SLAs, or unattended routing.
- **Safety** under arbitrary real-world volume, vendor wording, or schema drift (only sample + duplicated stress CSV).
- That recipients will **always** read disclaimers — **skim risk** remains a **process** and **culture** problem, not solved by layout alone.
- **Correctness** of KB mapping or **`example_issue_ids`** semantics — the scaffold only **reflects** pipeline fields.

---

## Known limitations

- **§1** label “Likely recurring” can still be **misread** if readers skim (qualifiers are in copy, not in the heading).
- **§3** at scale: long **comma-separated ID lists** become a **dense wall** — harder to scan than short samples.
- **Mapping layer quirks** (e.g. same alert text, different `issue_id`, different `mapping_ready`) surface in output as **data truth**, which can **confuse** humans comparing rows — **not** an email-scaffold bug.
- **Frozen** = no creeping “small” copy fixes without a **new** decision — avoids endless polish loops.

---

## Next possible phase (not started)

Examples only — pick **one** explicitly if/when scope expands:

- **Presentation-only:** wrap §3 IDs (e.g. one ID per line), optional max-width formatting — **still** no triage/KB change.
- **Integration:** wire scaffold output to a real mailer **behind** mandatory human send — policy, not code, in this repo.
- **Evidence:** re-run scaffold against **real** exported pipeline JSON when available — **validate** skim posture on **live-shaped** data.

---

## Version

v0.1 — checkpoint recorded; scaffold logic frozen at this milestone.
