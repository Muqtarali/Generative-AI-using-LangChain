from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

docs = [
    "Delhi is the capital of India",
    "Mumbai is the financial capital of India",
    "Cricket is very popular in India"
]

vectors = embeddings.embed_documents(docs)


print(str(vectors))