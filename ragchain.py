from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from config import LLM_MODEL


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def build_rag_components(vectorstore):
    retriever = vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 5, "lambda_mult": 0.7}
    )

    prompt = ChatPromptTemplate.from_template("""
    You are a helpful assistant.
    Answer the question using ONLY the context below.
    If the answer is not in the context, say "I don't know."

    Context:
    {context}

    Question:
    {question}
    """)

    llm = ChatGroq(
        model=LLM_MODEL,
        temperature=0
    )

    return retriever, prompt, llm, StrOutputParser()
