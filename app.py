import streamlit as st
import streamlit.components.v1 as components
import os

# INSTRUCTION: Set page configuration
st.set_page_config(layout="wide", page_title="Spam Classifier AI")

# INSTRUCTION: Hide default Streamlit UI elements
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .block-container {
                padding-top: 0rem;
                padding-bottom: 0rem;
                padding-left: 0rem;
                padding-right: 0rem;
            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# INSTRUCTION: Define the path to the static frontend files
# This assumes 'app.py' is in the root and 'index.html' is in './static/index.html'
html_file_path = os.path.join(os.path.dirname(__file__), 'static', 'index.html')

# INSTRUCTION: Read and serve the HTML file
try:
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    # Embed the HTML. The browser will now correctly request assets from the /static/ path.
    components.html(html_content, height=1000, scrolling=False)
except FileNotFoundError:
    st.error("CRITICAL ERROR: 'static/index.html' not found. Please verify your file structure.")

