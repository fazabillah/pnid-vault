# P&ID Extractor RBI

A Streamlit MVP for extracting valve tags, piping/service labels, and annotation markers from P&ID PDFs, with a grounded GenAI copilot for RBI engineers.

## Quick Start

1. **Activate the virtual environment:**
   ```bash
   source venv/bin/activate
   ```

2. **Run the app:**
   ```bash
   streamlit run app/main.py
   ```

3. **Upload a P&ID PDF** to begin extraction.

## Project Structure

- **`app/`** — Streamlit frontend and configuration
  - `main.py` — Main app entrypoint
  - `config.py` — Paths, constants, and settings
- **`backend/`** — Core extraction and processing logic
  - `utils.py` — PDF, image, and utility functions
  - More modules added as sprints progress
- **`frontend/`** — UI components and helpers
- **`data/`** — Sample PDFs and ground truth CSVs for evaluation
- **`tests/`** — Unit and integration tests
- **`output/`** — Extraction results and debug artifacts

## Tech Stack

- **UI:** Streamlit
- **PDF:** PyMuPDF (fitz)
- **OCR:** Tesseract (via pytesseract)
- **Image Processing:** Pillow, OpenCV
- **Data:** Pandas
- **Database:** SQLite (Sprint 04+)
- **Tests:** pytest

## Development

Each sprint builds one feature end-to-end. See `.planning/PROGRESS.md` for the current sprint and next steps.

## License

MIT
