from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

# GPT
model = ChatOpenAI(
    model='gpt-4o-mini',
    base_url="https://openrouter.ai/api/v1"
)

class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description='Give ths output')
    
pydentic_parser = PydanticOutputParser(pydantic_object=Feedback)
str_parser = StrOutputParser()

feedback = """This is a very very phone"""


prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback into posite or negative \n{feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction': pydentic_parser.get_format_instructions()}
)

classifier_chain = prompt1 | model | pydentic_parser

prompt2 = PromptTemplate(
    template='Write a apporopriate response to this positive feedback {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write a apporopriate response to this negative feedback {feedback}',
    input_variables=['feedback']
)

#now the branch chain
branch_chain = RunnableBranch(
    #(condition, chain)
    (lambda x:x.sentiment == 'positive', prompt2 | model | str_parser),
    (lambda x:x.sentiment == 'negative', prompt3 | model | str_parser),
    # Default Chain
    RunnableLambda(lambda x: 'Could not find')
)

chain = classifier_chain | branch_chain

result = chain.invoke({'feedback': feedback})
print(result)
