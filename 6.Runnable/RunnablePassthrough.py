from langchain_groq.chat_models import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough

load_dotenv()

prompt=PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"],
)
paasthrow=RunnablePassthrough()
prompt2=PromptTemplate(
    template="Expla this {joke}",
    input_variables={"joke"}
)
model = ChatGroq(
    model='openai/gpt-oss-20b',
    temperature=0.2,
)


parsal=StrOutputParser()


joke=RunnableSequence(parsal,model,parsal),

chain=RunnableParallel({
    "joke":RunnablePassthrough(joke),
    "expnation":RunnableSequence(prompt2,model,parsal),
})

finalchain=RunnableSequence(joke,chain)





result=finalchain.invoke({'topic':'AI'})

print(result)