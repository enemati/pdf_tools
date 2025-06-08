import sys
from pdf2image import convert_from_path

def print_help():
    help_text = """
Usage:
    python3 converter.py <pdf_file> <format> [dpi] [quality]

Arguments:
    <pdf_file>     Path to the input PDF file (required)
    <format>       Output image format: PNG, JPEG, BMP, etc. (required)
    [dpi]          Optional. DPI (dots per inch) for image quality. Default is 300.
    [quality]      Optional. Only for JPEG. Compression quality (1-100). Default is 75.

Examples:
    python3 converter.py Ticket.pdf PNG
    python3 converter.py Ticket.pdf JPEG 300
    python3 converter.py Ticket.pdf JPEG 300 90

Notes:
    - For formats other than JPEG, the 'quality' parameter is ignored.
"""
    print(help_text)

# Show help
if len(sys.argv) >= 2 and sys.argv[1] in ['--help', '-h']:
    print_help()
    sys.exit(0)

# Check minimum required arguments
if len(sys.argv) < 3:
    print("❌ Error: Missing required arguments.\nUse --help to see usage instructions.")
    sys.exit(1)

# Read arguments
pdf_path = sys.argv[1]
image_format = sys.argv[2].upper()

# DPI default is 300
try:
    dpi = int(sys.argv[3]) if len(sys.argv) >= 4 else 300
except ValueError:
    print("❌ Error: DPI must be an integer.")
    sys.exit(1)

# JPEG quality default is 75 (only used for JPEG)
try:
    quality = int(sys.argv[4]) if image_format == 'JPEG' and len(sys.argv) >= 5 else 75
except ValueError:
    print("❌ Error: JPEG quality must be an integer between 1 and 100.")
    sys.exit(1)

# Run conversion
try:
    images = convert_from_path(pdf_path, dpi=dpi)
    for i, image in enumerate(images):
        filename = f'page_{i + 1}.{image_format.lower()}'
        if image_format == 'JPEG':
            image.save(filename, image_format, quality=quality)
        else:
            image.save(filename, image_format)
    print(f"✅ Converted {len(images)} page(s) to {image_format} at {dpi} DPI (quality={quality if image_format == 'JPEG' else 'N/A'}).")
except Exception as e:
    print(f"❌ Error: {e}")
