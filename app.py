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
# Construct the path to the index.html file.
# CORRECTED: This now correctly looks for index.html in the same directory as app.py.
<<<<<<< HEAD
frontend_path = os.path.join(os.path.dirname(__file__), "index.html")

=======
frontend_path = os.path.join(os.path.dirname(__file__), "static", "index.html")
>>>>>>> 6769ce056c0aa2d81be80e294e91af0ddd4c91c4
# Read the content of the index.html file
html_content = ""
try:
    with open(frontend_path, "r", encoding="utf-8") as f:
        html_content = f.read()
except FileNotFoundError:
    st.error("Frontend file not found! Ensure 'index.html' is in the same directory as this script.")

# --- RENDER HTML ---
# Embed the HTML in the Streamlit app.
# `scrolling=False` is important for single-page apps.
# Height is set to a high value to ensure it can fill the viewport.
components.html(html_content, height=1000, scrolling=False)
