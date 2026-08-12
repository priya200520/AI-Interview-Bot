from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_transcript(transcript):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=4000,
        chunk_overlap=200
    )

    chunks = text_splitter.split_text(transcript)

    return chunks
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)


def summarize_chunks(chunks):

    summaries = []

    for i, chunk in enumerate(chunks):

        prompt = f"""
Summarize this part of a YouTube video.

Use simple and clear language.
Include only the important information.

Video Part {i + 1}:

{chunk}
"""

        response = llm.invoke(prompt)

        summaries.append(response.content)

    return summaries