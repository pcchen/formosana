#!/usr/bin/env python3
"""Extract 羅馬字/漢字 pairs from kautian_詞目.csv."""

import csv
import re
import sys


def clean_hanzi(s):
    """Remove annotation markers like 【替】【白】【文】."""
    return re.sub(r'【[替白文俗]】', '', s).strip()


def extract_pairs(input_path, output_path=None):
    pairs = []
    with open(input_path, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            hanzi = clean_hanzi(row.get('漢字') or '')
            lomaji = clean_hanzi(row.get('羅馬字') or '')
            if hanzi and lomaji:
                pairs.append((lomaji, hanzi))

    if output_path:
        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['羅馬字', '漢字'])
            writer.writerows(pairs)
        print(f"Written: {output_path} ({len(pairs)} pairs)")
    else:
        for lomaji, hanzi in pairs:
            print(f"{lomaji},{hanzi}")
        print(f"\nTotal: {len(pairs)} pairs", file=sys.stderr)


if __name__ == '__main__':
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'docs_MOE/kautian_詞目.csv'
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    extract_pairs(input_file, output_file)
