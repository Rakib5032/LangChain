from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model= 'gpt-4o-mini',
    base_url="https://openrouter.ai/api/v1"
)

loader = TextLoader('9_Document_loader/cricket.txt', encoding='utf-8')

docs = loader.load()

prompt = PromptTemplate(
    template='Write a summary for the following poem \n{poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

chain = prompt | model | parser

response = chain.invoke({'poem': docs[0].page_content})

print(response)


# print(docs)

# print(type(docs))

# print(docs[0])

