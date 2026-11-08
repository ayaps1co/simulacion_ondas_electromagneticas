import streamlit as st
import other as other


A = st.text_input("Ingresa tu amplitud", key='amplitud')
ax = st.text_input("Ingresa tu fase inicial", key='fase')
k = st.text_input("Ingresa tu numero de onda", key='numero_onda')
omega = st.text_input("Ingresa tu velocidad de propagacion", key='velocidad')
epsilon = st.text_input("Ingresa tu angulo de elipticidad", key='elipticidad')
if epsilon == "pi/4" or epsilon== "-pi/4":
    psi = "0" 
else:
    psi = st.text_input("Ingresa tu angulo angulo de inclinacion", key='inclinacion')


if st.button("Generar gráficas"):
    if A=="" or ax=="" or k=="" or omega=="" or epsilon =="" or psi == "":
        st.write("Complete todos los parametros...")
    else:
        other.graficas(A, ax, k, omega, epsilon, psi)    

