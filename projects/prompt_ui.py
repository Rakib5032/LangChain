from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt
import streamlit as st

load_dotenv()

model = ChatOpenAI(
    model= 'gpt-4o-mini',
    base_url="https://openrouter.ai/api/v1"
)

st.header('Basic Research Tool')
# user_input = st.text_input('Enter your prompt')

# if st.button('Sumarize'):
#     respond = model.invoke(user_input)
#     st.write(respond.content)

paper_input = st.selectbox('Select Research paper name', ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox('Select Explanation Style',["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] )

length_input = st.selectbox('Enter Explanation Length', ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"])


# user_input = f"Sumarise the paper {paper_input} and find the {style_input} and keep the output in {length_input}"

template = load_prompt('template.json')

prompt = template.format(
    paper_input=paper_input,
    style_input=style_input,
    length_input=length_input
)


if st.button('Click'):
    respond = model.invoke(prompt)
    st.write(respond.content)
    st.write(prompt)


