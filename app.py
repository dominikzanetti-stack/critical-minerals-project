import streamlit as st
import pandas as pd

st.set_page_config(layout = "wide")

st.title("Critical Minerals Interactive Table")
st.write("This application will visualize critical minerals and their supply chains")

data = pd.DataFrame({
    'Element': ['Lithium', 'Cobalt', ' Nickel'],
    'Price': ['100', '50', '20']
})

st.dataframe(data)