from lib.sidebar import Sidebar
import streamlit as st
from lib.query import *

# BQ object from classes
from __init__ import bq

# Drop the title and tab text down here
CONST_PAGE_TITLE = "The Court"
CONST_TAB_1 = "TAB 1"
CONST_TAB_2 = "TAB 2"

st.set_page_config(
    page_title=CONST_PAGE_TITLE, page_icon="🗡️", initial_sidebar_state="collapsed"
)

st.markdown(
            """
            <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
            </style>
            """,
            unsafe_allow_html=True,
        )

sidebar = Sidebar(side_title=CONST_PAGE_TITLE, markdown_enabled=False)

# Set tabs, page must have different or unique tabs (streamlit limitation)
# or drop this Tab if you are not using it.
tab1, tab2 = st.tabs([CONST_TAB_1, CONST_TAB_2])

with tab1:
    # Your code here
    rows = bq.run_query(CONST_QUERY_GET_AWAY_TEAM_NAME)

    # Print results.
    st.write("Away Team Name:")
    for row in rows:
        st.write("✍️ " + row['away_team_name'])
    st.text_input(label="TAB1")
with tab2:
    # Your code here
    st.text_input(label="TAB2")
