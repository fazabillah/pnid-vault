import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
OUTPUT_DIR = PROJECT_ROOT / "output"
TESTS_DIR = PROJECT_ROOT / "tests"

PDF_PATH = DATA_DIR / "PnID-sample.pdf"
GROUND_TRUTH_VALVES = DATA_DIR / "ground_truth_valves.csv"
GROUND_TRUTH_PIPING = DATA_DIR / "ground_truth_piping.csv"

TESSERACT_PATH = "/usr/local/bin/tesseract"
TESSERACT_DPI = 300

OCR_TRIGGER_MIN_WORDS = 10
OCR_TRIGGER_MIN_CHARS = 50
