#!/Users/alecloudenback/.local/pipx/venvs/pymupdf/bin/python
"""
Check PDF pages for content overflow beyond margins.

Usage: python check_overflow.py [options] [path_to_pdf]

Options:
  --all           Show all overflow (including headers/footers)
  --side-only     Only show left/right overflow (default)
  --threshold N   Minimum overflow in points to report (default: 5)

If no path provided, defaults to _book/Modern-Financial-Modeling.pdf
"""

import sys
import argparse
try:
    import fitz  # PyMuPDF
except ImportError:
    print("PyMuPDF not installed. Run: pip install pymupdf")
    sys.exit(1)

# Page dimensions from _quarto.yml (in points, 72pt = 1 inch)
PAGE_WIDTH = 7 * 72    # 504pt
PAGE_HEIGHT = 10 * 72  # 720pt

# Margins in points
INNER_MARGIN = 1 * 72      # 72pt (1 inch)
OUTER_MARGIN = 0.75 * 72   # 54pt (0.75 inch)
TOP_MARGIN = 0.875 * 72    # 63pt
BOTTOM_MARGIN = 0.875 * 72 # 63pt

# Tolerance for floating point comparisons
TOLERANCE = 2


def get_content_bounds(page):
    """Get bounding box of all content on a page, excluding header/footer zones."""

    blocks = page.get_text("dict", flags=fitz.TEXT_PRESERVE_WHITESPACE)["blocks"]

    if not blocks:
        return None

    # Collect all content bounds
    all_bounds = []

    for block in blocks:
        bbox = block.get("bbox", (0, 0, 0, 0))
        all_bounds.append(bbox)

    # Also check for images
    for img in page.get_images():
        try:
            img_rect = page.get_image_bbox(img)
            if img_rect:
                all_bounds.append((img_rect.x0, img_rect.y0, img_rect.x1, img_rect.y1))
        except:
            pass

    # Check drawings (vector graphics) - these often cause overflow
    drawings = page.get_drawings()
    for d in drawings:
        if "rect" in d:
            r = d["rect"]
            all_bounds.append((r.x0, r.y0, r.x1, r.y1))

    return all_bounds


def check_page_overflow(page, page_num, check_vertical=False, threshold=5):
    """Check if content on a page extends beyond margins."""

    all_bounds = get_content_bounds(page)

    if not all_bounds:
        return None

    # Determine margins based on page number (1-indexed)
    # Odd pages: inner margin on left, outer on right
    # Even pages: outer margin on left, inner on right
    if page_num % 2 == 1:  # Odd page (recto)
        left_margin = INNER_MARGIN
        right_margin = OUTER_MARGIN
    else:  # Even page (verso)
        left_margin = OUTER_MARGIN
        right_margin = INNER_MARGIN

    # Calculate expected content boundaries
    expected_left = left_margin
    expected_right = PAGE_WIDTH - right_margin
    expected_top = TOP_MARGIN
    expected_bottom = PAGE_HEIGHT - BOTTOM_MARGIN

    # Header/footer zones (content in these areas is expected)
    header_zone = 50  # Content above this Y is in header zone
    footer_zone = PAGE_HEIGHT - 50  # Content below this Y is in footer zone

    issues = []

    # Check each content block
    for bbox in all_bounds:
        min_x, min_y, max_x, max_y = bbox

        # Skip tiny elements (likely artifacts)
        if (max_x - min_x) < 3 or (max_y - min_y) < 3:
            continue

        # Check left overflow (for main content, not header/footer)
        if min_x < expected_left - threshold:
            # Only report if it's in the main content area
            if min_y > header_zone and max_y < footer_zone:
                overflow = expected_left - min_x
                issues.append(f"Left overflow: {overflow:.1f}pt at y={min_y:.0f}-{max_y:.0f}")

        # Check right overflow
        if max_x > expected_right + threshold:
            if min_y > header_zone and max_y < footer_zone:
                overflow = max_x - expected_right
                issues.append(f"Right overflow: {overflow:.1f}pt at y={min_y:.0f}-{max_y:.0f}")

        # Vertical overflow (optional - usually expected for headers/footers)
        if check_vertical:
            if min_y < expected_top - threshold:
                overflow = expected_top - min_y
                issues.append(f"Top overflow: {overflow:.1f}pt")

            if max_y > expected_bottom + threshold:
                overflow = max_y - expected_bottom
                issues.append(f"Bottom overflow: {overflow:.1f}pt")

    # Deduplicate similar issues
    return list(set(issues)) if issues else None


def main():
    parser = argparse.ArgumentParser(description="Check PDF for content overflow")
    parser.add_argument("pdf_path", nargs="?", default="_book/Modern-Financial-Modeling.pdf",
                       help="Path to PDF file")
    parser.add_argument("--all", action="store_true",
                       help="Show all overflow including headers/footers")
    parser.add_argument("--threshold", type=float, default=5,
                       help="Minimum overflow in points to report (default: 5)")
    parser.add_argument("--verbose", "-v", action="store_true",
                       help="Show more details")

    args = parser.parse_args()

    try:
        doc = fitz.open(args.pdf_path)
    except FileNotFoundError:
        print(f"Error: PDF not found at {args.pdf_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error opening PDF: {e}")
        sys.exit(1)

    print(f"Checking {args.pdf_path} ({len(doc)} pages)")
    print(f"Page size: {PAGE_WIDTH}pt x {PAGE_HEIGHT}pt (7\" x 10\")")
    print(f"Margins - Inner: {INNER_MARGIN}pt (1\"), Outer: {OUTER_MARGIN}pt (0.75\")")
    print(f"Threshold: {args.threshold}pt")
    print("-" * 60)

    overflow_pages = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        display_num = page_num + 1  # 1-indexed for display

        # Check actual page size
        actual_width = page.rect.width
        actual_height = page.rect.height

        if abs(actual_width - PAGE_WIDTH) > TOLERANCE or abs(actual_height - PAGE_HEIGHT) > TOLERANCE:
            print(f"Page {display_num}: Unexpected size {actual_width:.1f}x{actual_height:.1f}pt")

        issues = check_page_overflow(page, display_num,
                                     check_vertical=args.all,
                                     threshold=args.threshold)

        if issues:
            overflow_pages.append((display_num, issues))
            print(f"\nPage {display_num}:")
            for issue in issues:
                print(f"  - {issue}")

    doc.close()

    print("\n" + "-" * 60)
    if overflow_pages:
        page_list = [p[0] for p in overflow_pages]
        print(f"Found overflow on {len(overflow_pages)} page(s):")
        # Group consecutive pages
        if len(page_list) <= 20:
            print(f"  Pages: {page_list}")
        else:
            print(f"  First 20: {page_list[:20]}...")
    else:
        print("No overflow detected.")


if __name__ == "__main__":
    main()
