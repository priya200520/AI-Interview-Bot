import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)

st.set_page_config(
    page_title="AI Interview Bot",
    page_icon="🎤"
)

st.title("🎤 AI Interview Bot")

st.write("Gemini connection test")

if st.button("Test Gemini"):

    response = llm.invoke(
        "Ask me one Python interview question."
    )

    st.success("Gemini is working!")

    st.write(response.content)