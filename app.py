import streamlit as st
import streamlit.components.v1 as components
import os

# --- Page Configuration ---
# This must be the first Streamlit command in your script.
st.set_page_config(layout="wide", page_title="URL Threat Analyzer")

# --- Path Configuration ---
# Get the absolute path to the directory where this script is located.
_RELEASE = True # Set to False for local development
if not _RELEASE:
    _root_dir = os.path.dirname(os.path.abspath(__file__))
    _static_dir = os.path.join(_root_dir, "static")
    _frontend_dir = os.path.join(_root_dir, "frontend")
else:
    _root_dir = os.path.dirname(os.path.abspath(__file__))
    _static_dir = os.path.join(_root_dir, "static")
    _frontend_dir = os.path.join(_root_dir, "frontend")


# --- Serve the Frontend ---
# Check if the index.html file exists.
frontend_path = os.path.join(_frontend_dir, "index.html")
if not os.path.exists(frontend_path):
    st.error("Fatal Error: `frontend/index.html` not found. Please ensure the file exists in the correct directory.")
else:
    # Read the HTML file
    with open(frontend_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # --- Serve the Static Model Files ---
    # Streamlit serves files from a directory named 'static' by default at the root level.
    # The frontend JavaScript will fetch from '/static/model.json' etc.
    # This configuration works seamlessly with Streamlit's server.

    # Render the HTML using Streamlit Components
    components.html(html_content, height=1024, scrolling=True)

    # Add a footer to confirm the app is running via Streamlit
    st.markdown("---")
    st.info("Powered by Streamlit. Analysis is performed 100% in your browser.")

