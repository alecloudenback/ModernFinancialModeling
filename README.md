# Computational Thinking for Actuaries and Financial Professionals

## Rendering the Book

### Setup

1. [Install Quarto and the VS Code Extension](https://quarto.org/docs/get-started/)
2. You need to [install additional prerequisites](https://quarto.org/docs/output-formats/pdf-basics.html#prerequisites) to render to PDF.
3. You need https://wiki.gnome.org/Projects/LibRsvg to render SVGs in PDF. On Mac, this is available via Homebrew: `brew install librsvg`.

#### Preview

`quarto preview` will open the HTML version in browser and automatically update as you make changes.

#### Render

`quarto render` will render the book to HTML and PDF in the `_book` directory.
