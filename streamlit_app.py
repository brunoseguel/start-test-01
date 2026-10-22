import streamlit as st
import pandas as pd

st.title('🤖 test app ML')

st.write('Primera prueba de *App* de ***Machine Learning***')

with st.expander('data'):
  st.write('**Raw data**')
  df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
  st.dataframe(df)

  st.write('**X**')
  X = df.drop('species', axis=1)
  X

  st.write('**y**')
  y = df.species
  y
