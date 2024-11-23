import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


st.set_page_config(
    page_title="Inspección de datos", 
    page_icon="🔍",
    initial_sidebar_state="collapsed"
)
st.sidebar.header("Inspección de datos")

st.subheader('Vamos a inspeccionar datos por convocatoria')
st.markdown("**usando [`streamlit-aggrid`](https://github.com/PablocFonseca/streamlit-aggrid)**")
st.divider()

option = st.selectbox(
    'Escoje la convocatoria',
    ('2020', '2021', '2022', '2023', '2024'))

df = pd.read_excel(
    'data/aspirantes_' + option + '.xlsx', 
)
AgGrid(df)