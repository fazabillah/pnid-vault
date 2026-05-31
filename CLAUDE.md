# P&ID Extractor RBI

A Streamlit MVP that extracts valve tags, piping/service/spec text, and annotation markers from P&ID PDFs, with a grounded GenAI copilot for RBI engineers. Built locally on macOS, Python 3.12, open-source stack.

## How to resume any session

1. Read `.planning/PROGRESS.md` — this tells you the current sprint, its status, and exactly what to do next.
2. Read the current sprint file at `.planning/sprints/sprint-XX.md`.
3. Resume from the handoff note. No other briefing is needed.

## Tracking structure

- `.planning/PROGRESS.md` — master tracking file, always current
- `.planning/sprints/sprint-XX.md` — one file per sprint (00–11), pre-populated from PRD
- `.planning/PRD.md` — full product requirements document
- `.planning/PnID-sample.pdf` — sample drawing used for testing
- `data/ground_truth_valves.csv` — manual list of every visible valve tag on the sample (created in Sprint 05)
- `data/ground_truth_piping.csv` — manual list of visible service labels on the sample (created in Sprint 06)

## Sprint plan (12 sprints — authoritative)

00 Environment Setup → 01 Project Structure → 02 PDF Ingestion (with bboxes) → 03 OCR Fallback (with bboxes) → **04 Database Layer** → 05 Valve Extraction → 06 Piping Extraction → 07 Frontend Review UI → 08 Annotation Engine → 09 GenAI Copilot → 10 Integration Tests → 11 Packaging

The database moved from Sprint 08 → 04 on 2026-05-31 so Sprints 05–08 build directly against persistence.

## After each sprint, always update

1. The sprint file: check off completed tasks, list files created/modified, record decisions made.
2. `PROGRESS.md`: update current sprint, rewrite the handoff note, check off the sprint in the checklist, add to the decisions log if relevant.

## Key constraints

- Python 3.12 only
- macOS (MacBook Air M4), local-first
- Open-source tools by default; free-tier or trial APIs only if open source is not enough
- User is new to Python — keep steps beginner-friendly and explain each terminal command

## Locked MVP decisions (PRD §18, resolved 2026-05-31)

- Valve extraction: tag only; coarse type from prefix, blank if unknown
- No line tracing in MVP
- Multi-page PDFs supported, per-page independent
- Manual marker confirmation is optional
- OCR: Tesseract local only (no API fallback)
- Copilot: Ollama local first (llama3.1:8b or qwen2.5:7b); free-trial API only as fallback

## Tech stack

- UI: Streamlit
- PDF reading: PyMuPDF (`fitz`) — committed; bbox API beats pdfplumber
- OCR fallback: Tesseract via `pytesseract` — committed (EasyOCR dropped)
- Image processing: Pillow / OpenCV
- Data tables: Pandas
- Local database: SQLite (introduced in Sprint 04)
- Tests: pytest
- AI copilot: Ollama (local) with free-trial API as fallback

## Architecture invariants

- Every extracted word (PDF or OCR) has a bounding box in PDF user units. Coordinate normalization happens in Sprint 03 so downstream sprints don't care about the source.
- Sprint 04 onward: all data flows through SQLite. No in-memory-only state for valves, piping, or markers.
- Sprint 08 annotation uses bboxes captured during extraction. No CV symbol detection in MVP.
- Evaluation against ground-truth CSVs is part of Sprints 05, 06, and 10.

## Coding rules

- Keep files small and focused — no large monolithic scripts
- Use functions and modules
- Write clean, readable code; comments only where logic is non-obvious
- No over-engineering for MVP
- Do not add features beyond what the current sprint requires
