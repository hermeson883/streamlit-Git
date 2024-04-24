import streamlit as st
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/hermeson883/data_science_workshop/main/linguagens.csv")

st.dataframe(df)

linguagens = df["Linguagem"].unique()

escolha = st.selectbox("Escolha um", linguagens)

if st.button("Click em mim"):
    filtro = df.loc[df["Linguagem"] == escolha]
    st.write(filtro)