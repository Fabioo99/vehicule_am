import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit import checkbox

car_data = pd.read_csv("vehicles_us.csv")
st.header('Elige una opcion')
hist_checkbox = checkbox("Mostrar histograma del odómetro")
disp_checkbox = checkbox("Mostrar diagrama de dispersión (odómetro vs precio)")


if hist_checkbox:
    st.write('Creación de un histograma del odómetro')
    fig = px.histogram(car_data, x='odometer',
                       title="Distribución del Odómetro",
                       labels={"odometer": "Kilometraje ( millas )"})
    st.plotly_chart(fig, use_container_width=True)

if disp_checkbox:
    st.write('Creación de un diagrama de dispersión (odómetro vs precio)')
    fig = px.scatter(car_data, x="odometer", y="price", color="paint_color",
                     title="Dispersión de precio vs. odómetro por marca",
                     labels={"odometer": "Kilometraje", "price": "Precio"},
                     hover_name="model",
                     hover_data=["model_year"])
    st.plotly_chart(fig)
