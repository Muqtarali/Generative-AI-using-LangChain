
from langchain_openai import OpenAI, openai

from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

model=OpenAI(model="gpt-3.5-turbo-instruct", temperature=0.9)

result=model.invoke("What is the capital of india?")
print(result)   
