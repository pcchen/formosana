#!/usr/bin/env python3
"""Convert an ODS file to CSV, one CSV file per sheet."""

import csv
import sys
from pathlib import Path

from odf.opendocument import load
from odf.table import Table, TableRow, TableCell
from odf.text import P


def get_cell_text(cell):
    """Extract text content from a table cell."""
    parts = []
    for p in cell.getElementsByType(P):
        # Get all text content including nested elements
        text = ''
        for node in p.childNodes:
            if hasattr(node, 'data'):
                text += node.data
            elif hasattr(node, '__str__'):
                text += str(node)
        parts.append(text)
    return '\n'.join(parts)


def get_repeat_count(element, attr_name):
    """Get the repeat count from an element attribute."""
    for attr in element.attributes:
        if attr[1] == attr_name:
            return int(element.attributes[attr])
    return 1


def convert_ods_to_csv(ods_path):
    """Convert each sheet in an ODS file to a separate CSV file."""
    ods_path = Path(ods_path)
    output_dir = ods_path.parent
    doc = load(str(ods_path))

    sheets = doc.spreadsheet.getElementsByType(Table)
    for sheet in sheets:
        sheet_name = sheet.getAttribute('name')
        csv_path = output_dir / f"{ods_path.stem}_{sheet_name}.csv"

        rows = []
        for row in sheet.getElementsByType(TableRow):
            row_repeat = get_repeat_count(row, 'number-rows-repeated')
            cells = []
            for cell in row.getElementsByType(TableCell):
                col_repeat = get_repeat_count(cell, 'number-columns-repeated')
                text = get_cell_text(cell)
                cells.extend([text] * col_repeat)
            # Trim trailing empty cells
            while cells and cells[-1] == '':
                cells.pop()
            rows.extend([cells] * row_repeat)

        # Trim trailing empty rows
        while rows and (not rows[-1] or all(c == '' for c in rows[-1])):
            rows.pop()

        with open(csv_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(rows)

        print(f"Written: {csv_path} ({len(rows)} rows)")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        ods_file = sys.argv[1]
    else:
        ods_file = 'docs_MOE/kautian.ods'
    convert_ods_to_csv(ods_file)
