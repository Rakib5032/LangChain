from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

model = OpenAIEmbeddings(
    model= 'text-embedding-3-large',
    base_url="https://openrouter.ai/api/v1"
)

response = model.embed_query('tell about tcl global')
print(str(response))