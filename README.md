# PDF Tools

This repository contains a simple CLI script for converting PDF pages to image files.

## Requirements

- Python 3.11 or later
- [`pdf2image`](https://github.com/Belval/pdf2image) Python package
- Poppler utilities installed on your system (required by `pdf2image`)

Install the dependency with pip:

```bash
pip install pdf2image
```

## Usage

Run the `converter.py` script from the command line. The script requires the path
of the PDF file and the desired output image format. Optional arguments allow you
to control the DPI and JPEG quality.

```bash
python3 converter.py <pdf_file> <format> [dpi] [quality]
```

Arguments:

- `<pdf_file>` – Path to the input PDF file.
- `<format>` – Output image format such as `PNG`, `JPEG` or `BMP`.
- `[dpi]` – Optional dots per inch value (default `300`).
- `[quality]` – Optional JPEG quality from 1–100 (default `75`). Ignored for
  other formats.

### Examples

```bash
# Convert to PNG using the default DPI
python3 converter.py Ticket.pdf PNG

# Convert to JPEG at 300 DPI with quality 90
python3 converter.py Ticket.pdf JPEG 300 90
```

The script saves each page of the PDF as a separate image named `page_1.png`,
`page_2.png`, and so on. When converting to JPEG, the `quality` parameter sets the
compression level.

## Help

You can display a help message with the following command:

```bash
python3 converter.py --help
```
