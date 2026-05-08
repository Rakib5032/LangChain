import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",
    task="text-generation",
    max_new_tokens=512,
    temperature=0
)

model = ChatHuggingFace(llm = llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template='Give name, age, and city of firctional character {name} \n {format_instruction} do not add extra things', 
    input_variables=['name'],
    partial_variables={'format_instruction': parser.get_format_instructions() }
)

# prompt = template.format()
# result = model.invoke(prompt)
# result = parser.parse(result.content)

# print(result)

chain = template | model | parser

result = chain.invoke({'name': 'Misir Ali'})
print(result)