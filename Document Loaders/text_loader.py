from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_groq.chat_models import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv()

model = ChatGroq(
    model='openai/gpt-oss-20b',
    temperature=0.2,
)




file_path = Path(__file__).with_name("cricket.txt")
loader = TextLoader(str(file_path), encoding="utf-8")
documents = loader.load()



Prompt=PromptTemplate(
    template="writ a summary of this poem \n {poem}",
    input_variables={'poem'}
)
# print(documents)
# print(type(documents))


# print(len(documents))

# print(documents[0])

# print(documents[0].page_content)
# print(documents[0].matadata)

parse=StrOutputParser()

chain=RunnableSequence(Prompt,model,parse)

result=chain.invoke({'poem':documents[0].page_content})

print(result)