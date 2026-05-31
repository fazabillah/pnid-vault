import streamlit as st

st.set_page_config(page_title="P&ID Extractor", layout="wide")

st.title("P&ID Extractor RBI")
st.write("Hello from Streamlit!")

with st.sidebar:
    st.header("About")
    st.write("""
    This is a Streamlit MVP that extracts valve tags, piping/service/spec text,
    and annotation markers from P&ID PDFs.
    """)

st.success("✓ Environment setup complete!")
st.info("Ready to build the next sprint: Project Structure and Backend Foundation")
