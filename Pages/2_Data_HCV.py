import streamlit as st #Decimo paso
import pandas as pd #Decimo paso
import matplotlib.pyplot as plt #Decimo paso

def plot_histogram(Column): #Decimo paso
   plt.figure(figsize=(6,4)) #Decimo paso
   plt.hist(data[Column], bins=20, color="purple", edgecolor="black") #Decimo paso
   plt.title(title) #Decimo paso
   plt.xlabel(Column) #Decimo paso
   plt.ylabel("Frecuency") #Decimo paso
   return plt #Decimo paso

def box_plot(Column): #Decimo paso
   plt.figure(figsize=(6,4)) #Decimo paso
   plt.boxplot(data[Column]) #Decimo paso
   plt.title(title) #Decimo paso
   plt.xlabel(Column) #Decimo paso
   plt.ylabel("Values") #Decimo paso
   return plt #Decimo paso

st.title("Análisis y Descripción de los Datos Seleccionados") #Decimo paso
st.markdown("---")
st.markdown("## Descripción General de la Data")
st.markdown("---")
st.write("""La base de datos definida para el desarrollo del proyecto final relaciona el conjunto de valores
          de laboratorio de donantes de sangre y pacientes con hepatitis C, junto a valores relacionados con 
          datos demográficos como la edad y sexo, entre otros.""")
st.write("""La información de la base de datos actual se ha obtenido del repositorio de datos de Machine Learning 
          (https://archive.ics.uci.edu/), especificamente en el HCV data, donado por Ralf Lichtinghagen, Frank 
          Klawonn y Georg Hoffman, quienes a partir del caso de estudio definido en el artículo 'Using machine 
          learning techniques to generate laboratory diagnostic pathways—a case study', logran obtener los datos.
          """)

data0=pd.read_csv("Models\Data\HCV_Data.csv") #Decimo paso

st.dataframe(data0) 
st.write("""Una vez definida la base de datos, al momento de realizar un primer reconocimiento se observa que esta 
         cuenta con 13 variables, siendo únicamente 1 variable categórica la definida como el label y las restantes 
         12 variables se llegaran a considerar como features, debido a que condicionaran la posible respuesta.""")
st.write("""Sin embargo, a fin de aportar más claridad se procederá a indicar los nombres de cada una de las 
         variables asi: """)
col1, col2=st.columns(2) 

with col1:
   st.info("""
      1. Diagnostico (diagnosis),
      2. Edad (Age),
      3. Género Biológico (Sex),
      4. Albúmina (ALB),
      5. ALP,
      6. Alanina aminotransferasa (ALT),
      7. Aspartato amino- transferasa (AST),
         """)   

with col2: 
   st.info("""
	         8. Bilirrubina (BIL),
	         9. Colina esterasa (CHE),
	         10. CHOL,
	         11. CREA,
	         12. γ-glutamil-transferasa (GGT),
	         13. PROT
         """)

st.markdown("---")
st.subheader("Descripción estadistica de las variables relacionadas") 
st.markdown("---")

#(values: '0=Blood Donor', '0s=suspect Blood Donor', '1=Hepatitis', '2=Fibrosis', '3=Cirrhosis')
# st.write("""Debido a la denominación de los labels, se procede para un mejor manejo de los datos a modificar 
#          su abreviatura por 'BD', 'SBD', 'H', 'F' y 'C'.
#          """)

# name_clases={'0=Blood Donor':"BD", '0s=suspect Blood Donor':"SBD",'1=Hepatitis':"H",
#              '2=Fibrosis':"F",'3=Cirrhosis':"C"} #Decimo paso
# data0["HCV_Data"]=data0["HCV_Data"].replace(name_clases) #Decimo paso

st.dataframe(data0.describe())

col1, col2=st.columns(2) #Decimo paso

with col1: #Decimo paso
   title="Histogram of Features" #Decimo paso
   selected_Column_a=st.selectbox("Select Column",data0.columns) #Decimo paso
   # st.pyplot(plot_histogram(selected_Column_a,f"Histograma de {selected_Column_a}"))
   # st.pyplot(plot_histogram(selected_Column_a, f"Histogram of {selected_Column_a}")) #Decimo paso
   # st.dataframe(selected_Column_a) 
   st.bar_chart(df0) 


with col2: #Decimo paso
   title="Boxplot of Features" #Decimo paso
   selected_column=st.selectbox("Select other Column",data0.columns) #Decimo paso
   # selected_Column_b=st.selectbox("Select Column",data0.columns) #Decimo paso
   # st.pyplot(box_plot(selected_column,f"Histograma de {selected_column}"))
   # st.pyplot(box_plot(selected_Column_b, f"Boxplot of {selected_Column_b}")) #Decimo paso

st.markdown("---") #Decimo paso

   