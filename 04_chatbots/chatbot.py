from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model= 'gpt-4o-mini',
    base_url="https://openrouter.ai/api/v1"
)

message = [
    SystemMessage(content='You are a helpful AI Assistant')
]
while True:
    user_input = input('User :')
    message.append(HumanMessage(user_input))
    if user_input == 'exit':
        break;
    
    response = model.invoke(message)
    message.append(AIMessage(response.content))
    print('AI : ', response.content)
print(message)