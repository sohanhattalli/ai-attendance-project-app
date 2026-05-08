import streamlit as st
from src.components.footer import footer_dashboard
from src.ui.style_base_layout import style_background_dashboard, style_base_layout

def student_screen():
    style_background_dashboard()
    style_base_layout()
    st.header("Student Screen")
    footer_dashboard()