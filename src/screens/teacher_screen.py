import streamlit as st
from src.components.footer import footer_dashboard
from src.ui.style_base_layout import style_background_dashboard, style_base_layout

def teacher_screen():
    style_background_dashboard()
    style_base_layout()
    st.header("Teacher Screen")
    footer_dashboard()