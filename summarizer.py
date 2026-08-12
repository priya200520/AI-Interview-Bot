from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_transcript(transcript):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=4000,
        chunk_overlap=200
    )

    chunks = text_splitter.split_text(transcript)

    return chunks