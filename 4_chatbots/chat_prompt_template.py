from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', 'your are a {domain} exprt'),
    ('human', 'Explain the {topic} in simple terms')
])

prompt = chat_template.invoke({'domain': 'Football', 'topic': 'Red card'})

print(prompt)



