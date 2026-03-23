#!/usr/bin/env python3
"""
run_pipeline.py v0.2 — minimal deterministic pipeline.

Three-layer flow (must stay separate):
1) Family match from known_patterns.json — pattern match != safe triage.
2) Triage posture — not every family match => likely_recurring; duplicate v0.2 uses subfamilies.
3) Grounded mapping from kb_ticket_mapping.json — family match != KB/ticket/owner.

Does not generate email drafts (see project docs).
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Any


def _norm(s: str) -> str:
    return (s or "").lower()


def _contains_any(text: str, phrases: list[str]) -> bool:
    t = _norm(text)
    return any(_norm(p) in t for p in phrases if p)


def _match_pattern(raw_message: str, pattern: dict[str, Any]) -> bool:
    rules = pattern.get("match_rules") or {}
    text = _norm(raw_message)
    exclude = rules.get("exclude_if_contains_any") or []
    if exclude and _contains_any(raw_message, exclude):
        return False
    all_of = rules.get("all_of") or []
    for phrase in all_of:
        if _norm(phrase) not in text:
            return False
    any_of = rules.get("any_of") or []
    if any_of:
        if not any(_norm(p) in text for p in any_of):
            return False
    return True


def _first_matching_pattern(raw_message: str, patterns: list[dict[str, Any]]) -> dict[str, Any] | None:
    for p in patterns:
        if _match_pattern(raw_message, p):
            return p
    return None


def _intentional_missing_issue_ids(kb: dict[str, Any]) -> dict[str, set[str]]:
    out: dict[str, set[str]] = {}
    for block in kb.get("intentional_missing_mappings", []):
        fam = block.get("issue_family")
        if not fam:
            continue
        out.setdefault(fam, set()).update(block.get("example_issue_ids") or [])
    return out


def _find_mapping_for_row(
    row: dict[str, str],
    issue_family: str | None,
    kb: dict[str, Any],
    intentional_ids: dict[str, set[str]],
    raw_message: str,
) -> dict[str, Any] | None:
    if not issue_family:
        return None
    if row.get("issue_id") in intentional_ids.get(issue_family, set()):
        return None
    for m in kb.get("mappings", []):
        if m.get("issue_family") != issue_family:
            continue
        when = m.get("applies_when") or {}
        src_ok = row.get("source_system") in (when.get("source_system_in") or [])
        mod_ok = row.get("module_or_domain") in (when.get("module_or_domain_in") or [])
        if not (src_ok and mod_ok):
            continue
        blockers = m.get("do_not_apply_if_contains_any") or []
        if blockers and _contains_any(raw_message, blockers):
            continue
        return m
    return None


def _triage_for_duplicate_v02(
    raw_message: str,
    pattern: dict[str, Any],
) -> str:
    """v0.2: PAT-001A may yield likely_recurring; 001B/001C stay review_needed per pattern defaults."""
    esc = pattern.get("escalate_to_review_if_contains_any") or []
    if esc and _contains_any(raw_message, esc):
        return "review_needed"
    default = pattern.get("recommended_default_triage") or "review_needed"
    if default in ("likely_recurring", "likely_new", "review_needed"):
        return default
    return "review_needed"


def _triage_for_timeout_v01(
    raw_message: str,
    pattern: dict[str, Any],
) -> str:
    esc = pattern.get("escalate_to_review_if_contains_any") or []
    if esc and _contains_any(raw_message, esc):
        return "review_needed"
    return "likely_recurring"


def _triage_for_file_v01(
    raw_message: str,
    pattern: dict[str, Any],
) -> str:
    esc = pattern.get("escalate_to_review_if_contains_any") or []
    if esc and _contains_any(raw_message, esc):
        return "review_needed"
    return "likely_recurring"


def run(
    sample_path: Path,
    patterns_path: Path,
    kb_path: Path,
) -> list[dict[str, Any]]:
    with patterns_path.open(encoding="utf-8") as f:
        pat_doc = json.load(f)
    with kb_path.open(encoding="utf-8") as f:
        kb_doc = json.load(f)

    patterns = pat_doc.get("patterns") or []
    intentional_ids = _intentional_missing_issue_ids(kb_doc)

    results: list[dict[str, Any]] = []
    with sample_path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            raw = row.get("raw_message_text") or ""
            issue_id = row.get("issue_id") or ""

            matched = _first_matching_pattern(raw, patterns)
            matched_family = matched["issue_family"] if matched else None
            matched_pattern_id = matched["pattern_id"] if matched else None
            issue_subfamily = matched.get("issue_subfamily") if matched else None

            would_escalate = False
            triage = "likely_new"
            if matched:
                fam = matched_family or ""
                if fam == "duplicate_key_violation":
                    triage = _triage_for_duplicate_v02(raw, matched)
                elif fam == "timeout_threshold_exceeded":
                    triage = _triage_for_timeout_v01(raw, matched)
                elif fam == "reference_file_missing":
                    triage = _triage_for_file_v01(raw, matched)
                else:
                    triage = "review_needed"
                would_escalate = triage == "review_needed"

            mapping = _find_mapping_for_row(row, matched_family, kb_doc, intentional_ids, raw)
            mapping_ready = mapping is not None

            related_kb_id = mapping.get("related_kb_id") if mapping else None
            related_ticket_id = mapping.get("related_ticket_id") if mapping else None
            owner_hint = mapping.get("owner_hint") if mapping else None

            missing_mapping_flag = bool(matched_family) and not mapping_ready

            results.append(
                {
                    "issue_id": issue_id,
                    "environment": row.get("environment"),
                    "source_system": row.get("source_system"),
                    "module_or_domain": row.get("module_or_domain"),
                    "matched_family": matched_family,
                    "issue_subfamily": issue_subfamily,
                    "matched_pattern_id": matched_pattern_id,
                    "would_escalate_review": would_escalate,
                    "triage_label_candidate": triage,
                    "related_kb_id": related_kb_id,
                    "related_ticket_id": related_ticket_id,
                    "owner_hint": owner_hint,
                    "mapping_ready": mapping_ready,
                    "missing_mapping_flag": missing_mapping_flag,
                }
            )

    return results


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    p = argparse.ArgumentParser(description="Run v0.2 family match + triage + mapping layers.")
    p.add_argument("--sample", type=Path, default=root / "data" / "sample_issues.csv")
    p.add_argument("--patterns", type=Path, default=root / "data" / "known_patterns.json")
    p.add_argument("--kb", type=Path, default=root / "data" / "kb_ticket_mapping.json")
    p.add_argument("--quiet", action="store_true", help="Suppress stderr stats")
    args = p.parse_args()

    if not args.sample.exists():
        print(f"Missing sample file: {args.sample}", file=sys.stderr)
        return 1

    out = run(args.sample, args.patterns, args.kb)
    print(json.dumps(out, indent=2, ensure_ascii=False))

    if not args.quiet:
        n = len(out)
        matched = sum(1 for r in out if r["matched_family"])
        mapping_ok = sum(1 for r in out if r["mapping_ready"])
        review = sum(1 for r in out if r["triage_label_candidate"] == "review_needed")
        print(
            f"[run_pipeline v0.2] rows={n} matched_family={matched} "
            f"mapping_ready={mapping_ok} triage_review_needed={review}",
            file=sys.stderr,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
