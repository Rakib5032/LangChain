from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
message = [SystemMessage(content='You are a ai assistant', additional_kwargs={}, response_metadata={}), HumanMessage(content='Tell me about Dhaka city in 5 line', additional_kwargs={}, response_metadata={}), AIMessage(content='Dhaka is the capital city of Bangladesh and is one of the most populous cities in the world. It is a vibrant and bustling metropolis with a rich history and culture. Dhaka is known for its eclectic mix of modern and traditional architecture, as well as its bustling markets and vibrant street life. The city is also home to numerous historical landmarks, including the Lalbagh Fort and the Ahsan Manzil palace. Dhaka is a melting pot of different cultures and religions, making it a diverse and dynamic city to explore.', additional_kwargs={}, response_metadata={}, tool_calls=[], invalid_tool_calls=[])]

print(len(message))

for index, value in enumerate(message):
    print(f'Index is {index} and response is {value}')
    print("-" * 50)
    
