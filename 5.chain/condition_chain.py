from langchain_groq.chat_models import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda, RunnablePassthrough
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal

load_dotenv()

model = ChatGroq(
    model='openai/gpt-oss-20b',
    temperature=0.2,
)

parser=StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(
        description='Sentiment of the feedback'
    )

parser2=PydanticOutputParser(pydantic_object=Feedback)


prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback as positive or negative.\n{feedback}\n{format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2


prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)



branch_chain = RunnableBranch(
    (lambda x: x['sentiment'].sentiment == 'positive', prompt2 | model | parser),
    (lambda x: x['sentiment'].sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: 'Could not find sentiment'),
)

chain = RunnablePassthrough.assign(sentiment=classifier_chain) | branch_chain

print(chain.invoke({'feedback': 'This is a beautiful mobile'}))

chain.get_graph().print_ascii()