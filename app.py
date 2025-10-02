import streamlit as st
import streamlit.components.v1 as components
import os

# Set Streamlit page configuration for a wide, borderless layout
st.set_page_config(layout="wide", page_title="Spam Classifier AI")

# --- HIDE STREAMLIT STYLE ---
# Hide the default Streamlit header, footer, and menu
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

# --- GET HTML CONTENT ---
# Construct the path to the index.html file
# This assumes your script `app.py` is in the root, and `index.html` is in `static/`
frontend_path = os.path.join(os.path.dirname(__file__), "static", "index.html")

# Read the content of the index.html file
html_content = ""
try:
    with open(frontend_path, "r", encoding="utf-8") as f:
        html_content = f.read()
except FileNotFoundError:
    st.error("Frontend file not found! Ensure 'static/index.html' exists.")

# --- RENDER HTML ---
# Embed the HTML in the Streamlit app.
# `scrolling=False` is important for single-page apps.
# Height is set to a high value to ensure it can fill the viewport.
components.html(html_content, height=1000, scrolling=False)
