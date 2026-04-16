from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI(
    model= 'gpt-4o-mini',
    base_url="https://openrouter.ai/api/v1"
)

class Fact(BaseModel):
    facts: list[str] = Field(description='5 Facts about the topic')
    
parser = PydanticOutputParser(pydantic_object=Fact)

template = PromptTemplate(
    template='Give 5 interesting fun fact about {topic} \n{format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser
prompt = {'topic': 'Football'}
result = chain.invoke(prompt)
print(result)