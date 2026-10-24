
from langchain_google_genai import ChatGoogleGenerativeAI 
from langchain_core.messages import HumanMessage, AIMessage,SystemMessage
from dotenv import load_dotenv

load_dotenv()


model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash"
)

chat_history = [
    SystemMessage(content="You are a helpful assistant that provides accurate and concise information based on the user's input. If you don't know the answer, respond with 'I don't know.'")
]

while True:
    user_input = input("Enter your prompt (or type 'exit' to quit): ").strip()
    chat_history.append(HumanMessage(content=user_input))
    
    if user_input.lower() == "exit":
        break
    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.text))
    print(response.text)