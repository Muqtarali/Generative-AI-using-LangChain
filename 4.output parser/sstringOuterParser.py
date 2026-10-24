from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


model = ChatGoogleGenerativeAI(model="gemini-3.8-flash", temperature=0.2)

template=PromptTemplate(
    template="write a detailed report on {topic}",
    input_variables=["topic"],
)

template2=PromptTemplate(
    template="write a summary on the following text: {text}",
    input_variables=["text"],
)

parser=StrOutputParser()

chain=template | model | parser | template2 | model | parser

result=chain.invoke({"topic":"Samsung Galaxy S24 Ultra in 5 line"})

print(result)