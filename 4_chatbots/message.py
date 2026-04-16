from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1"
)

messages = [
    SystemMessage(content='You are a ai assistant'),
    HumanMessage(content='Tell me about Dhaka city in 5 line')
]

respond = model.invoke(messages)
messages.append(AIMessage(respond.content))

print(messages)
