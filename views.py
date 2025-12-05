import streamlit as st
import pandas as pd

def display_periodic_table(elements):
    for r in range(1, 10):
        cols = st.columns(18)
        for c in range(1, 19):
                
            filter = (elements['Row'] == r) & (elements['Column'] == c)
            element_data = elements[filter]
               
            if not element_data.empty:
                symbol = element_data.iloc[0]['Symbol']

                if cols[c-1].button(symbol):
                    st.session_state["selected_element"] = symbol
                    st.rerun()