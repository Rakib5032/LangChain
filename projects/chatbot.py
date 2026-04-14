from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(
    model= 'gpt-4o-mini',
    base_url="https://openrouter.ai/api/v1"
)

chat =[]
while True:
    user_input = input('User :')
    chat.append(user_input)
    if user_input == 'exit':
        break;
    
    response = model.invoke(chat)
    chat.append(response.content)
    print(response.content)
print(chat)