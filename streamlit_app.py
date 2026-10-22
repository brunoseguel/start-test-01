import streamlit as st
import pandas as pd

st.title('🤖 test app ML')

st.write('Primera prueba de *App* de ***Machine Learning***')

df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
st.dataframe(df)
