from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model="claude-3.0-sonnet-20241022", temperature=0.9,max_completion_tokens=100)

result=model.invoke("What is the capital of india?")
print(result.content)

