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

# chain
chain = template | model | parser

prompt = {'topic': 'Football'}
result = chain.invoke(prompt)
print(result)

chain.get_graph().print_ascii()