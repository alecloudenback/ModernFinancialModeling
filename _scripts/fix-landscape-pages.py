#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["pikepdf"]
# ///
"""
Post-render script to rotate landscape pages back to portrait.
Quarto's landscape divs create pages that are physically rotated in the PDF,
which some publishers don't accept. This script detects landscape pages
(width > height) and rotates them 90 degrees clockwise.
"""

from pathlib import Path
import pikepdf


def fix_landscape_pages(pdf_path: Path) -> None:
    """Rotate any landscape pages to portrait orientation."""

    if not pdf_path.exists():
        print(f"PDF not found: {pdf_path}")
        return

    print(f"Checking {pdf_path} for landscape pages...")

    with pikepdf.open(pdf_path, allow_overwriting_input=True) as pdf:
        rotated_pages = []

        for i, page in enumerate(pdf.pages):
            # Get the effective dimensions accounting for existing rotation
            rotation = int(page.get("/Rotate", 0))
            box = page.mediabox
            width = float(box[2]) - float(box[0])
            height = float(box[3]) - float(box[1])

            # Account for existing rotation when determining orientation
            if rotation in (90, 270):
                width, height = height, width

            # If width > height, it's landscape and needs rotation
            if width > height:
                rotated_pages.append(i + 1)  # 1-indexed for display
                page.rotate(-90, relative=True)

        if rotated_pages:
            pdf.save(pdf_path)
            print(f"Rotated {len(rotated_pages)} landscape page(s): {rotated_pages}")
        else:
            print("No landscape pages found.")


def main():
    # Find PDF files in _book directory
    book_dir = Path("_book")

    if not book_dir.exists():
        print("_book directory not found")
        return

    pdf_files = list(book_dir.glob("*.pdf"))

    if not pdf_files:
        print("No PDF files found in _book/")
        return

    for pdf_path in pdf_files:
        fix_landscape_pages(pdf_path)


if __name__ == "__main__":
    main()
