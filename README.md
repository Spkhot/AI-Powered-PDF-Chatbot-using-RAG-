# AI-Powered PDF Chatbot (RAG)

A simple Retrieval-Augmented Generation (RAG) application that allows users to ask questions from PDF documents using LangChain, ChromaDB, and Google's Gemini API.

## Features

* PDF document loading
* Text chunking
* Vector embeddings
* ChromaDB vector storage
* Semantic search
* AI-powered question answering

## Technologies Used

* Python
* LangChain
* ChromaDB
* Gemini API
* PyPDF
* Python Dotenv

## Installation

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key
```

Run the application:

```bash
python app.py
```

## How It Works

1. Load PDF document
2. Split text into chunks
3. Generate embeddings
4. Store vectors in ChromaDB
5. Retrieve relevant chunks
6. Generate answers using Gemini

## Author

Soham Khot
