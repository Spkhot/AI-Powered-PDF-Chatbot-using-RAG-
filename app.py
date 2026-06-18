# app.py
from dotenv import load_dotenv
import os

load_dotenv()

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import Chroma

# API KEY
google_api = os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"] =google_api

# LOAD PDF
loader = PyPDFLoader("employee.pdf")
documents = loader.load()

# CHUNKING
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

# EMBEDDINGS
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

# VECTOR DATABASE
db = Chroma.from_documents(
    chunks,
    embeddings
)

# LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

print("PDF Chatbot Ready!")

while True:

    question = input("\nAsk Question: ")

    if question.lower() == "exit":
        break

    docs = db.similarity_search(
        question,
        k=3
    )

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
    Answer using only the context below.

    Context:
    {context}

    Question:
    {question}
    """

    response = llm.invoke(prompt)

    print("\nAnswer:")
    print(response.content)