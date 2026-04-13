from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

# Step 1: create endpointcl
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
)

# Step 2: wrap with chat model
chat_model = ChatHuggingFace(llm=llm)

# Step 3: invoke
result = chat_model.invoke("Create a Html form")
print(result.content)