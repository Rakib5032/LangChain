import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",
    task="text-generation",
)

model = ChatHuggingFace(llm = llm)

class Person(BaseModel):
    name: str = Field(description="Name of the person")
    age: int = Field(gt=18, description='Age of the person')
    city: str = Field(description="City of the person")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='Generate a name, age, and city of a person from {place} except Dhaka \n{format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

# chain = template.invoke({'place':'Bangladesh'})
# result = model.invoke(chain)
# result = parser.parse(result.content)
# print(result)

chain = template | model | parser

result = chain.invoke({'place': 'Bangladesh'})
print(result)
