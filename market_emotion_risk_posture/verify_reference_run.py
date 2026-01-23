"""Offline verifier for a canonized reference run.

Design goals:
- No network access.
- No SpiralBrain imports or inference.
- stdlib-only.
- Fail loudly on mismatch.

Usage:
  python verify_reference_run.py fixtures/market_emotion/reference_run

Maintainers can (re)generate the manifest:
  python verify_reference_run.py fixtures/market_emotion/reference_run --write-manifest
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Tuple


class VerificationError(RuntimeError):
    pass


@dataclass(frozen=True)
class CheckResult:
    name: str
    ok: bool
    details: str


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return _sha256_bytes(path.read_bytes())


def sha256_gzip_decompressed_bytes(path: Path) -> str:
    # Provenance contract: hash the exact UTF-8 text stored in the gz artifact.
    # This intentionally matches the run's recorded `dataset_provenance.sources.*.sha256`.
    with gzip.open(path, "rt", encoding="utf-8") as f:
        text = f.read()
    return _sha256_bytes(text.encode("utf-8"))


def canonical_json_sha256(path: Path) -> str:
    """Deterministic hash of JSON value.

    Canonicalization:
    - parse JSON
    - dump with sort_keys=True and compact separators
    - UTF-8 bytes

    NOTE: This must match the canonicalization used when the reference run was generated.
    """

    value = json.loads(path.read_text(encoding="utf-8"))
    canonical = json.dumps(
        value,
        sort_keys=True,
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")
    return _sha256_bytes(canonical)


def parse_manifest_lines(text: str) -> List[Tuple[str, str]]:
    """Parses lines like: <sha256><space><space><relpath>"""

    entries: List[Tuple[str, str]] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) < 2:
            raise VerificationError(f"Invalid manifest line: {raw_line!r}")
        sha = parts[0].lower()
        relpath = " ".join(parts[1:])
        if len(sha) != 64 or any(c not in "0123456789abcdef" for c in sha):
            raise VerificationError(f"Invalid sha256 in manifest line: {raw_line!r}")
        entries.append((sha, relpath))
    return entries


def build_manifest(root: Path) -> List[Tuple[str, str]]:
    """Build a stable manifest of all files under root (excluding VERIFY.sha256 itself)."""

    files: List[Path] = [p for p in root.rglob("*") if p.is_file()]
    files = [p for p in files if p.name != "VERIFY.sha256"]
    files.sort(key=lambda p: p.as_posix())

    entries: List[Tuple[str, str]] = []
    for path in files:
        rel = path.relative_to(root).as_posix()
        entries.append((sha256_file(path), rel))
    return entries


def write_manifest(root: Path, entries: List[Tuple[str, str]]) -> None:
    manifest_path = root / "VERIFY.sha256"
    lines = [
        "# SHA-256 manifest for fixtures/market_emotion/reference_run",
        "# Format: <sha256><space><space><relative/path>",
    ]
    for sha, rel in entries:
        lines.append(f"{sha}  {rel}")
    manifest_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def require(path: Path, what: str) -> None:
    if not path.exists():
        raise VerificationError(f"Missing {what}: {path}")


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def get_required(d: Dict[str, Any], key: str, ctx: str) -> Any:
    if key not in d:
        raise VerificationError(f"Missing key {key!r} in {ctx}")
    return d[key]


def verify_manifest(root: Path) -> List[CheckResult]:
    manifest_path = root / "VERIFY.sha256"
    require(manifest_path, "VERIFY.sha256")

    entries = parse_manifest_lines(manifest_path.read_text(encoding="utf-8"))
    if not entries:
        raise VerificationError("VERIFY.sha256 has no entries")

    results: List[CheckResult] = []
    for expected_sha, rel in entries:
        file_path = root / Path(rel)
        require(file_path, f"fixture file listed in manifest ({rel})")
        actual_sha = sha256_file(file_path)
        if actual_sha != expected_sha:
            raise VerificationError(
                f"Hash mismatch for {rel}: expected {expected_sha}, got {actual_sha}"
            )
    results.append(CheckResult("manifest_sha256", True, f"{len(entries)} files matched"))
    return results


def verify_reference_run(root: Path) -> List[CheckResult]:
    results: List[CheckResult] = []

    # 1) Manifest (hash-lock of fixture bytes)
    results.extend(verify_manifest(root))

    # 2) Summary report structure
    summary_path = root / "summary_report.json"
    require(summary_path, "summary_report.json")
    summary = load_json(summary_path)

    total_profiles = get_required(summary, "total_profiles", "summary_report.json")
    market_data_points = get_required(summary, "market_data_points", "summary_report.json")
    if total_profiles != 6:
        raise VerificationError(f"total_profiles expected 6, got {total_profiles}")
    if market_data_points != 60:
        raise VerificationError(f"market_data_points expected 60, got {market_data_points}")

    dataset_prov = get_required(summary, "dataset_provenance", "summary_report.json")
    sources = get_required(dataset_prov, "sources", "dataset_provenance")
    alignment = get_required(dataset_prov, "alignment", "dataset_provenance")
    matched_days_in_order = get_required(alignment, "matched_days_in_order", "alignment")
    if len(matched_days_in_order) != 60:
        raise VerificationError(
            f"matched_days_in_order expected length 60, got {len(matched_days_in_order)}"
        )

    # 3) Verify upstream payload hashes (decompressed bytes)
    raw_dir = root / "provenance" / "raw"
    require(raw_dir, "provenance/raw")

    for source_key, src in sources.items():
        expected_payload_sha = get_required(src, "sha256", f"sources.{source_key}")
        gz_path = raw_dir / f"{expected_payload_sha}.json.gz"
        require(gz_path, f"raw gz payload for {source_key}")
        actual_payload_sha = sha256_gzip_decompressed_bytes(gz_path)
        if actual_payload_sha != expected_payload_sha:
            raise VerificationError(
                f"Raw payload SHA mismatch for {source_key}: expected {expected_payload_sha}, got {actual_payload_sha}"
            )

    results.append(CheckResult("raw_payload_sha256", True, "all sources match"))

    # 4) Verify exact aligned model input hash
    expected_market_sha = get_required(dataset_prov, "market_data_sha256", "dataset_provenance")
    market_path = root / "provenance" / "market_data_used.json"
    require(market_path, "provenance/market_data_used.json")
    actual_market_sha = canonical_json_sha256(market_path)
    if actual_market_sha != expected_market_sha:
        raise VerificationError(
            f"market_data_used.json SHA mismatch: expected {expected_market_sha}, got {actual_market_sha}"
        )

    market_data_used = load_json(market_path)
    if not isinstance(market_data_used, list) or len(market_data_used) != 60:
        raise VerificationError(
            f"market_data_used expected list of length 60, got {type(market_data_used).__name__} length {len(market_data_used) if isinstance(market_data_used, list) else 'n/a'}"
        )

    used_days = [str(item.get("timestamp", ""))[:10] for item in market_data_used]
    if used_days != matched_days_in_order:
        raise VerificationError(
            "market_data_used timestamps do not match matched_days_in_order exactly"
        )

    results.append(CheckResult("market_data_sha256", True, expected_market_sha))

    # 5) Verify predictions + posture distributions from per-profile result files
    results_summary = get_required(summary, "results_summary", "summary_report.json")

    for profile, expected_profile_summary in results_summary.items():
        results_path = root / f"{profile}_results.json"
        require(results_path, f"{profile}_results.json")

        profile_obj = load_json(results_path)
        preds = get_required(profile_obj, "predictions", f"{results_path.name}")
        if not isinstance(preds, list):
            raise VerificationError(f"predictions must be a list in {results_path.name}")
        if len(preds) != 60:
            raise VerificationError(
                f"{results_path.name}: expected 60 predictions, got {len(preds)}"
            )

        dist = {"buy": 0, "hold": 0, "sell": 0, "error": 0}
        for p in preds:
            direction = p.get("direction")
            if direction in ("buy", "hold", "sell"):
                dist[direction] += 1
            else:
                dist["error"] += 1

        expected_dist = get_required(
            expected_profile_summary, "direction_distribution", f"results_summary.{profile}"
        )
        if dist != expected_dist:
            raise VerificationError(
                f"Direction distribution mismatch for {profile}: expected {expected_dist}, got {dist}"
            )

        # Sanity-check summary counts
        if get_required(expected_profile_summary, "error_predictions", f"results_summary.{profile}") != 0:
            raise VerificationError(f"{profile}: summary reports non-zero errors")
        if get_required(expected_profile_summary, "total_predictions", f"results_summary.{profile}") != 60:
            raise VerificationError(f"{profile}: summary total_predictions != 60")
        if get_required(expected_profile_summary, "valid_predictions", f"results_summary.{profile}") != 60:
            raise VerificationError(f"{profile}: summary valid_predictions != 60")

    results.append(CheckResult("posture_distributions", True, "all profiles match"))

    # 6) Verify global counts implied by summary
    expected_total_predictions = total_profiles * market_data_points
    # (We also effectively verified per-profile length above.)
    results.append(
        CheckResult("prediction_counts", True, f"{expected_total_predictions} predictions implied")
    )

    return results


def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(description="Verify canonized reference run offline.")
    parser.add_argument("fixture_dir", nargs='?', default='results/market_emotion_research_20260120_201255', type=str, help="Path to the reference run directory (default: results/market_emotion_research_20260120_201255)")
    parser.add_argument(
        "--write-manifest",
        action="store_true",
        help="(Maintainers) Write VERIFY.sha256 for the fixture directory.",
    )
    args = parser.parse_args(argv)

    root = Path(args.fixture_dir).resolve()
    if not root.exists():
        raise VerificationError(f"Fixture directory not found: {root}")

    if args.write_manifest:
        entries = build_manifest(root)
        write_manifest(root, entries)
        print(f"Wrote {len(entries)} entries to {root / 'VERIFY.sha256'}")
        return 0

    checks = verify_reference_run(root)
    for c in checks:
        status = "PASS" if c.ok else "FAIL"
        print(f"{status}: {c.name} - {c.details}")

    print("VERIFICATION PASSED")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except VerificationError as e:
        print(f"VERIFICATION FAILED: {e}", file=sys.stderr)
        raise SystemExit(2) from e