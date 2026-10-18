#!/usr/bin/env python3
"""Deterministic half of WetLabEngine — pedagogical reconstruction.

Not UnifiedAuditEngine.py. No Gemini. No clone of Results-AI-Audit-Engine.
The posted engine (v5.7) is Colab-oriented: it hardcodes PROJECT_NAME = MECP2,
clones https://github.com/ProteinFoldingEngine/Results-AI-Audit-Engine.git,
looks for Projects/MECP2/findings.json, and exits if a Gemini key is missing.

This script is the numeric contract only. It reads a campaign findings.json
from the public tree (Labs/MECP2 or Labs/p53), ignores Colab dataset_root
paths, and scores each constraint against the tail-median of
diagnostics_timeseries.csv. PNG/PDB Git LFS files are not required.

Smoke test (Labs/MECP2): Run 5 (unrescued R106W–DNA) was contracted as
unstable (best_final_RMSD_A >= 20 Å). If the tail median is ~3 Å, the
verdict must be DEVIATION — that mismatch is the honesty check.

Original engine license: CC BY-NC-SA 4.0.
This reconstruction is offered so a researcher can rerun the scoreboard
without an API key. It is not a folding oracle.

Usage:
  python3 wetlab_deterministic_audit.py /path/to/Labs/MECP2
  python3 wetlab_deterministic_audit.py /path/to/Labs/p53 --no-smoke
"""

from __future__ import annotations

import argparse
import csv
import json
import statistics
import sys
from pathlib import Path
from typing import Any, Optional

PREFERRED_RMSD_COLS = [
    "RMSD_interface",
    "rmsd_interface",
    "RMSD",
    "rmsd",
    "Backbone_RMSD",
    "RMSD(Å)",
    "RMSD(AA)",
    "final_RMSD",
    "final_rmsd",
]


def verdict_from_constraint(
    value: Optional[float], op: str, target: float, tol: Optional[float] = None
) -> str:
    """Published v5.7 rule. INDETERMINATE if the metric is missing."""
    if value is None:
        return "INDETERMINATE"
    try:
        if value != value:  # NaN
            return "INDETERMINATE"
    except TypeError:
        return "INDETERMINATE"
    tol_val = float(tol) if tol is not None else 0.0
    target_val = float(target)
    if op == "<=":
        return "CONFIRMED" if value <= target_val + tol_val else "DEVIATION"
    if op == "<":
        return "CONFIRMED" if value < target_val + tol_val else "DEVIATION"
    if op == ">=":
        return "CONFIRMED" if value >= target_val - tol_val else "DEVIATION"
    if op == ">":
        return "CONFIRMED" if value > target_val - tol_val else "DEVIATION"
    if op in ("==", "="):
        return "CONFIRMED" if abs(value - target_val) <= tol_val else "DEVIATION"
    if op == "!=":
        return "CONFIRMED" if abs(value - target_val) > tol_val else "DEVIATION"
    return "INDETERMINATE"


def combine_verdicts(verdicts: list[str]) -> str:
    if any(v == "DEVIATION" for v in verdicts):
        return "DEVIATION"
    if verdicts and all(v == "CONFIRMED" for v in verdicts):
        return "CONFIRMED"
    return "INDETERMINATE"


def pick_rmsd_col(fieldnames: Optional[list[str]]) -> Optional[str]:
    if not fieldnames:
        return None
    lower = {name.lower(): name for name in fieldnames}
    for cand in PREFERRED_RMSD_COLS:
        if cand in fieldnames:
            return cand
        if cand.lower() in lower:
            return lower[cand.lower()]
    return None


