import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Título principal
st.header('Venta de Vehículos')

# Checkbox para mostrar el histograma
build_histogram = st.checkbox('Mostrar histograma')

if build_histogram:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de vehículos')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# Checkbox para mostrar el gráfico de dispersión
build_scatter = st.checkbox('Mostrar gráfico de dispersión')

if build_scatter:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de vehículos')
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig_scatter, use_container_width=True)