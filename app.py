import streamlit as st
import pandas as pd
import glob
from views import display_periodic_table, display_legend


st.set_page_config(layout = "wide")
st.title("Critical Minerals Interactive Table")
st.subheader("Raw data")

if "selected_element" not in st.session_state:
    st.session_state["selected_element"] = None

filenames = glob.glob("*.csv")
data ={}
for filename in filenames:
        clean_name = filename.replace(".csv", "")
        data[clean_name] = pd.read_csv(filename, sep =";")
elements = data["elements"]
prices = data["prices"]
production = data["production"]

if st.session_state["selected_element"] is None:

    display_legend()
    display_periodic_table(elements)
    

else:
    st.title(f"{st.session_state["selected_element"]} Details")
    production_data = production[production["Symbol"] == st.session_state["selected_element"]]
    price_data = prices[prices["Symbol"] == st.session_state["selected_element"]]

    st.write("Production Info", production_data)
    st.write("Price Info", price_data)

    if st.button("Back"):
         st.session_state["selected_element"] = None
         st.rerun()

st.write(f"Debug: You selected {st.session_state['selected_element']}")