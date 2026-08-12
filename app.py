import streamlit as st
import re

from utils import generate_question, evaluate_answer


# Page settings
st.set_page_config(
    page_title="AI Interview Bot",
    page_icon="🤖"
)


st.title("🤖 AI Interview Bot")

st.write("Practice your technical interview with AI.")


# Topic selection
topic = st.selectbox(
    "Choose an interview topic:",
    [
        "Python",
        "SQL",
        "DBMS",
        "DSA",
        "OOPs",
        "Web Development"
    ]
)


# Session state
if "question" not in st.session_state:
    st.session_state.question = None

if "feedback" not in st.session_state:
    st.session_state.feedback = None

if "scores" not in st.session_state:
    st.session_state.scores = []


# Generate question
if st.button("Generate Question"):

    st.session_state.question = generate_question(topic)
    st.session_state.feedback = None


# Display question
if st.session_state.question:

    st.subheader("📝 Interview Question")

    st.write(st.session_state.question)

    answer = st.text_area(
        "Your Answer:",
        height=150
    )


    # Submit answer
    if st.button("Submit Answer"):

        if not answer.strip():

            st.warning("Please enter your answer.")

        else:

            with st.spinner("AI is evaluating your answer..."):

                feedback = evaluate_answer(
                    st.session_state.question,
                    answer
                )

                st.session_state.feedback = feedback


                # Extract score from AI response
                score_match = re.search(
                    r"Score:\s*(\d+(?:\.\d+)?)\s*/\s*10",
                    feedback
                )


                if score_match:

                    score = float(score_match.group(1))

                    st.session_state.scores.append(score)


    # Display feedback
    if st.session_state.feedback:

        st.subheader("📊 AI Evaluation")

        st.markdown(st.session_state.feedback)


        # Next question
        if st.button("Next Question"):

            st.session_state.question = generate_question(topic)

            st.session_state.feedback = None

            st.rerun()


# Sidebar progress
if st.session_state.scores:

    st.sidebar.subheader("📊 Interview Progress")

    st.sidebar.write(
        f"Questions Attempted: {len(st.session_state.scores)}"
    )


    # Overall score
    average_score = sum(st.session_state.scores) / len(
        st.session_state.scores
    )

    st.sidebar.metric(
        "Overall Score",
        f"{average_score:.1f}/10"
    )