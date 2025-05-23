import streamlit as st
import pandas as pd
import numpy as np

st.write("""
# Pesquisa de preferências
Olá aluno(a) da FGV Comunicação! Responda *sabiamente* as perguntas abaixo:
""")

st.text_input("Digite seu nome:")
st.text_input("Digite sua idade:")
st.text_input("Digite o seu período:")

prof = st.selectbox(
    "Qual o seu professor favorito do 1 período da ECMI?",
    ("Eurico", "Josir", "Matheus", "Renata", "Victor"),
)

if prof == "Josir":
    st.write("Ótima escolha!")

disciplina = st.selectbox(
    "Qual a sua disciplina preferida do 1 período?",
    ("Ciências de Dados", "Ciências Sociais", "Comunicação e Cultura Digital", "Programação", "Teorias da Comunicação"),
)

if disciplina == "Programação":
    st.write("Ótima escolha!")

st.write("Obrigada!")
