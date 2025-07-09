import streamlit as st

st.title("📝 Latihan Soal Reaksi Organik")

question = "Apa hasil dari reaksi alkena dengan HBr menurut aturan Markovnikov?"
options = ["Alkohol primer", "Alkil bromida", "Eter", "Amina"]
answer = "Alkil bromida"

choice = st.radio(question, options)

if st.button("Cek Jawaban"):
    if choice == answer:
        st.success("Jawaban benar!")
    else:
        st.error(f"Jawaban salah. Jawaban yang benar adalah: {answer}.")
