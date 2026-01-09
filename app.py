import pandas as pd
import streamlit as st
import plotly.express as px

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

st.header('Mi Primer Proyecto WEB')

# Crear un histograma
fig_hist = px.histogram(car_data, x="odometer")
st.plotly_chart(fig_hist)  # Mostrar en Streamlit


hist_button = st.button('Construir diagrama') # crear un botón
     
if hist_button:
    st.write('Creación de un diagrama de disperción para el conjunto de datos de anuncios de venta de coches')
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig_scatter)  # Mostrar en Streamlit

         

