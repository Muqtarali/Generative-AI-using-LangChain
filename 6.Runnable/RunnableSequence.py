from langchain_groq.chat_models import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv()

prompt=PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"],
)
prompt2=PromptTemplate(
    template="Expla this {joke}",
    input_variables={"joke"}
)
model = ChatGroq(
    model='openai/gpt-oss-20b',
    temperature=0.2,
)


parsal=StrOutputParser()

chain=RunnableSequence(prompt,model,parsal,prompt2,model,parsal)

result=chain.invoke({'topic':'human'})

print(result)