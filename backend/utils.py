"""Utility functions for PDF and image processing."""

from pathlib import Path
from PIL import Image
import io


def pdf_to_images(pdf_path: str, page_nums: list[int] = None) -> list[Image.Image]:
    """Convert PDF pages to PIL images.

    Args:
        pdf_path: Path to the PDF file.
        page_nums: List of page numbers (0-indexed). If None, convert all pages.

    Returns:
        List of PIL Image objects.
    """
    import fitz

    doc = fitz.open(pdf_path)
    images = []
    pages_to_process = page_nums if page_nums else range(len(doc))

    for page_num in pages_to_process:
        page = doc[page_num]
        pix = page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5))
        img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        images.append(img)

    doc.close()
    return images


def get_word_bbox(word_dict: dict) -> tuple[float, float, float, float]:
    """Extract bounding box from PyMuPDF word dictionary.

    Returns (x0, y0, x1, y1) in PDF user units.
    """
    return (word_dict[0], word_dict[1], word_dict[2], word_dict[3])
