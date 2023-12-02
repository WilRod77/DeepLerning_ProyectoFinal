import streamlit as st

st.title("Oportunidades de Implementación en Streamlit")

st.markdown("---")
st.markdown("## Elementos Estáticos")
st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    st.write("Texto sin Resalte")
    st.markdown("""#
            Espacios para relacionar texto 
            
            -[x] Bullet
            * Viñeta de simbolo
            1. Viñeta numérica
            a. Viñeta de alfabeto
            
            
            """)
    st.write("Relación de texto normal tipo párrafo")
    
with col2:
    st.write("Resalte de texto")
    st.success("Exitoso!!")
    st.info("Inforación")
    st.warning("Warning")
    st.error("Error")

st.markdown("---")
st.markdown("## Elementos Dinámicos")
st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    st.checkbox("Checkbox")
    st.button("Button")
    st.multiselect("Multiselect",("Option 1","Option 2"))
    st.slider("Slider",0,100)
    st.date_input("Date_input")
    
with col2:
    st.radio("Radio Multiselect",("Option 1","Option 2"))
    st.selectbox("Selectbox",("Option 1","Option 2"))
    st.select_slider("Select_slider",("Option 1","Option 2"))
    st.time_input("Time_input")

st.text_input("Text_input")

st.markdown("---")
st.markdown("## Elementos de Entrada de Información")
st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    st.file_uploader("File_uploader")#Tercer paso
    Var2=st.radio("Radio Multiselect2",("Option 1","Option 2"))
    st.success("Ud selecciono: "+Var2)    

with col2:
    Entrada_Texto=st.text_input("Text_input2")#Cuarto paso
    st.success(Entrada_Texto)
    Var=st.selectbox("Selectbox2",("Option 1","Option 2"))#Cuarto paso
    st.success("Ud selecciono: "+Var)


st.markdown("---")
st.markdown("## Elementos Gráficos")
st.markdown("---")

import pandas as pd 

col1, col2 = st.columns(2)
with col1:
    data={"data":[1,2,1,3,2,4,4,2,4]} 
    df=pd.DataFrame(data) 
    st.dataframe(df) 
    st.bar_chart(df) 

with col2:
    st.line_chart(df) 
    st.area_chart(df) 

st.markdown("---")
st.markdown("## Otros Elementos")
st.markdown("---")

file=st.file_uploader("Sube un archivo con extensión .xlsx",type=["xlsx"]) #Noveno paso

if file is not None: #Noveno paso
   df=pd.read_excel(file) #Noveno paso
   st.write("datos del archivo: "+file.name) #Noveno paso
   st.dataframe(df) #Noveno paso

import time 
latest_iteration = st.empty() 
bar = st.progress(0) 

for i in range(100): 
    latest_iteration.text(f'Iteration {i+1}') 
    bar.progress(i + 1)  
    time.sleep(0.1)  

st.markdown("---")
st.markdown("Elaborado por: Wilmar Guillermo Rodriguez Lopez")
st.markdown("---")