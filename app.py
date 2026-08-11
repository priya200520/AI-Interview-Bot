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

st.write("Practice your technical interview with AI.")

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

    if not name:
        st.warning("Please enter your name.")

    else:

        prompt = f"""
You are a professional technical interviewer.

The candidate's name is {name}.
The candidate is applying for the role of {role}.

Ask ONE technical interview question suitable for this role.

Do not provide the answer.
Do not ask multiple questions.

Question:
"""

        with st.spinner("Preparing your interview question..."):
            response = llm.invoke(prompt)

        st.success("Interview Started!")

        st.subheader("Question 1")

        question = response.content

        st.write(question)

        answer = st.text_area(
            "Your Answer",
            placeholder="Type your answer here..."
        )

        if st.button("Evaluate Answer"):

            if not answer:
                st.warning("Please enter your answer.")

            else:

                evaluation_prompt = f"""
You are an expert technical interviewer.

The candidate is applying for the role of {role}.

Interview Question:
{question}

Candidate Answer:
{answer}

Evaluate the candidate's answer.

Give the evaluation in this format:

## Score
Give a score out of 10.

## Strengths
Mention what the candidate did well.

## Improvements
Mention what the candidate should improve.

## Correct Explanation
Give a clear and correct explanation of the concept.
"""

                with st.spinner("Evaluating your answer..."):
                    evaluation = llm.invoke(evaluation_prompt)

                st.subheader("📊 Interview Evaluation")

                st.markdown(evaluation.content)