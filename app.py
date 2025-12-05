import streamlit as st
import pandas as pd
import glob

st.set_page_config(layout = "wide")
st.title("Critical Minerals Interactive Table")

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
        
        element_data = elements[(elements["Row"] == r) & (elements["Column"] == c)]
        
        if not element_data.empty:
            cols[c-1].button(element_data.iloc[0]['Symbol'])
            
st.subheader("Raw data")
st.write(data["elements"])
st.write(data["prices"])