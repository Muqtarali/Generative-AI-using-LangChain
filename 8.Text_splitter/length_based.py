from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyMuPDFLoader
from pathlib import Path


file_path=Path(__file__).with_name('dl-curriculum.pdf')

loader=PyMuPDFLoader(str(file_path))

doc=loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
)

chunks = splitter.split_documents(doc)

print(len(chunks))

for chunk in chunks:
    print(chunk)
    print("---")