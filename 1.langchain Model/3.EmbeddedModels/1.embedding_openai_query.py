from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small",dimensions=32)

embedding = embeddings.embed_query("delhi is the capital of indai")

print(embedding)