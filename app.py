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


question_limit = st.selectbox(
    "Choose number of questions:",
    [
        5,
        10,
        15
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

if "interview_completed" not in st.session_state:
    st.session_state.interview_completed = False


# ---------------- RESET INTERVIEW ----------------

if st.sidebar.button("🔄 Reset Interview"):

    st.session_state.question = None
    st.session_state.feedback = None
    st.session_state.scores = []
    st.session_state.history = []
    st.session_state.final_report = None
    st.session_state.interview_completed = False

    st.rerun()


# ---------------- INTERVIEW PROGRESS ----------------

questions_attempted = len(st.session_state.scores)

st.sidebar.subheader("📊 Interview Progress")

st.sidebar.write(
    f"Questions: {questions_attempted}/{question_limit}"
)

if st.session_state.scores:

    average_score = (
        sum(st.session_state.scores)
        / len(st.session_state.scores)
    )

    st.sidebar.metric(
        "Overall Score",
        f"{average_score:.1f}/10"
    )


# ---------------- GENERATE FIRST QUESTION ----------------

if not st.session_state.interview_completed:

    if st.button(
        "🎯 Generate Question",
        disabled=st.session_state.question is not None
    ):

        with st.spinner("Generating interview question..."):

            st.session_state.question = generate_question(
                topic,
                difficulty
            )

        st.session_state.feedback = None
        st.rerun()


# ---------------- DISPLAY QUESTION ----------------

if (
    st.session_state.question
    and not st.session_state.interview_completed
):

    st.subheader(
        f"📝 Question {questions_attempted + 1} of {question_limit}"
    )

    st.write(st.session_state.question)


    answer = st.text_area(
        "Your Answer:",
        height=150,
        key=f"answer_{questions_attempted}"
    )


    # ---------------- SUBMIT ANSWER ----------------

    if st.button("✅ Submit Answer"):

        if not answer.strip():

            st.warning("Please enter your answer.")

        elif st.session_state.feedback is None:

            with st.spinner("AI is evaluating your answer..."):

                feedback = evaluate_answer(
                    st.session_state.question,
                    answer
                )

                st.session_state.feedback = feedback


                score_match = re.search(
                    r"Score:\s*(\d+(?:\.\d+)?)\s*/\s*10",
                    feedback
                )


                if score_match:

                    score = float(score_match.group(1))

                    st.session_state.scores.append(score)

                    st.session_state.history.append(
                        {
                            "question": st.session_state.question,
                            "answer": answer,
                            "score": score
                        }
                    )

                st.rerun()


    # ---------------- DISPLAY FEEDBACK ----------------

    if st.session_state.feedback:

        st.subheader("📊 AI Evaluation")

        st.markdown(st.session_state.feedback)


        # Check if interview is completed
        if len(st.session_state.scores) >= question_limit:

            st.success(
                "🎉 Interview Completed! Check your final report below."
            )

            st.session_state.interview_completed = True
            st.session_state.question = None

            st.rerun()

        else:

            if st.button("➡️ Next Question"):

                with st.spinner("Generating next question..."):

                    st.session_state.question = generate_question(
                        topic,
                        difficulty
                    )

                st.session_state.feedback = None

                st.rerun()


# ---------------- INTERVIEW HISTORY ----------------

if st.session_state.history:

    st.subheader("📚 Interview History")

    for i, item in enumerate(st.session_state.history):

        with st.expander(
            f"Question {i + 1} — Score: {item['score']}/10"
        ):

            st.write("**Question:**")
            st.write(item["question"])

            st.write("**Your Answer:**")
            st.write(item["answer"])


# ---------------- FINAL INTERVIEW REPORT ----------------

if st.session_state.interview_completed:

    st.subheader("🏆 Final Interview Report")

    total_questions = len(st.session_state.scores)

    average_score = (
        sum(st.session_state.scores)
        / total_questions
    )

    st.write(
        f"**Questions Attempted:** {total_questions}"
    )

    st.write(
        f"**Average Score:** {average_score:.1f}/10"
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
        f"**Overall Performance:** {performance}"
    )


    if st.button("🤖 Generate AI Final Report"):

        with st.spinner(
            "AI is analyzing your interview performance..."
        ):

            st.session_state.final_report = (
                generate_final_report(
                    st.session_state.history
                )
            )


# ---------------- DISPLAY AI REPORT ----------------

if st.session_state.final_report:

    st.subheader("🤖 AI Performance Analysis")

    st.markdown(
        st.session_state.final_report
    )