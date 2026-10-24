from pathlib import Path

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader


loader=DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

document=loader.lazy_load()


print(document)

print(document[0].page_content)
print(document[0].matadata)

for doc in document:
    print(document.metadata)

