from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

template = PromptTemplate(
    template='Give 5 interesting fun fact about {topic} ',
    input_variables=['topic'],
)

model = ChatOpenAI(
    model= 'gpt-4o-mini',
    base_url="https://openrouter.ai/api/v1"
)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='write a short summary on{text}',
    input_variables='text'
)

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic': 'Football'})
print(result)
