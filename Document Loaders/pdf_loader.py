from pathlib import Path

from langchain_community.document_loaders import PyMuPDFLoader


file_path = Path(__file__).with_name("dl-curriculum.pdf")
loader = PyMuPDFLoader(str(file_path))


documents = loader.load()

print(f"Loaded {len(documents)} document(s) from {file_path.name}.")

print(documents[0].page_content)

print(documents[0].metadata)

