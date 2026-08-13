from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)


def generate_question(topic, difficulty):

    prompt = f"""
You are a technical interviewer.

Generate one {difficulty} level interview question about {topic}.

The question should be suitable for a fresher candidate.

Return only the question.
"""

    response = llm.invoke(prompt)

    return response.content


def evaluate_answer(question, answer):

    prompt = f"""
You are a technical interviewer.

Question:
{question}

Candidate's Answer:
{answer}

Evaluate the candidate's answer.

Give the result EXACTLY in this format:

Score: X/10

Feedback:
Explain what was correct and what could be improved.

Correct Answer:
Give a simple and accurate answer.
"""

    response = llm.invoke(prompt)

    return response.content


def generate_final_report(history):

    interview_data = ""

    for item in history:

        interview_data += f"""
Question: {item['question']}

Candidate Answer: {item['answer']}

Score: {item['score']}/10
"""

    prompt = f"""
You are an expert technical interviewer.

Analyze the following interview performance:

{interview_data}

Give a personalized final report in this format:

## Strengths
- Mention the candidate's strong areas based on their answers.

## Areas to Improve
- Mention specific topics or skills that need improvement.

## Recommendation
Give a short practical recommendation for improving technical interview performance.

Keep the feedback clear, encouraging, and suitable for a fresher.
"""

    response = llm.invoke(prompt)

    return response.content