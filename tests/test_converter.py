import importlib
import sys
import types
from unittest import mock

import pytest

# Helper function to import the converter module with patched dependencies

def import_converter(args, images=None):
    sys.modules.pop('converter', None)
    fake_image = mock.Mock()
    fake_images = images if images is not None else [fake_image]
    fake_pdf2image = types.SimpleNamespace(convert_from_path=mock.Mock(return_value=fake_images))
    with mock.patch.dict(sys.modules, {"pdf2image": fake_pdf2image}):
        with mock.patch.object(sys, "argv", ["converter.py", *args]):
            module = importlib.import_module("converter")
    return module, fake_pdf2image, fake_images


def test_help(capsys):
    with pytest.raises(SystemExit) as exc:
        import_converter(["--help"], images=[])
    assert exc.value.code == 0
    out = capsys.readouterr().out
    assert "Usage:" in out


def test_missing_arguments(capsys):
    with pytest.raises(SystemExit) as exc:
        import_converter([])
    assert exc.value.code == 1
    out = capsys.readouterr().out
    assert "Missing required arguments" in out


def test_invalid_dpi(capsys):
    with pytest.raises(SystemExit) as exc:
        import_converter(["file.pdf", "PNG", "abc"])
    assert exc.value.code == 1
    out = capsys.readouterr().out
    assert "DPI must be an integer" in out


def test_jpeg_conversion():
    module, fake_pdf2image, images = import_converter([
        "file.pdf",
        "JPEG",
        "200",
        "80",
    ])
    fake_pdf2image.convert_from_path.assert_called_once_with("file.pdf", dpi=200)
    images[0].save.assert_called_once_with("page_1.jpeg", "JPEG", quality=80)
