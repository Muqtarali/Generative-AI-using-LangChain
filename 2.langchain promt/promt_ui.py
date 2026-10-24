from pyexpat import model

from  langchain_core.prompts import PromptTemplate,load_template
from langchain_google_genai import ChatGoogleGenerativeAI 
import streamlit as st
from dotenv import load_dotenv
from typer import prompt

load_dotenv()


llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash"
)



st.title("LangChain Prompt UI")
st.header("Enter your prompt below:")



paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox("Select the explanation style:", ["Concise", "Detailed", "Step-by-step"])
length_input = st.selectbox("Select the explanation length:", ["Short", "Medium", "Long"])


# template = PromptTemplate(
#     template="""
# Please summarize the research paper titled "{paper_input}" with the following specifications:
# Explanation Style: {style_input}  
# Explanation Length: {length_input}  
# 1. Mathematical Details:  
#    - Include relevant mathematical equations if present in the paper.  
#    - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
# 2. Analogies:  
#    - Use relatable analogies to simplify complex ideas.  
# If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  
# Ensure the summary is clear, accurate, and aligned with the provided style and length.
# """,
# input_variables=['paper_input', 'style_input','length_input'],
# validate_template=True
# )


template = load_template('template.json')

prompt = template.invoke({
    "paper_input": paper_input,
    "style_input": style_input,
    "length_input": length_input,
})


if st.button("Generate Response"):
    if prompt:
       response = llm.invoke(prompt)
       st.subheader("Response:")
       st.write(response.text)