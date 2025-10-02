import streamlit as st
import streamlit.components.v1 as components
import os

# Set Streamlit page configuration for a wide, borderless layout
st.set_page_config(layout="wide", page_title="Spam Classifier AI")

# --- HIDE STREAMLIT STYLE ---
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


# --- SERVE THE STATIC FRONTEND ---
# This now points to the 'static' directory where the index.html and models folder are located.
# This is the standard way to serve a frontend with Streamlit components.
frontend_dir = os.path.join(os.path.dirname(__file__), "static")
frontend_path = os.path.join(frontend_dir, "index.html")

# By setting the path for components, Streamlit can correctly serve
# other files in that directory (like your models).
st.components.v1.html(open(frontend_path).read(), height=1000, scrolling=False)

