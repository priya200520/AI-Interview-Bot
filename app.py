import streamlit as st
from utils import generate_question, evaluate_answer


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


# Generate question
if st.button("Generate Question"):

    question = generate_question(topic)

    st.session_state.question = question


# Display question
if "question" in st.session_state:

    st.subheader("📝 Interview Question")

    st.write(st.session_state.question)

    answer = st.text_area(
        "Your Answer:",
        height=150
    )


    # Evaluate answer
    if st.button("Submit Answer"):

        if not answer.strip():

            st.warning("Please enter your answer.")

        else:

            with st.spinner("AI is evaluating your answer..."):

                feedback = evaluate_answer(
                    st.session_state.question,
                    answer
                )

            st.subheader("📊 AI Evaluation")

            st.markdown(feedback)