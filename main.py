import streamlit as st
import pandas as pd
import plotly.express as px
df = pd.read_csv("https://raw.githubusercontent.com/hermeson883/data_science_workshop"
                 "/main/linguagens.csv")

grafico = px.pie(df, names='Linguagem')
grafico2 = px.bar(df, color='Linguagem', x='Linguagem',
                  y='Desenvolvedores')
st.plotly_chart(grafico)
st.plotly_chart(grafico2)

st.write("## Dieguinho")
st.write("""
    ## Dieguinho 
""")

st.map()