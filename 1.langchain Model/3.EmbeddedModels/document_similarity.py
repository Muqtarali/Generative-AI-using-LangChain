from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = "tell me about Virat Kohli"
  
doc_embeddings = embeddings.embed_documents(documents)
query_embedding = embeddings.embed_query(query)

# Convert to numpy arrays
doc_embeddings = np.array(doc_embeddings)
query_embedding = np.array(query_embedding)

similarity_scores = cosine_similarity(
    query_embedding.reshape(1, -1),
    doc_embeddings
)

# Get the index of the most similar document
most_similar_index = np.argmax(similarity_scores)

print(query)
print(documents[most_similar_index])
print("similarity score is:", np.sort(similarity_scores)[::-1][0])