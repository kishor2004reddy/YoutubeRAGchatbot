import streamlit as st
from loaders import load_youtube_transcript
from vectorstore import get_or_create_vectorstore
from ragchain import build_rag_components

st.set_page_config(page_title="YouTube RAG Chatbot")

st.title("🎥 YouTube Video Chatbot")

video_url = st.text_input("Enter YouTube Video URL")

if video_url:
    with st.spinner("Processing video..."):
        transcript = load_youtube_transcript(video_url)
        vectorstore = get_or_create_vectorstore(video_url, transcript)
        retriever, prompt, llm, output_parser = build_rag_components(vectorstore)

    st.success("Video ready!")

    query = st.text_input("Ask a question about the video")

    if query:
        with st.spinner("Thinking..."):
            docs = retriever.invoke(query)

            context = "\n\n".join(doc.page_content for doc in docs)

            chain_input = {"context": context, "question": query}
            response = llm.invoke(prompt.format(**chain_input))
            answer = output_parser.invoke(response)

        st.subheader("Answer")
        st.write(answer)

        st.subheader("📌 How this answer was generated")
        with st.expander("View retrieved transcript segments"):
            for i, doc in enumerate(docs, 1):
                st.markdown(f"**Chunk {i}:**")
                st.write(doc.page_content)
                st.divider()
