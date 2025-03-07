import streamlit as st

import pandas as pd

# CSV-Datei laden
df_all = pd.read_csv("df_all.csv")  # Falls es eine Excel-Datei ist: pd.read_excel("mein_datensatz.xlsx")


st.title("Happiness 🙂")

st.markdown("<h3 style='color: #6E66CC;'>A single factor or the interplay of many?</h3>", unsafe_allow_html=True)

st.markdown("""

How happy is our society – and is happiness measurable? Various indicators make it possible to describe the subjective and objective well-being of a society or an individual. But which country is truly the happiest? And can we identify differences in terms of prosperity, social environment, or political conditions? Is happiness determined by individual factors alone, or is it ultimately the interplay of several influences?


---
""")
st.sidebar.title("Table of contents")
pages=["Exploration", "DataVizualization", "Modelling"]
page=st.sidebar.radio("Go to", pages)

if page == pages[0] : 
  st.markdown("<h3 style='color: #6E66CC;'>Exploration</h3>", unsafe_allow_html=True)
  st.dataframe(df_all.head())
  st.dataframe(df_all.describe())
  st.write(df_all.shape)
if page == pages[1] : 
  st.markdown("<h3 style='color: #6E66CC;'>DataVizualization</h3>", unsafe_allow_html=True)
if page == pages[2] : 
    st.markdown("<h3 style='color: #6E66CC;'>Modelling</h3>", unsafe_allow_html=True)
