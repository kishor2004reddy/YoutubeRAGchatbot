import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from urllib.parse import urlparse, parse_qs
from config import EMBEDDING_MODEL, CHUNK_SIZE, CHUNK_OVERLAP


def get_video_id(video_url: str) -> str:
    query = urlparse(video_url).query
    return parse_qs(query).get("v", ["unknown"])[0]


def get_or_create_vectorstore(video_url, documents):
    video_id = get_video_id(video_url)
    persist_dir = f"./chroma_db/{video_id}"

    embedding = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    if os.path.exists(persist_dir):
        return Chroma(
            persist_directory=persist_dir,
            embedding_function=embedding
        )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    docs = splitter.split_documents(documents)

    vectorstore = Chroma.from_documents(
        documents=docs,
        embedding=embedding,
        persist_directory=persist_dir
    )
    vectorstore.persist()

    return vectorstore
