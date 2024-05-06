import streamlit as st
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/hermeson883/data_science_workshop"
                 "/main/linguagens.csv")

st.bar_chart(df, x='Linguagem', y='Desenvolvedores')
