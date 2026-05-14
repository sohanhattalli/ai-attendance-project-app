import streamlit as st



def style_background_home():

    st.markdown("""
        <style>
                @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');

                .stApp {
                    background: #5865F2 !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background-color:#E0E3FF !important;
                    padding:2.5rem !important;
                    border-radius: 5rem !important;
                    }

                .landing-role-title {
                    font-family: 'Climate Crisis', sans-serif !important;
                    font-size: 2rem !important;
                    line-height: 1.15 !important;
                    color: #111111 !important;
                    margin: 0 0 0.75rem 0 !important;
                    font-weight: 700 !important;
                }
        </style>  

                """
            ,unsafe_allow_html=True)
    

def style_background_dashboard():

    st.markdown("""
        <style>

                .stApp {
                    background: #E0E3FF !important;
                }

        </style>  

                """
            ,unsafe_allow_html=True)
    

    

def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

                
         /* Hide Top Bar of streamlit */
                
            #MainMenu, footer, header {
                visibility: hidden;
            }
                
            .block-container {
                padding-top:1.5rem !important;    
            }

            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height: 1.1 !important;
                margin-bottom:0rem !important;
            }
                

            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height:0.9 !important;
                margin-bottom:0rem !important;
            }
                
            h3, h4, p {
                font-family: 'Outfit', sans-serif;    
            }

            button[kind="primary"]{
                border-radius: 1.5rem !important;
                background-color: #5865F2 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background-color: #EB459E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: black !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="primary"]:hover,
            button[kind="secondary"]:hover,
            button[kind="tertiary"]:hover{
                transform: scale(1.05);
            }

            /* After button styles: inputs & selects need light surfaces (must load last to win over stray rules) */
            div[data-testid="stTextInput"] input,
            div[data-testid="stTextArea"] textarea,
            div[data-testid="stNumberInput"] input,
            div[data-testid="stDateInput"] input {
                background-color: #ffffff !important;
                color: #111111 !important;
                caret-color: #111111 !important;
                border: 1px solid rgba(17, 17, 17, 0.22) !important;
                border-radius: 0.75rem !important;
            }

            /* Make the typing caret visible on focus across all text-like inputs */
            div[data-testid="stTextInput"] input:focus,
            div[data-testid="stTextArea"] textarea:focus,
            div[data-testid="stNumberInput"] input:focus,
            div[data-testid="stDateInput"] input:focus {
                caret-color: #111111 !important;
                outline: 2px solid #5865F2 !important;
                outline-offset: 1px !important;
            }

            div[data-testid="stSelectbox"] [data-baseweb="select"] > div,
            div[data-testid="stMultiSelect"] [data-baseweb="select"] > div {
                background-color: #ffffff !important;
                color: #111111 !important;
                border: 1px solid rgba(17, 17, 17, 0.22) !important;
                border-radius: 0.75rem !important;
            }

            div[data-testid="stSelectbox"] button,
            div[data-testid="stMultiSelect"] button {
                background-color: #ffffff !important;
                color: #111111 !important;
                border: 1px solid rgba(17, 17, 17, 0.22) !important;
            }

            .block-container label[data-testid="stWidgetLabel"] p {
                color: #111111 !important;
            }

            div[data-testid="stFileUploader"] section {
                background-color: rgba(255, 255, 255, 0.96) !important;
                border: 1px solid rgba(17, 17, 17, 0.15) !important;
                border-radius: 0.75rem !important;
            }
        </style>  

                """
            ,unsafe_allow_html=True)