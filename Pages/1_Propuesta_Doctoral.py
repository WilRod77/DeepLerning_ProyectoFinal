import streamlit as st #Noveno paso
import pandas as pd #Noveno paso

st.title("Contextualización Propuesta Doctoral") #Noveno paso
st.markdown("---")
st.markdown("## Título")
st.markdown("---")
st.success("""Aplicación de Aprendizaje por Refuerzo y Series de Tiempo para el Análisis 
         de Pronostico del Inventario Cooperativo de Medicamentos de Alto Costo Mediante 
         la integración de Técnicas de Aprendizaje por Refuerzo y Series de tiempo. 
""")

st.markdown("---")
st.markdown("## Resumen")
st.markdown("---")
st.write("""La adecuada gestión de los inventarios de las cadenas de suministro medico permiten
          incrementar el bienestar social, a partir de reducir la tasa de mortalidad por falta 
         de disponibilidad de los medicamentos. Estas presentan al igual que la mayoría de las 
         cadenas de suministro dificultad para adquirir, administrar y gestionar sus suministros,
          siendo los medicamentos en el caso particular. Donde la incertidumbre de la demanda de 
         los medicamentos es una de las mayores problemáticas en la gestión de las instituciones 
         médicas. En el mismo sentido se ha observado que esta demanda presenta fluctuaciones, 
         debido a diversos factores dentro de los cuales se pueden destacar la introducción de 
         nuevos medicamentos especializados, introducción de nuevas marcas y aumentos de precios 
         de medicamentos aún protegidos por patentes, entre otros. asimismo, se observa que como 
         consecuencia de la falta de previsión de la demanda un impacto negativo en los costos, 
         disponibilidad, gestión, logística e inventarios. Por lo cual, la presente investigación 
         propone el desarrollo de un modelo predictivo y un novedoso modelo de inventarios denominado
          Inventario Cooperativo, en relación a la demanda de los Medicamentos de Alto Costo (MAC). 
         Siendo estos definidos como medicamentos diseñados o enfocados para tratar enfermedades poco 
         comunes, muy caras, con alto índice de mortalidad y cuyos tratamientos tienen un alto costo 
         terapéutico. El desarrollo propuesto buscará ofrecer una manera de gestionar los inventarios
          de los MAC, primero determinando la previsión de la demanda y luego a partir de la gestión 
         de los inventarios. Donde el pronóstico se enfocará en los modelos de programación profunda 
         basada en aprendizaje por refuerzo al considerarse más rápidos y eficientes.  
""")

st.markdown("---")
st.markdown("## Pregunta de Investigación")
st.markdown("---")

st.write("""#
         ¿Cómo gestionar la predicción demanda de inventario cooperativo de los medicamentos de 
         alto costo mediante la aplicación de aprendizaje por refuerzo y series de tiempo?
         """)

st.markdown("---")
st.markdown("## Aportes al conocimiento y recursos necesarios")
st.markdown("---")
col1, col2 = st.columns(2)
with col1:
   st.subheader("Aportes al conocimiento")
   st.info("""
            1. Modelo de inventario cooperativo para la cadena de suministro medico.
            2. Arquitéctura lógica del algoritmo de predicción.
            3. Algoritmo de pronostico del inventario de los medicamentos de alto costo.
            4. Evaluación del modelo de inventario cooperativo y algoritmo de pronostico.
            5. Levantamiento del estado del arte de la cadena de suministro médico
            """)
with col2:
   st.subheader("Recursos necesarios")
   st.warning("""
              1. Base de datos de medicamentos de alto costo.
              2. Modelos de aprendizaje por refuerzo y series de tiempo existentes.
              3. Modelos de inventarios existentes.
              4. Modelos de predicción de demanda de medicamentos.
              5. Bases de datos para consulta de información.
              6. Software y harware necesarios.
              """)


st.markdown("---")
st.markdown("## Base de datos actual")
st.markdown("---")
st.write("""La base de datos actual se ha obtenido del ministerio de la salud en el siguiente enlace: 
         https://datos.gov.co/Salud-y-Protecci-n-Social/C-DIGO-NICO-DE-MEDICAMENTOS-VIGENTES/i7cb-raxc/data
         """)
import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt 

data=pd.read_csv("Models\Data\Current_Medicines.csv")

st.dataframe(data) 

st.subheader("Descripción estadística de los medicamentos vigentes") 
st.dataframe(data.describe()) 
st.write("""
         Se observa que aún cuando la base de datos cuenta con un total de 114,930 medicamentos reportados por
          el Ministerio de salud, realmente es necesario considerar una revisión detallada de esta, ya que al 
         momento no se ha logrado identificar como las variables relacionadas (categóricas y numéricas), pueden
          generar un aporte significativo a la propuesta considerada.
         """)
st.markdown("---") 