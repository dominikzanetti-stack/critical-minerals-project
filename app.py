import streamlit as st
import pandas as pd
import glob
import json
import os
from views import display_periodic_table, display_legend


st.set_page_config(layout = "wide")
st.title("Critical Minerals Interactive Table")
st.subheader("Raw data")

LINKS_FILE = "element_links.json"

if os.path.exists(LINKS_FILE):
    # The 'with open' block creates the file object (f)
    with open(LINKS_FILE, "r") as f:
        # We pass the file object (f) to json.load()
        mineral_links = json.load(f)
    print(f"Loaded {len(mineral_links)} mineral links from file.")
else:
    print(f"Warning: {LINKS_FILE} not found. Ensure webcrawler.py has run successfully.")
    mineral_links = {}

# The rest of your app code follows...




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

    element_row = elements[elements["Symbol"] == st.session_state["selected_element"]]
    element_name = element_row.iloc[0]["Name"]
    xlsx_link = mineral_links[element_name]
    element_data = pd.read_excel(xlsx_link, header=3)

    st.write(element_data)

    st.write("Production Info", production_data)
    st.write("Price Info", price_data)

    if st.button("Back"):
         st.session_state["selected_element"] = None
         st.rerun()

st.write(f"Debug: You selected {st.session_state['selected_element']}")
