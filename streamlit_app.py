
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Admisión MCD", 
    page_icon="😵‍💫", 
    initial_sidebar_state="collapsed" 
)
st.sidebar.header("Admisión MCD")

st.subheader('¿Es dificil entrar a la Maestría en Ciencia de Datos?')
st.divider()

df_resumen = pd.read_excel(
    'data/Estadisticas-MCD.xlsx', 
    sheet_name='Aspirantes',
    header=3
)

c1, c2, c3 = st.columns(3)
with c1:
    st.metric(
        label="Aspirantes totales", 
        value= df_resumen['Num. Aspirantes'].sum(), 
        help="Acumulado de aspirantes del 2020, 2021, 2022, 2023 y 2024"
    )
with c2:
    st.metric(
        label="Aceptados", 
        value= (df_resumen['Aceptados nacional'].sum() + 
                df_resumen['Aceptado extranjero'].sum()), 
        help="Acumulado de aspirantes aceptados del 2020 al 2024"  
    )
with c3:
    st.metric(
        label="Aspirantes extranjeros", 
        value= df_resumen['Extranjeros'].sum(), 
        help="Acumulado de aspirantes extranjeros del 2020 al 2023"  
    )

st.divider()

df_resumen['Aceptados'] = (
    df_resumen['Aceptados nacional'] + df_resumen['Aceptado extranjero']
)

st.markdown("#### Aceptados por generación")
st.caption("Del resumen generado por el Sistema de Información de Posgrados (SIPO) de la Unison")
st.bar_chart(
    data=df_resumen, 
    x='Convocatoria', 
    y=['No aceptados', 'Aceptados']
)

st.button('¡Que felicidad!', on_click=st.balloons)

st.divider()


st.markdown("#### Y vamos ganando internacionalización")

df_resumen['No aceptado extranjero'] = (
    df_resumen['Extranjeros'] - df_resumen['Aceptado extranjero']
)

tab1, tab2, tab3 = st.tabs(["Bar", "Area", "Ploty"])

with tab1:
    st.markdown("#### Evolución de la demanda internacional por convocatoria")
    st.caption("Del resumen generado por el Sistema de Información de Posgrados (SIPO) de la Unison")
    st.bar_chart(
        data=df_resumen, 
        x='Convocatoria', 
        y=['No aceptado extranjero', 'Aceptado extranjero']
    )

with tab2:
    st.markdown("#### Evolución de la demanda internacional por convocatoria")
    st.caption("Del resumen generado por el Sistema de Información de Posgrados (SIPO) de la Unison")
    st.area_chart(
        data=df_resumen, 
        x='Convocatoria', 
        y=['No aceptado extranjero', 'Aceptado extranjero']
    )

with tab3:
    st.plotly_chart(
        px.bar(
            df_resumen, 
            x='Convocatoria', 
            y=['No aceptado extranjero', 'Aceptado extranjero'],
            title="Evolución de la demanda internacional por convocatoria"
        )
    )
    st.caption("Del resumen generado por el Sistema de Información de Posgrados (SIPO) de la Unison")

df = df_resumen[[
    'Convocatoria','Num. Aspirantes', 'Extranjeros',
    'Aceptados', 'Aceptados nacional', 'Aceptado extranjero',
    'No aceptados', 'No aceptado extranjero'
]].set_index('Convocatoria')

with st.expander("Ver los datos tabulares"):
    st.dataframe(df)
    