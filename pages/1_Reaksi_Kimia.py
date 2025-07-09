import streamlit as st

st.title("🔁 Prediksi Reaksi Organik")

reaction = st.text_input("Masukkan Reaksi (contoh: alkene + HBr)")

if reaction:
    if "alkene" in reaction.lower() and "hbr" in reaction.lower():
        st.success("Produk: Alkil bromida (mengikuti aturan Markovnikov)")
        st.image("images/alkyl_bromide_example.png", caption="Contoh Produk")
        st.markdown("**Penjelasan:** Reaksi adisi elektrofilik di mana H⁺ menyerang karbon lebih kaya elektron, dan Br⁻ masuk ke karbon lainnya.")
    else:
        st.warning("Reaksi belum tersedia dalam database.")
