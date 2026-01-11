import streamlit as st

class Sidebar:
    def __init__(self, side_title: str, markdown_enabled: bool):
        st.header(side_title)
        if markdown_enabled:
            st.sidebar.markdown(side_title)
        
        # markdown
        st.markdown(
            """
            <style>
                [data-testid="stSidebarNav"] {
                    background-image: url(https://i.ibb.co/YL7RBrk/2.png);
                    background-size: 140px 140px;
                    background-repeat: no-repeat;
                    padding-top: 100px;
                    background-position: 20px 20px;
                }
                [data-testid="stSidebar"] {
                    background-color: black;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )