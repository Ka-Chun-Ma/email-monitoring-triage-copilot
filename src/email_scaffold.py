#!/usr/bin/env python3
"""
email_scaffold.py v0.1 — minimal daily monitoring email draft from pipeline JSON only.

Inputs: JSON array produced by run_pipeline.py (stdout). No pattern/KB changes.

Non-goals: final resolution, automation, implied ownership, expanding mappings.

v0.1 presentation hardening: skim-resistant action line; section counts in headings.

Section 3: summary only (counts + issue IDs by subgroup) to avoid repeating full lines from §1/§2.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from typing import Any


def _comma_issue_ids(rows: list[dict[str, Any]]) -> str:
    ids = [str(r.get("issue_id") or "(no id)") for r in rows]
    return ", ".join(ids) if ids else "(none)"


def _row_line(r: dict[str, Any]) -> str:
    mid = r.get("issue_id") or "(no id)"
    mod = r.get("module_or_domain") or "-"
    fam = r.get("matched_family") or "-"
    pat = r.get("matched_pattern_id") or "-"
    tri = r.get("triage_label_candidate") or "-"
    return f"- **{mid}** - module: {mod}; family: {fam}; pattern: {pat}; triage candidate: {tri}"


def render_email_draft(rows: list[dict[str, Any]], report_date: str) -> str:
    likely_recurring = [r for r in rows if r.get("triage_label_candidate") == "likely_recurring"]
    review_needed = [r for r in rows if r.get("triage_label_candidate") == "review_needed"]
    likely_new = [r for r in rows if r.get("triage_label_candidate") == "likely_new"]
    missing_mapping = [r for r in rows if r.get("missing_mapping_flag")]
    mm_likely_recurring = [
        r for r in missing_mapping if r.get("triage_label_candidate") == "likely_recurring"
    ]
    mm_review_needed = [
        r for r in missing_mapping if r.get("triage_label_candidate") == "review_needed"
    ]

    n_lr = len(likely_recurring)
    n_rn = len(review_needed)
    n_ln = len(likely_new)
    n_mm = len(missing_mapping)

    lines: list[str] = [
        f"Subject: [DRAFT - human review required] Daily monitoring triage - {report_date}",
        "",
        "Action required: review all sections. Items are provisional and may appear in multiple sections.",
        "",
        "---",
        "",
        "**This message is a draft scaffold only.** It does **not** state final resolution, root cause, or approved action.",
        "**Human review is mandatory** before any operational follow-up.",
        "",
        "---",
        "",
        f"## 1 - Likely recurring ({n_lr}) (triage candidate)",
        "",
        "*Triage label `likely_recurring` from the pipeline - **not** a guarantee of recurrence or closure.*",
        "",
    ]
    if likely_recurring:
        lines.extend(_row_line(r) for r in likely_recurring)
    else:
        lines.append("*(none)*")

    lines.extend(
        [
            "",
            f"## 2 - Review needed ({n_rn}) (human judgment required)",
            "",
            "*Triage label `review_needed` - escalation / judgment expected before any recurring posture.*",
            "",
        ]
    )
    if review_needed:
        lines.extend(_row_line(r) for r in review_needed)
    else:
        lines.append("*(none)*")

    if likely_new:
        lines.extend(
            [
                "",
                f"### Unmatched / likely new ({n_ln}) (still requires human review)",
                "",
                "*No stable family match - not treated as recurring.*",
                "",
            ]
        )
        lines.extend(_row_line(r) for r in likely_new)

    lines.extend(
        [
            "",
            f"## 3 - No grounded KB / ticket / owner mapping ({n_mm})",
            "",
            "*`missing_mapping_flag` from pipeline: matched family exists but **no** grounded KB / ticket / owner link in current mapping data. **Does not** invite automation or silent routing.*",
            "*Below is a **summary** (same rows as in §1/§2 where applicable; IDs only, no repeated detail lines).*",
            "",
        ]
    )
    if not missing_mapping:
        lines.append("*(none)*")
    else:
        n_mm_lr = len(mm_likely_recurring)
        n_mm_rn = len(mm_review_needed)
        lines.append(
            f"**Likely recurring + missing mapping ({n_mm_lr}):** {_comma_issue_ids(mm_likely_recurring)}"
        )
        lines.append("")
        lines.append(
            f"**Review needed + missing mapping ({n_mm_rn}):** {_comma_issue_ids(mm_review_needed)}"
        )

    lines.extend(
        [
            "",
            "---",
            "",
            "**Overlap note:** The same issue may appear in more than one section (e.g. likely recurring **and** missing mapping). "
        "That is expected; sections answer different questions.",
            "",
            "**Stop:** Do not treat this draft as closure. Next step is always human review.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    p = argparse.ArgumentParser(description="Build email draft from run_pipeline.py JSON on stdin or file.")
    p.add_argument(
        "--input",
        "-i",
        type=argparse.FileType("r", encoding="utf-8"),
        default=None,
        help="JSON file (default: stdin)",
    )
    p.add_argument(
        "--date",
        type=str,
        default=None,
        help="Report date YYYY-MM-DD (default: UTC today or EMAIL_SCAFFOLD_DATE)",
    )
    args = p.parse_args()
    src = args.input if args.input is not None else sys.stdin
    raw = src.read()
    rows = json.loads(raw)
    if not isinstance(rows, list):
        print("Expected JSON array of pipeline rows.", file=sys.stderr)
        return 1
    report_date = args.date or os.environ.get("EMAIL_SCAFFOLD_DATE") or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    print(render_email_draft(rows, report_date))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
