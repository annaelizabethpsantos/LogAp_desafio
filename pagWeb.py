import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.sidebar.title('Menu')
paginaSelecionada = st.sidebar.selectbox('Selecione uma página', ['Página de Plotagem', 'Algoritmo resolvido'])

if paginaSelecionada == 'Página de Plotagem':

    def main():
        file = st.file_uploader("Escolha um arquivo para upload:", type = ["csv"])
        show_file = st.empty()

        if not file:
            show_file.info("Escolha um arquivo para upload do tipo {}".format(' '.join(["csv"])))
            return
 
        df = pd.read_csv(file, sep = ';')
        st.dataframe(df)
        df.plot.scatter(x='Velocidade do vento (m/s)', y='Potência (kWh)')
        st.pyplot()
    main()

elif paginaSelecionada == 'Algoritmo resolvido':
    n = []
    st.title('Soma')
    sentence = st.text_input('Insira os números:') 
    n.append(sentence)
    for numero in n:
        st.write(numero)
        
    sentence2 = st.text_input('Insira um número para validação:') 
    n2 = sentence2
    if sentence2:
        st.write(sentence2)

    for i in numero:
        for j in numero:
            if numero [i] + numero[j] == n2:
                st.write(numero[i])
                st.write(numero[j])
