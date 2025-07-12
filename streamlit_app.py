import streamlit as st
import json
from quiz import start_quiz

# Load data elemen
with open('periodic_table_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

st.set_page_config(page_title="Tabel Periodik Interaktif", layout="wide")
st.title("🧪 Tabel Periodik Interaktif")

menu = st.sidebar.radio("Menu", ["Tabel Periodik", "Kuis"])

if menu == "Tabel Periodik":
    st.subheader("Pilih Kategori Elemen:")
    kategori = st.selectbox("Kategori", sorted(set([el['category'] for el in data])))

    filtered = [el for el in data if el['category'] == kategori]

    for el in filtered:
        with st.expander(f"{el['symbol']} - {el['name']}"):
            st.markdown(f"""
            **Nomor Atom:** {el['number']}  
            **Simbol:** {el['symbol']}  
            **Nama:** {el['name']}  
            **Massa Atom:** {el['atomic_mass']}  
            **Kategori:** {el['category']}  
            **Elektronegativitas:** {el.get('electronegativity', 'N/A')}  
            **Konfigurasi Elektron:** {el.get('electron_configuration', 'N/A')}
            """)

elif menu == "Kuis":
    start_quiz(data)
