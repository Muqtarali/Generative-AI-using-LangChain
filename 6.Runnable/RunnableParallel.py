from langchain_groq.chat_models import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableSequence

load_dotenv()

prompt1=PromptTemplate(
    template="Generate a tweet of the about {topic}",
    input_variables={'topic'}
)
prompt2=PromptTemplate(
    template="generte a linkiden post about {topic}",
    input_variables={'topic'}
)
model = ChatGroq(
    model='openai/gpt-oss-20b',
    temperature=0.2,
)

Pares=StrOutputParser()

chain=RunnableParallel({

    "tweet":RunnableSequence(prompt1,model,Pares),
    "linkidenPost":RunnableSequence(prompt2,model,Pares)
    }
)

result=chain.invoke({'topic':'AI'})
print(result)