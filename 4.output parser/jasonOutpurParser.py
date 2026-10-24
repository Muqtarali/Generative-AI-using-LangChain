from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,jasonOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.8-flash", temperature=0.2)


parser=jasonOutputParser()


template = PromptTemplate(
    template='Give me 5 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)


# promt=template.format({'topic':'black hole'})

# result=model.invok(promt)

# final_result=parser.parse(result)

# print(final_result['name'])

#another way

chain = template | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)
