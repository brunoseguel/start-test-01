
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

# data preparations
with st.sidebar:
  st.header('Input features')
  island = st.selectbox('Island', ('Biscoe', 'Dream', 'Torgersen'))
  gender = st.selectbox('gender',('male', 'female'))
  bill_length_mm = st.slider('Bill length (mm)', 32.1, 59.6, 43.9)
  bill_depth_mm = st.slider('Bill depth (mm)', 13.1, 21.5, 17.2)
  flipper_length_mm = st.slider('Fliper length (mm)', 172.0, 231.0, 201.0)
  body_mass_g = st.slider('Body mas (g)', 2700.0, 6300.0, 4207.0)

  # Create a Dataframe for the input features
  data = {'island', island,
        'gender', gender,
        'bill_length_mm', bill_length_mm,
        'bill_depth_mm', bill_depth_mm,
        'flipper_length_mm', flipper_length_mm,
        'body_mass_g', body_mass_g}
  input_df = pd.Dataframe(data, index=[0])

input_df


