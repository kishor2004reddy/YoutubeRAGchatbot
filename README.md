# 🎥 YouTube RAG Chatbot  
### Explainable Video Question-Answering using Retrieval-Augmented Generation

YouTube RAG Chatbot is an end-to-end Retrieval-Augmented Generation (RAG) application that allows users to ask natural-language questions about any YouTube video and receive grounded, explainable answers based strictly on the video’s transcript.

The system retrieves the most relevant transcript segments from a persistent vector database and uses a large language model to generate accurate answers — while also showing how each answer was derived.

---

## 🚀 Live Demo
Coming soon (after deployment)

---

## ✨ Features

- YouTube Transcript Ingestion  
  Automatically loads transcripts from any public YouTube video.

- Retrieval-Augmented Generation (RAG)  
  Combines semantic search with an LLM to produce context-aware answers.

- Explainable Answers  
  Displays the exact transcript chunks used to generate each response.

- Persistent Vector Store  
  Transcripts are embedded and stored once per video. Repeated queries reuse the existing database for fast responses.

- Cost-Efficient & Fast  
  Uses open-source embeddings and Groq’s LLaMA-3.1 model for low-latency inference.

- Interactive Web UI  
  Built with Streamlit for simplicity and usability.

---

## 🧱 Architecture Overview

User Query  
↓  
Vector Retriever (ChromaDB)  
↓  
Relevant Transcript Chunks  
↓  
LLM (Groq – LLaMA 3.1)  
↓  
Final Answer + Source Context  

---

## 🛠️ Tech Stack

Frontend: Streamlit  
LLM: Groq (LLaMA-3.1-8B-Instant)  
Embeddings: HuggingFace (all-MiniLM-L6-v2)  
Vector DB: ChromaDB  
Framework: LangChain  
Data Source: YouTube Transcripts  

---

## 📂 Project Structure

youtube_rag_app/  
├── app.py                  # Streamlit application  
├── config.py               # Environment variables & constants  
├── loaders.py              # YouTube transcript loader  
├── vectorstore.py          # Persistent ChromaDB logic  
├── rag_chain.py            # Retrieval + generation pipeline  
├── chroma_db/              # Vector databases (one per video)  
├── requirements.txt  
└── README.md  

---

## ⚙️ Installation

Clone the repository  
git clone https://github.com/your-username/YouTubeRAGchatbot.git  
cd YouTubeRAGchatbot  

Create virtual environment  
conda create -n yt_rag python=3.10  
conda activate yt_rag  

Install dependencies  
pip install -r requirements.txt  

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

GROQ_API_KEY=your_groq_api_key  
HUGGINGFACE_TOKEN=your_huggingface_token  
LANGCHAIN_API_KEY=your_langchain_api_key  

---

## ▶️ Running the App Locally

streamlit run app.py  

Open in browser:  
http://localhost:8501  

---

## 📌 Example Usage

1. Paste a YouTube video URL  
2. Ask a question about the video  
3. Receive a precise answer and the transcript chunks used to generate it  

---

## 🔮 Future Enhancements

- Timestamp-based transcript navigation  
- Multi-video querying  
- Chat memory & conversation history

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Kishor Reddy  
AI / ML Enthusiast | RAG & LLM Systems  

If you find this project useful, feel free to star the repository.
