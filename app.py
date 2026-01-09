import pandas as pd
import streamlit as st
import plotly.express as px

datos=pd.read_csv('vehicles_us.csv')

st.title('Analises de ventas')
st.header('Analisis exploratorio')