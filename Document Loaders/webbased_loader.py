from langchain_community.document_loaders import WebBaseLoader
from langchain_groq.chat_models import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model='openai/gpt-oss-20b',
    temperature=0.2,
)


prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question','text']
)

parser = StrOutputParser()

url = 'https://www.flipkart.com/boat-20000-mah-22-5-w-slim-power-bank/p/itm57b327e742304?pid=PWBGR4KGHXQCZVSQ&lid=LSTPWBGR4KGHXQCZVSQAD7BPU&marketplace=FLIPKART&store=tyy%2F4mr%2Ffu6&srno=b_1_1&otracker=browse&fm=organic&iid=en_Snx0x_nQVlxNuV-1uDkdVsWCuNLGIEoS5SUpyYdbzlA5j0kfUqPUfyOmWnnIOuJNaNZ_Ed3p0FNJoijbpr8_-4GCr6toC2RDwvViWGdfzha4z7Ndet8RYFpTVaisqDV7&ppt=None&ppn=None&ssid=lbinjs1y3k0000001792781879859&ov_redirect=true&ov_redirect=true'
loader = WebBaseLoader(url)

docs = loader.load()


chain = prompt | model | parser

print(chain.invoke({'question':'What is the prodcut that we are talking about?', 'text':docs[0].page_content}))