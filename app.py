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

if "scores" not in st.session_state:
    st.session_state.scores = []

if "evaluated" not in st.session_state:
    st.session_state.evaluated = False


# -----------------------------
# Generate Question
# -----------------------------

def generate_question(role, question_number):

    prompt = f"""
You are a professional technical interviewer.

The candidate is applying for the role of {role}.

Ask ONE technical interview question.

This is question number {question_number}.

Do not provide the answer.
Do not ask multiple questions.
"""

    response = llm.invoke(prompt)

    return response.content


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
# Start Interview
# -----------------------------

if st.button("Start Interview"):

    if not name:
        st.warning("Please enter your name.")

    else:

        st.session_state.role = role
        st.session_state.question_number = 1
        st.session_state.scores = []
        st.session_state.evaluated = False

        with st.spinner("Preparing your interview..."):

            st.session_state.question = generate_question(
                role,
                1
            )

        st.success("Interview Started!")

        st.rerun()


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

Evaluate the answer.

IMPORTANT:
Start your response with exactly this format:

Score: X/10

Then provide:

## Strengths
What did the candidate do well?

## Improvements
What should the candidate improve?

## Correct Explanation
Give the correct explanation.
"""

            with st.spinner("Evaluating your answer..."):

                evaluation = llm.invoke(
                    evaluation_prompt
                )

            evaluation_text = evaluation.content

            st.subheader("📊 Interview Evaluation")

            st.markdown(evaluation_text)

            # Extract score
            try:

                score_text = evaluation_text.split(
                    "Score:"
                )[1].split("/10")[0].strip()

                score = float(score_text)

                st.session_state.scores.append(score)
                st.session_state.evaluated = True

            except:

                st.warning(
                    "Score could not be automatically detected."
                )


    # -------------------------
    # Next Question
    # -------------------------

    if st.session_state.evaluated:

        if st.button(
            "Next Question",
            key=f"next_{st.session_state.question_number}"
        ):

            st.session_state.question_number += 1

            st.session_state.evaluated = False

            with st.spinner("Preparing next question..."):

                st.session_state.question = generate_question(
                    st.session_state.role,
                    st.session_state.question_number
                )

            st.rerun()


# -----------------------------
# Final Report
# -----------------------------

if len(st.session_state.scores) >= 3:

    st.divider()

    st.header("🏆 Final Interview Report")

    total_score = sum(st.session_state.scores)

    average_score = total_score / len(
        st.session_state.scores
    )

    st.metric(
        "Overall Score",
        f"{average_score:.1f}/10"
    )

    st.write(
        f"Questions Evaluated: {len(st.session_state.scores)}"
    )

    if average_score >= 8:

        st.success(
            "Excellent performance! You are well prepared."
        )

    elif average_score >= 6:

        st.info(
            "Good performance, but there is room for improvement."
        )

    else:

        st.warning(
            "Keep practicing your technical concepts."
        )