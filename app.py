import streamlit as st
import pandas as pd
import glob

st.set_page_config(layout = "wide")
st.title("Critical Minerals Interactive Table")
st.subheader("Raw data")

if "selected_element" not in st.session_state:
    st.session_state["selected_element"] = None

if st.session_state["selected_element"] is None:
    filenames = glob.glob("*.csv")

    data ={}
    for filename in filenames:
        clean_name = filename.replace(".csv", "")
        data[clean_name] = pd.read_csv(filename, sep =";")

    elements = data["elements"]
    # Create data for the periodic table
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
else:
    st.write(st.session_state["selected_element"])



st.write(data["elements"])
st.write(f"Debug: You selected {st.session_state['selected_element']}")