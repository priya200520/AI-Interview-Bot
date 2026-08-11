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

# -----------------------------
# Session State
# -----------------------------

if "question" not in st.session_state:
    st.session_state.question = None

if "question_number" not in st.session_state:
    st.session_state.question_number = 0

if "role" not in st.session_state:
    st.session_state.role = None


# -----------------------------
# Candidate Details
# -----------------------------

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


# -----------------------------
# Generate Question
# -----------------------------

def generate_question(role, question_number):

    prompt = f"""
You are a professional technical interviewer.

The candidate is applying for the role of {role}.

This is question number {question_number}.

Ask ONE technical interview question suitable
for this role.

Do not provide the answer.
Do not ask multiple questions.

Question:
"""

    response = llm.invoke(prompt)

    return response.content


# -----------------------------
# Start Interview
# -----------------------------

if st.button("Start Interview"):

    if not name:
        st.warning("Please enter your name.")

    else:

        st.session_state.role = role
        st.session_state.question_number = 1

        with st.spinner("Preparing your interview..."):

            st.session_state.question = generate_question(
                role,
                1
            )

        st.success("Interview Started!")


# -----------------------------
# Display Question
# -----------------------------

if st.session_state.question:

    st.subheader(
        f"Question {st.session_state.question_number}"
    )

    st.write(st.session_state.question)

    answer = st.text_area(
        "Your Answer",
        key=f"answer_{st.session_state.question_number}",
        placeholder="Type your answer here..."
    )

    # -------------------------
    # Evaluate Answer
    # -------------------------

    if st.button(
        "Evaluate Answer",
        key=f"evaluate_{st.session_state.question_number}"
    ):

        if not answer:

            st.warning("Please enter your answer.")

        else:

            evaluation_prompt = f"""
You are an expert technical interviewer.

The candidate is applying for the role of {st.session_state.role}.

Interview Question:
{st.session_state.question}

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
Give a clear and correct explanation.
"""

            with st.spinner("Evaluating your answer..."):

                evaluation = llm.invoke(
                    evaluation_prompt
                )

            st.subheader("📊 Interview Evaluation")

            st.markdown(evaluation.content)

    # -------------------------
    # Next Question
    # -------------------------

    if st.button(
        "Next Question",
        key=f"next_{st.session_state.question_number}"
    ):

        st.session_state.question_number += 1

        with st.spinner("Preparing next question..."):

            st.session_state.question = generate_question(
                st.session_state.role,
                st.session_state.question_number
            )

        st.rerun()