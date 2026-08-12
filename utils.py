from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7
)


def generate_question(topic):

    prompt = f"""
You are a technical interviewer.

Generate one interview question about:
{topic}

The question should be suitable for a beginner/fresher.

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

Give the result in this format:

Score: X/10

Feedback:
Explain what was correct and what could be improved.

Correct Answer:
Give a simple and accurate answer.

"""

    response = llm.invoke(prompt)

    return response.content