import streamlit as st

st.set_page_config(
    page_title="AI Interview Bot",
    page_icon="🎤"
)

st.title("🎤 AI Interview Bot")

st.write("Welcome! I will act as your AI interviewer.")

name = st.text_input("Enter your name")

role = st.selectbox(
    "Select your interview role",
    [
        "Python Developer",
        "AI/ML Engineer",
        "Web Developer",
        "Data Analyst"
    ]
)

if st.button("Start Interview"):

    if name:
        st.success(f"Welcome {name}! Your {role} interview is starting.")
        st.write("### Question 1")
        st.write("Tell me about yourself and your technical skills.")
    else:
        st.warning("Please enter your name.")