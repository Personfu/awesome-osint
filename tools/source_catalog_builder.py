#!/usr/bin/env python3
"""Build a clean OSINT source catalog from JSON metadata."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def render(rows: list[dict[str, Any]]) -> str:
    lines = ['# OSINT Source Catalog', '', '| Source | Category | Tier | Use | Boundary |', '|---|---|---:|---|---|']
    for row in rows:
        lines.append(
            f"| {row.get('name','unknown')} | {row.get('category','general')} | {row.get('tier','B')} | {row.get('use','research')} | {row.get('boundary','public/authorized only')} |"
        )
    lines.append('\nDefault boundary: public data, owned assets, written consent, or explicit bug bounty scope only.\n')
    return '\n'.join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description='Render an OSINT source catalog.')
    parser.add_argument('input', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    raw = json.loads(args.input.read_text(encoding='utf-8'))
    rows = raw if isinstance(raw, list) else raw.get('sources', [])
    args.output.write_text(render(rows), encoding='utf-8')
    print(f'wrote {args.output}')


if __name__ == '__main__':
    main()
