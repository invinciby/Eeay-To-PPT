#!/usr/bin/env python3
"""Validate an Easy-To-PPT Markdown production pack.

This is a lightweight structural check. It does not judge content quality.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


REQUIRED_SECTIONS = [
    "Page Role",
    "Core Point",
    "Source Basis",
    "Page Content",
    "Suggested Visual",
    "Required Images",
]


def split_slides(text: str) -> list[tuple[int, str, str]]:
    pattern = re.compile(r"(?m)^##\s+Slide\s+(\d+)\s*:\s*(.+?)\s*$")
    matches = list(pattern.finditer(text))
    slides: list[tuple[int, str, str]] = []
    for idx, match in enumerate(matches):
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        slides.append((int(match.group(1)), match.group(2).strip(), text[start:end]))
    return slides


def section_present(body: str, section: str) -> bool:
    return bool(re.search(rf"(?m)^###\s+{re.escape(section)}\s*$", body))


def validate(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    errors: list[dict] = []
    warnings: list[dict] = []

    if not re.search(r"(?m)^#\s+.+", text):
        errors.append({"rule": "missing_deck_title", "detail": "Missing top-level deck title."})

    if "## Deck Metadata" not in text:
        warnings.append({"rule": "missing_deck_metadata", "detail": "Deck Metadata section is recommended."})

    slides = split_slides(text)
    if not slides:
        errors.append({"rule": "missing_slides", "detail": "No slide sections found. Expected headings like `## Slide 1: Title`."})

    seen_numbers: set[int] = set()
    for number, title, body in slides:
        if number in seen_numbers:
            errors.append({"rule": "duplicate_slide_number", "slide": number, "detail": "Slide number appears more than once."})
        seen_numbers.add(number)
        if not title:
            errors.append({"rule": "missing_slide_title", "slide": number, "detail": "Slide title is empty."})
        for section in REQUIRED_SECTIONS:
            if not section_present(body, section):
                errors.append({
                    "rule": "missing_required_section",
                    "slide": number,
                    "section": section,
                    "detail": f"Missing `### {section}`.",
                })
        if re.search(r"(?i)\b(TBD|TODO|待补充)\b", body):
            warnings.append({"rule": "placeholder_text", "slide": number, "detail": "Slide contains placeholder text."})

    expected = list(range(1, len(slides) + 1))
    actual = [number for number, _, _ in slides]
    if actual and actual != expected:
        warnings.append({
            "rule": "non_contiguous_slide_numbers",
            "detail": f"Expected contiguous slide numbers {expected}, got {actual}.",
        })

    return {
        "path": str(path),
        "slide_count": len(slides),
        "passed": not errors,
        "errors": errors,
        "warnings": warnings,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate an Easy-To-PPT Markdown production pack.")
    parser.add_argument("path", help="Path to production-pack Markdown file.")
    parser.add_argument("--out", help="Optional JSON report path.")
    args = parser.parse_args()

    report = validate(Path(args.path))
    payload = json.dumps(report, ensure_ascii=False, indent=2)
    if args.out:
        Path(args.out).write_text(payload + "\n", encoding="utf-8")
    print(payload)
    raise SystemExit(0 if report["passed"] else 1)


if __name__ == "__main__":
    main()
