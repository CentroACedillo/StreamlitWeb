import streamlit as st

name = st.text_input("Your name", "Andrés")
age = st.slider("Your age", 0,100, 32)

st.write(f"Hola, {name}. Tienes {age} años.")