def tail_median_rmsd(csv_path: Path) -> Optional[float]:
    """Engine rule: median of last max(100, n//10) rows, as loaded (not re-sorted)."""
    try:
        with csv_path.open(newline="") as fh:
            reader = csv.DictReader(fh)
            col = pick_rmsd_col(reader.fieldnames)
            if not col:
                return None
            values: list[float] = []
            for row in reader:
                raw = (row.get(col) or "").strip()
                if not raw:
                    continue
                try:
                    values.append(float(raw))
                except ValueError:
                    continue
    except OSError:
        return None
    if not values:
        return None
    n = len(values)
    tail_n = max(100, n // 10)
    tail = values[-tail_n:]
    return float(statistics.median(tail))


def resolve_artifact(campaign: Path, source_folder: str, rel: str) -> Optional[Path]:
    """Ignore Colab dataset_root. Prefer campaign/source_folder/path, then campaign/path."""
    if not rel:
        return None
    candidates = []
    if source_folder:
        candidates.append(campaign / source_folder / rel)
    candidates.append(campaign / rel)
    name = Path(rel).name
    if source_folder:
        candidates.append(campaign / source_folder / name)
    for p in candidates:
        if p.is_file():
            return p
    return None


def role_is_diagnostics(role: str) -> bool:
    r = (role or "").strip().lower().replace("-", "_")
    return r in {"diagnostics_csv", "diagnostics", "diagnostics_timeseries"}


def audit_campaign(campaign: Path) -> dict[str, Any]:
    findings_path = campaign / "findings.json"
    if not findings_path.is_file():
        raise FileNotFoundError(f"findings.json not found in {campaign}")
    doc = json.loads(findings_path.read_text())
    rows: list[dict[str, Any]] = []
    for finding in doc.get("findings") or []:
        run_id = finding.get("run_id")
        source_folder = finding.get("source_folder") or ""
        claim = finding.get("canonical_claim") or {}
        constraints = claim.get("constraints") or []
        artifacts = finding.get("artifacts") or []
        csv_rel = next(
            (a.get("path") for a in artifacts if role_is_diagnostics(str(a.get("role", "")))),
            None,
        )
        csv_path = resolve_artifact(campaign, source_folder, csv_rel) if csv_rel else None
        rmsd = tail_median_rmsd(csv_path) if csv_path else None
        constraint_verdicts = []
        constraint_notes = []
        for c in constraints:
            v = verdict_from_constraint(
                rmsd if c.get("metric") == "best_final_RMSD_A" else None,
                str(c.get("op", "")),
                float(c.get("value")),
                c.get("tolerance"),
            )
            constraint_verdicts.append(v)
            constraint_notes.append(
                f"{c.get('metric')} {c.get('op')} {c.get('value')}"
                + (f" ±{c.get('tolerance')}" if c.get("tolerance") is not None else "")
            )
        rows.append(
            {
                "run_id": run_id,
                "type": claim.get("type", ""),
                "rmsd": rmsd,
                "csv": str(csv_path) if csv_path else None,
                "constraints": "; ".join(constraint_notes),
                "verdict": combine_verdicts(constraint_verdicts) if constraint_verdicts else "INDETERMINATE",
            }
        )

    counts = {
        "CONFIRMED": sum(1 for r in rows if r["verdict"] == "CONFIRMED"),
        "DEVIATION": sum(1 for r in rows if r["verdict"] == "DEVIATION"),
        "INDETERMINATE": sum(1 for r in rows if r["verdict"] == "INDETERMINATE"),
    }

    thesis = ((doc.get("thesis") or {}).get("canonical_field_claim") or {})
    thesis_out: Optional[dict[str, Any]] = None
    for constraint in thesis.get("constraints") or []:
        if constraint.get("aggregation") != "count_runs_meeting":
            continue
        where = (constraint.get("where") or [{}])[0]
        meeting = 0
        for r in rows:
            if r["rmsd"] is None:
                continue
            if verdict_from_constraint(r["rmsd"], str(where.get("op")), float(where.get("value"))) == "CONFIRMED":
                meeting += 1
        thesis_out = {
            "meeting": meeting,
            "op": constraint.get("op"),
            "value": constraint.get("value"),
            "where": f"{where.get('metric')} {where.get('op')} {where.get('value')}",
            "satisfied": verdict_from_constraint(
                float(meeting), str(constraint.get("op")), float(constraint.get("value"))
            )
            == "CONFIRMED",
        }

    return {
        "schema_version": doc.get("schema_version"),
        "project": doc.get("project"),
        "n": len(rows),
        "rows": rows,
        "counts": counts,
        "thesis": thesis_out,
    }


def fmt_rmsd(v: Optional[float]) -> str:
    if v is None:
        return "—"
    return f"{v:.2f}"


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("Usage:")[0].strip())
    parser.add_argument(
        "campaign",
        nargs="?",
        default="Labs/MECP2",
        help="Campaign directory containing findings.json (default: Labs/MECP2)",
    )
    parser.add_argument(
        "--no-smoke",
        action="store_true",
        help="Do not require MECP2 Run 5 to be DEVIATION (use for Labs/p53).",
    )
    args = parser.parse_args(argv)
    campaign = Path(args.campaign).expanduser().resolve()
    if not campaign.is_dir():
        print(f"error: campaign directory not found: {campaign}", file=sys.stderr)
        print("clone https://github.com/proteinfoldingengine/WetLabEngine and pass Labs/MECP2", file=sys.stderr)
        return 2

    try:
        report = audit_campaign(campaign)
    except FileNotFoundError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2

    print(f"campaign: {campaign}")
    print(f"project:  {report['project']}")
    print(f"schema:   {report['schema_version']}")
    print(f"runs:     {report['n']}")
    print()
    print(f"{'run':<5} {'verdict':<14} {'RMSD Å':>8}  claim")
    print("-" * 72)
    for r in report["rows"]:
        print(
            f"{str(r['run_id']):<5} {r['verdict']:<14} {fmt_rmsd(r['rmsd']):>8}  {r['type']}"
        )
    print("-" * 72)
    c = report["counts"]
    print(
        f"CONFIRMED {c['CONFIRMED']}   DEVIATION {c['DEVIATION']}   INDETERMINATE {c['INDETERMINATE']}"
    )
    if report["thesis"]:
        t = report["thesis"]
        flag = "PASS" if t["satisfied"] else "FAIL"
        print(
            f"thesis count_runs_meeting ({t['where']}): {t['meeting']} {t['op']} {t['value']}  {flag}"
        )

    run5 = next((r for r in report["rows"] if r["run_id"] == 5), None)
    if args.no_smoke:
        return 0
    if run5 is None:
        print("smoke: no run_id 5 in this campaign (pass --no-smoke for p53).", file=sys.stderr)
        return 1
    if run5["verdict"] != "DEVIATION":
        print(
            f"smoke FAIL: Run 5 verdict is {run5['verdict']} (RMSD {fmt_rmsd(run5['rmsd'])} Å). "
            "Expected DEVIATION against the ≥ 20 Å instability contract.",
            file=sys.stderr,
        )
        return 1
    print(
        f"smoke PASS: Run 5 is DEVIATION "
        f"(tail-median RMSD {fmt_rmsd(run5['rmsd'])} Å vs contracted ≥ 20 Å)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
