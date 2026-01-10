import pandas as pd
import streamlit as st
import plotly.express as px

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv') #Datos de vehiculos de US

st.header('Anuncio de vehiculos')


hist_button = st.button('Construir histograma')# crear un botón
if hist_button:
   st.write("Creación de histograma para el conjunto de datos de anuncios de venta de coches.")
    # Crear un histograma
   fig_hist = px.histogram(car_data, x="odometer",title="Información del kilometraje de los vehiculos") 
   fig_hist.update_layout(width=600, height=500,xaxis_title="Kilometraje",yaxis_title="Conteo")
   st.plotly_chart(fig_hist)  # Mostrar en Streamlit



disp_button = st.button('Construir diagrama') # crear un botón
     
if disp_button:
    st.write('Creación de un diagrama de disperción para el conjunto de datos de anuncios de venta de coches.')
    #Crear grafico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price",title="Relación de rodado y precio")
    fig_scatter.update_layout(width=600, height=500,xaxis_title="Kilometraje",yaxis_title="Precio")
    st.plotly_chart(fig_scatter)  # Mostrar en Streamlit

         

