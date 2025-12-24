# 🎥 YouTube RAG Chatbot  
### Explainable Video Question-Answering using Retrieval-Augmented Generation

YouTube RAG Chatbot is an end-to-end **Retrieval-Augmented Generation (RAG)** application that allows users to ask natural-language questions about any YouTube video and receive **grounded, explainable answers** based strictly on the video’s transcript.

The system retrieves the most relevant transcript segments from a persistent vector database and uses a large language model to generate accurate answers — while also showing **how each answer was derived**.

---

## 🚀 Live Demo
👉 Coming soon (after deployment)

---

## ✨ Features

- 🔗 **YouTube Transcript Ingestion**  
  Automatically loads transcripts from any public YouTube video.

- 🧠 **Retrieval-Augmented Generation (RAG)**  
  Combines semantic search with an LLM to produce context-aware answers.

- 📦 **Explainable Answers**  
  Displays the exact transcript chunks used to generate each response.

- 💾 **Persistent Vector Store**  
  Transcripts are embedded and stored **once per video**. Repeated queries reuse the existing database for fast responses.

- ⚡ **Cost-Efficient & Fast**  
  Uses open-source embeddings and Groq’s LLaMA-3.1 model for low-latency inference.

- 🖥️ **Interactive Web UI**  
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
