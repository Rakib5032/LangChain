from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embeddings = OpenAIEmbeddings(
    model='text-embedding-3-large',
    base_url='https://openrouter.ai/api/v1',
    dimensions=300
)

documents = [
    "Shakib Al Hasan is a Bangladeshi all-rounder.",
    "Tamim Iqbal is a Bangladeshi opening batsman.",
    "Mashrafe Mortaza is a former Bangladeshi captain.",
    "Mushfiqur Rahim is a Bangladeshi wicketkeeper-batsman.",
    "Mustafizur Rahman is a Bangladeshi fast bowler."
]

query = 'Who is Bangladeshi Capitan'

doc_embedding = embeddings.embed_documents(documents)
query_embedding = embeddings.embed_query(query)

# score = cosine_similarity([query_embedding], doc_embedding)
# print(score)
score = cosine_similarity([query_embedding], doc_embedding)[0]
print(score)

index, score = sorted(list(enumerate(score)),key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print(f'Document similarity score :{score}')