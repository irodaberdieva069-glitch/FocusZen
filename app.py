import streamlit as st
import time
import random

# Sahifa sozlamalari
st.set_page_config(page_title="FocusZen", layout="wide")

# CSS dizayn
st.markdown("""
    <style>
    .card { background-color: #f8f9fa; padding: 20px; border-radius: 15px; border: 1px solid #dee2e6; text-align: center; height: 250px; }
    .stButton>button { width: 100%; border-radius: 10px; }
    </style>
""", unsafe_allow_html=True)

# Session state boshqaruvi
if 'page' not in st.session_state: st.session_state.page = "Home"

# Asosiy menyu (Kartalar)
def home_page():
    st.title("🎯 FocusZen")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="card"><h3>📚 Dars</h3><br>Pomodoro taymer va vazifalar.</div>', unsafe_allow_html=True)
        if st.button("Darsni boshlash"): st.session_state.page = "Study"
    with col2:
        st.markdown('<div class="card"><h3>🗂️ Kartalar</h3><br>So\'z yodlash mashqi.</div>', unsafe_allow_html=True)
        if st.button("Kartalarni ochish"): st.session_state.page = "Cards"
    with col3:
        st.markdown('<div class="card"><h3>🎮 O\'yin</h3><br>Matematika sprinti.</div>', unsafe_allow_html=True)
        if st.button("O\'yinni boshlash"): st.session_state.page = "Game"

# Dars sahifasi
def study_page():
    st.title("📚 Dars vaqti")
    if st.button("⬅️ Orqaga"): st.session_state.page = "Home"; st.rerun()
    
    if st.button("25 daqiqa darsni boshlash"):
        with st.empty():
            for s in range(25 * 60, 0, -1):
                st.write(f"### Qolgan vaqt: {divmod(s, 60)[0]}:{divmod(s, 60)[1]:02d}")
                time.sleep(1)
        st.success("Barakalla! Tanaffus!")

# Kartalar sahifasi
def cards_page():
    st.title("🗂️ Kartalar")
    if st.button("⬅️ Orqaga"): st.session_state.page = "Home"; st.rerun()
    
    data = {"Apple": "Olma", "Code": "Kod", "Screen": "Ekran"}
    word = random.choice(list(data.keys()))
    
    if st.button("Kartani o'girish"):
        st.info(f"Tarjimasi: {data[word]}")
    st.write(f"### So'z: {word}")

# O'yin sahifasi
def game_page():
    st.title("🎮 Matematika Sprint")
    if st.button("⬅️ Orqaga"): st.session_state.page = "Home"; st.rerun()
    
    a, b = random.randint(1, 10), random.randint(1, 10)
    ans = st.number_input(f"{a} * {b} = ?", step=1)
    if st.button("Tekshirish"):
        if ans == a * b: st.success("To'g'ri!")
        else: st.error("Xato!")

# Sahifa navigatsiyasi
if st.session_state.page == "Home": home_page()
elif st.session_state.page == "Study": study_page()
elif st.session_state.page == "Cards": cards_page()
elif st.session_state.page == "Game": game_page()
