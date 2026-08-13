import streamlit as st
import re

from utils import (
    generate_question,
    evaluate_answer,
    generate_final_report
)


# Page settings
st.set_page_config(
    page_title="AI Interview Bot",
    page_icon="🤖"
)


# Title
st.title("🤖 AI Interview Bot")
st.write("Practice your technical interview with AI.")


# ---------------- INTERVIEW SETTINGS ----------------

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


difficulty = st.selectbox(
    "Choose difficulty level:",
    [
        "Easy",
        "Medium",
        "Hard"
    ]
)


# ---------------- SESSION STATE ----------------

if "question" not in st.session_state:
    st.session_state.question = None

if "feedback" not in st.session_state:
    st.session_state.feedback = None

if "scores" not in st.session_state:
    st.session_state.scores = []

if "history" not in st.session_state:
    st.session_state.history = []

if "final_report" not in st.session_state:
    st.session_state.final_report = None


# ---------------- RESET INTERVIEW ----------------

if st.sidebar.button("🔄 Reset Interview"):

    st.session_state.question = None
    st.session_state.feedback = None
    st.session_state.scores = []
    st.session_state.history = []
    st.session_state.final_report = None

    st.rerun()


# ---------------- GENERATE QUESTION ----------------

if st.button("🎯 Generate Question"):

    with st.spinner("Generating interview question..."):

        st.session_state.question = generate_question(
            topic,
            difficulty
        )

    st.session_state.feedback = None


# ---------------- DISPLAY QUESTION ----------------

if st.session_state.question:

    st.subheader("📝 Interview Question")

    st.write(st.session_state.question)

    answer = st.text_area(
        "Your Answer:",
        height=150
    )


    # ---------------- SUBMIT ANSWER ----------------

    if st.button("✅ Submit Answer"):

        if not answer.strip():

            st.warning("Please enter your answer.")

        else:

            with st.spinner("AI is evaluating your answer..."):

                feedback = evaluate_answer(
                    st.session_state.question,
                    answer
                )

                st.session_state.feedback = feedback


                # Extract score
                score_match = re.search(
                    r"Score:\s*(\d+(?:\.\d+)?)\s*/\s*10",
                    feedback
                )


                if score_match:

                    score = float(
                        score_match.group(1)
                    )

                    st.session_state.scores.append(
                        score
                    )


                    # Save history
                    st.session_state.history.append(
                        {
                            "question": st.session_state.question,
                            "answer": answer,
                            "score": score
                        }
                    )


    # ---------------- DISPLAY FEEDBACK ----------------

    if st.session_state.feedback:

        st.subheader("📊 AI Evaluation")

        st.markdown(
            st.session_state.feedback
        )


        # Next Question
        if st.button("➡️ Next Question"):

            with st.spinner(
                "Generating next question..."
            ):

                st.session_state.question = (
                    generate_question(
                        topic,
                        difficulty
                    )
                )

            st.session_state.feedback = None

            st.rerun()


# ---------------- SIDEBAR PROGRESS ----------------

if st.session_state.scores:

    st.sidebar.subheader(
        "📊 Interview Progress"
    )

    st.sidebar.write(
        f"Questions Attempted: "
        f"{len(st.session_state.scores)}"
    )


    average_score = (
        sum(st.session_state.scores)
        / len(st.session_state.scores)
    )


    st.sidebar.metric(
        "Overall Score",
        f"{average_score:.1f}/10"
    )


# ---------------- INTERVIEW HISTORY ----------------

if st.session_state.history:

    st.subheader("📚 Interview History")

    for i, item in enumerate(
        st.session_state.history
    ):

        with st.expander(
            f"Question {i + 1} — "
            f"Score: {item['score']}/10"
        ):

            st.write("**Question:**")
            st.write(item["question"])

            st.write("**Your Answer:**")
            st.write(item["answer"])


# ---------------- FINAL REPORT ----------------

if st.session_state.scores:

    st.subheader(
        "🏆 Final Interview Report"
    )


    total_questions = len(
        st.session_state.scores
    )


    average_score = (
        sum(st.session_state.scores)
        / total_questions
    )


    st.write(
        f"**Questions Attempted:** "
        f"{total_questions}"
    )

    st.write(
        f"**Average Score:** "
        f"{average_score:.1f}/10"
    )


    if average_score >= 8:

        performance = "Excellent 🚀"

    elif average_score >= 6:

        performance = "Good 👍"

    elif average_score >= 4:

        performance = "Average 🙂"

    else:

        performance = "Needs Improvement 💪"


    st.write(
        f"**Overall Performance:** "
        f"{performance}"
    )


    # AI Final Report
    if st.button(
        "🤖 Generate AI Final Report"
    ):

        with st.spinner(
            "AI is analyzing your performance..."
        ):

            st.session_state.final_report = (
                generate_final_report(
                    st.session_state.history
                )
            )


# ---------------- DISPLAY AI REPORT ----------------

if st.session_state.final_report:

    st.subheader(
        "🤖 AI Performance Analysis"
    )

    st.markdown(
        st.session_state.final_report
    )