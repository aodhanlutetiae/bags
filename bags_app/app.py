import streamlit as st
import pandas as pd
# import functions from separate file
from utils import load_data, get_shop, median

# layout and titling
st.set_page_config(layout="wide")
st.title('Vanishing bags')

# sidebar titling
with st.sidebar:
    st.header('Single-use plastic bags in England, the first six years')
    st.write(
        "The money each company collected, once single-use plastic bag charges came in (2016)"
    )

# assign data to df
df = load_data()

# title bar chart then show by calling function in utils.py, and add divider
st.header('Median value of money and donations')
st.bar_chart(data=median(df))
st.divider()

# build sidebar for filter
with st.sidebar:
    shops = get_shop(df)
    siopa = st.selectbox("Company", ["All"] + shops)
if siopa != "All":
    df = df[df["Company"] == siopa]

# show table (filtered or not)
st.table(df)
