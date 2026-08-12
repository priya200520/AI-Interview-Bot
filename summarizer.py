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
def create_final_summary(summaries):

    combined_summaries = "\n\n".join(summaries)

    prompt = f"""
You are an expert YouTube video summarizer.

Below are summaries of different parts of one YouTube video.

Combine them into one complete and easy-to-understand final summary.

Use this format:

## Summary
Give a clear overall summary.

## Key Points
- Point 1
- Point 2
- Point 3
- Point 4
- Point 5

## Important Takeaways
- Takeaway 1
- Takeaway 2
- Takeaway 3

Part Summaries:

{combined_summaries}
"""

    response = llm.invoke(prompt)

    return response.content