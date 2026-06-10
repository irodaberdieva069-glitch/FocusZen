import streamlit as st
import google.generativeai as genai

# Gemini API sozlamalari (o'z API kalitingni kirit)
genai.configure(api_key="API KEY")

st.set_page_config(page_title="FocusZen", layout="wide")

st.sidebar.title("FocusZen")
page = st.sidebar.radio("Menyu", ["Dars", "Kartalar", "AI Testlar"])

def get_ai_feedback(question, user_answer):
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"Savol: {question}. Foydalanuvchi javobi: {user_answer}. Bu javobni tahlil qil, to'g'ri yoki noto'g'riligini ayt va qisqa tushuntirish ber."
    response = model.generate_content(prompt)
    return response.text

if page == "AI Testlar":
    st.header("🤖 AI Bilim Sinovi")
    question = st.text_input("Savolingizni kiriting (masalan: 6-sinf matematika: ...)")
    answer = st.text_area("Javobingiz:")
    
    if st.button("Tahlil qilish"):
        with st.spinner("AI tahlil qilmoqda..."):
            feedback = get_ai_feedback(question, answer)
            st.markdown("### 📝 AI Tahlili:")
            st.write(feedback)

# Boshqa sahifalar (Dars va Kartalar avvalgidek qoladi)
