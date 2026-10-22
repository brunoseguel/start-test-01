
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

with st.expander('Data visualization'):
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')

*data preparations
with st.sidebar:
  siland = st.selectbox'Island',('Biscon', 'Dream', 'Torgemsen'))

