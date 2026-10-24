from langchain_groq.chat_models import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnableLambda,RunnablePassthrough

load_dotenv()

prompt=PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"],
)

model = ChatGroq(
    model='openai/gpt-oss-20b',
    temperature=0.2,
)


parsal=StrOutputParser()

chain=RunnableSequence(prompt,model,parsal)

def word_count(word):
    return len(word.split())

chain_to_used_of_lambda=RunnableParallel({
    "joke":RunnablePassthrough(),
    "word_count":RunnableLambda(word_count)

})


final_chain=RunnableSequence(chain,chain_to_used_of_lambda)

result=final_chain.invoke({'topic':'Ai'})

print(result)