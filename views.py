import streamlit as st
import pandas as pd

def display_periodic_table(elements):
      for r in range(1, 11):
        cols = st.columns(18, gap = "small")
        for c in range(1, 19):
                
            filter = (elements['Row'] == r) & (elements['Column'] == c)
            element_data = elements[filter]
               
            if not element_data.empty:
                symbol = element_data.iloc[0]['Symbol']

                rare_val = element_data.iloc[0]["Rare"]
                crit_val = element_data.iloc[0]["Critical"]

                display_label = symbol

                if (rare_val == 1) and (crit_val == 1):
                    display_label = f"🟣 {symbol}"
                elif (rare_val == 1):
                    display_label = f"🔵 {symbol}"
                elif (crit_val == 1):
                    display_label = f"🔴 {symbol}"
                
                if cols[c-1].button(display_label, key = symbol):
                    st.session_state["selected_element"] = symbol
                    st.rerun()

def display_legend():
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("🔴 **Critical Mineral** (USGS 2025)")
    with c2:
        st.markdown("🔵 **Rare Earth Element**")
    with c3:
        st.markdown("🟣 **Both**")
        
    st.markdown("---")