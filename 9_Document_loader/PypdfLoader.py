from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('9_Document_loader\dl-curriculum.pdf')

docs = loader.load()
# print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)
