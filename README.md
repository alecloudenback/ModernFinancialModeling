# Modern Financial Modeling: Concepts and Applications for Actuaries and Other Financial Professionals

## Rendering the Book

### Setup

1. [Install Quarto and the VS Code Extension](https://quarto.org/docs/get-started/)
2. You need to [install additional prerequisites](https://quarto.org/docs/output-formats/pdf-basics.html#prerequisites) to render to PDF.
3. You need https://wiki.gnome.org/Projects/LibRsvg to render SVGs in PDF. On Mac, this is available via Homebrew: `brew install librsvg`.
4. To render the PDF with fonts that include unicode characters (e.g. `ϵ`), you need to install the fonts from here: https://mirrors.mit.edu/CTAN/fonts/tex-gyre.zip

#### Preview

`quarto preview` will open the HTML version in browser and automatically update as you make changes.

#### Render

`quarto render` will render the book to HTML and PDF in the `_book` directory.


## Code Environments

Each chapter should stand alone as it's own `.qmd` file. This allows us to render each chapter individually, and also to render the entire book. For dependencies, create a folder in the `env` folder to correspond to a single chanpter, and at the start of the file activate the environment (use the REPL to create/edit the environment to avoid running package operations on each quarto preview/render).