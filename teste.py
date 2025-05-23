import streamlit as st
import pandas as pd
import numpy as np

st.write("""
# Pesquisa de preferências
Olá aluno(a)! Responda sabiamente as perguntas abaixo:
""")

st.text_input("Digite seu nome:")
st.text_input("Digite sua idade:")
st.text_input("Digite o seu período:")

option = st.selectbox(
    "Qual o seu professor favorito do 1 período da ECMI?",
    ("Eurico", "Josir", "Matheus", "Renata", "Victor"),
)

st.write("Você escolheu:", option)
