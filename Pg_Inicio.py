import streamlit as st

#Encabezado Primera Página
st.set_page_config(page_title="Proy_Final", page_icon=":D") #Primer paso
st.title("UAM - UAO - UNAB - UPTC | Doctorado en Ingeniería") #Primer paso
st.header("Curso: Deep Learning Avanzado | PhD. Ing. Reinel Tabares Soto") #Primer paso
st.subheader("Proyecto Final | Ing. Wilmar Guillermo Rodriguez Lopez")#Primer paso

#Descripción de la actividad
st.markdown("---")#Tercer paso
st.markdown("## Descripción General del Proyecto")#Primer paso
st.markdown("---")#Tercer paso
st.write("""En el presente proyecto se propenderá por la creación de una arquitectura 
         de Deep Learning que aborde como tarea específica la regresión, a partir de 
         la utilización de un conjunto de datos disponibles.""")
st.write("""Aún cuando se define la posibilidad de abordar los datos del proyecto, en 
         la actualidad el proyecto ha presentado dificultad para la obtención de los 
         mismos, por lo tanto se propone el empleo de un conjunto de datos de XXXXX 
         disponible en XXXX.""")
st.write('En este sentido se definen las siguientes actividades a fin de dar cumplimiento a lo solicitado: ')
st.markdown("""#
    1. Elaboración de una arquitectura de Deep Learning apropiada para el conjunto 
    de datos seleccionado.
    2. Entrenamiento del modelo en la tarea específica.
    3. Implementación de una interfaz interactiva utilizando la plataforma Streamlit 
    en Python.
""")
st.write("""En relación con lo anterior, se indicarán varias páginas en la barra lateral relacionadas con a.
         Contexto de la propuesta doctoral, b. Análisis y descripción del conjunto de datos seleccionado, c. 
         Interfaz interectiva con el modelo y arquitectura propuestas para el conjunto de datos.
         """)
st.markdown("---")

#Ajustes Barra Lateral

st.sidebar.title("Doctorado en Ingeniería")
st.sidebar.header("Deep Learning Avanzado")
st.sidebar.subheader("Proyecto Final")

# st.markdown("<h1 style='text-align: center;'>Análisis hidro-climático Tunja Boyacá</h1>", unsafe_allow_html=True)
st.markdown("Elaborado por: Wilmar Guillermo Rodriguez Lopez")
st.markdown("---")