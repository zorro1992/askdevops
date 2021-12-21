import pandas as pd
import streamlit as st

st.title("Hello world!")

uploaded_file = st.file_uploader("../car_sale.csv")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.write(df)

