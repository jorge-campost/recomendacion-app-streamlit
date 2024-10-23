import streamlit as st
import pandas as pd


# carga de las tablas de consulta
data_clientes = pd.read_csv("data_clientes.csv", sep=",", index_col=0)
recomendaciones = pd.read_csv("recomendaciones.csv", sep=",", index_col=0)

# Layout
st.title("Sistema de recomendaciones")

col1, col2 = st.columns(2)

id = col1.number_input("Ingres el N° de id del usuario:", min_value=1, step=1)

col2.write("")
is_clicked = col2.button("Buscar")

if is_clicked:

    data_clientes = data_clientes[data_clientes["id"] == id]

    if not data_clientes.empty:
        st.dataframe(data_clientes, hide_index=True)
        cluster = data_clientes.iloc[0].cluster

        recomendaciones_cliente = recomendaciones[recomendaciones["id_cliente"] == id]
        st.write("Productos recomendados:")
        st.dataframe(recomendaciones_cliente, hide_index=True)
    else:
        st.write("No hay datos del usuario solicitado")
