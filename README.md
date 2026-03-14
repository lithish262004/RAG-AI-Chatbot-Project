# AI Research Assistant Chatbot (NeoStats AI Engineer Challenge)

## Overview

This project is an **AI-powered chatbot built using Streamlit** that can answer user questions intelligently by combining **Large Language Models, Retrieval-Augmented Generation (RAG), and live web search**.

The chatbot can:

* Answer general questions using an LLM
* Retrieve information from uploaded documents (PDFs)
* Perform live web searches when document knowledge is insufficient
* Provide responses in **Concise or Detailed modes**

This project was developed as part of the **NeoStats AI Engineer Case Study: "The Chatbot Blueprint: Imagine, Build, Solve."**

---

## Features

### 1. Retrieval-Augmented Generation (RAG)

* Users can upload PDF documents.
* The system extracts text and splits it into chunks.
* TF-IDF vector embeddings are used to retrieve the most relevant document content.
* The chatbot answers questions using the retrieved document context.

### 2. Live Web Search

* If relevant document information is unavailable, the chatbot performs a **real-time web search**.
* Web search results are used as context for generating responses.

### 3. Response Modes

Users can switch between two response styles:

* **Concise Mode** – Short summarized answers
* **Detailed Mode** – In-depth explanations

### 4. Interactive UI

The application is built using **Streamlit**, providing:

* Simple chatbot interface
* File upload support
* Mode switching
* Real-time responses

---

## Project Architecture

User Query
↓
Streamlit Interface (`app.py`)
↓
RAG Retrieval (Vector Search from Documents)
↓
Web Search Fallback (DuckDuckGo API)
↓
LLM Response Generation (Groq Llama Model)
↓
Final Answer Display

---

## Project Structure

```
project/
├── config/
│   └── config.py
│
├── models/
│   ├── llm.py
│   └── embeddings.py
│
├── utils/
│   ├── pdf_loader.py
│   ├── vector_store.py
│   └── web_search.py
│
├── app.py
└── requirements.txt
```

---

## Technologies Used

* **Python**
* **Streamlit**
* **Groq LLM API**
* **DuckDuckGo Search**
* **PyPDF**
* **Scikit-learn (TF-IDF vectorization)**

---

## Installation

Clone the repository:

```
git clone https://github.com/yourusername/neo-stats-ai-chatbot.git
cd neo-stats-ai-chatbot
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Environment Setup

Create a `.env` file or configure environment variables for the API key:

```
GROQ_API_KEY=your_groq_api_key
```

---

## Running the Application

Start the Streamlit app:

```
streamlit run app.py
```

The application will run at:

```
http://localhost:8501
```

---

## Deployment

This application is deployed on **Streamlit Cloud**.

Deployment steps:

1. Push the repository to GitHub
2. Connect the repository to Streamlit Cloud
3. Add API keys in Streamlit secrets
4. Deploy the `app.py` file

