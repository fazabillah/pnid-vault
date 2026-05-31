"""Main Streamlit entrypoint for P&ID Extractor."""

import streamlit as st

st.set_page_config(
    page_title="P&ID Extractor",
    page_icon="📋",
    layout="wide",
)

st.title("P&ID Extractor")

st.markdown("""
Welcome to the P&ID Extractor MVP. This tool extracts valve tags,
piping/service labels, and annotations from P&ID PDFs.

**Features:**
- Upload and process P&ID PDF files
- Extract valve tags and specifications
- Annotate key equipment and piping routes
- AI-powered RBI insights

Start by uploading a P&ID file to begin.
""")

uploaded_file = st.file_uploader("Choose a P&ID PDF", type="pdf")

if uploaded_file is not None:
    st.success(f"File uploaded: {uploaded_file.name}")
    st.info("PDF processing coming in Sprint 02")
