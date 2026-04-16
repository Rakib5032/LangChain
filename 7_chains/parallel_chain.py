from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

# Models (different providers via OpenRouter)

# GPT
model1 = ChatOpenAI(
    model='gpt-4o-mini',
    base_url="https://openrouter.ai/api/v1"
)

# Claude (Anthropic via OpenRouter)
model2 = ChatOpenAI(
    model='anthropic/claude-3-haiku',
    base_url="https://openrouter.ai/api/v1"
)

# Mistral
model3 = ChatOpenAI(
    model='mistralai/mistral-small-24b-instruct-2501',
    base_url="https://openrouter.ai/api/v1"
)

prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text \n{text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template='Generate 5 short question answer from the following text \n {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz in a single document\n notes -> {note} and quiz {quiz}',
    input_variables=['note', 'quiz']
)

parser = StrOutputParser()

#create chain
parallel_chain = RunnableParallel({
    'note': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chain = prompt3 | model3 | parser

chain = parallel_chain | merge_chain

text = """
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

The advantages of support vector machines are:

Effective in high dimensional spaces.

Still effective in cases where number of dimensions is greater than the number of samples.

Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.

Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.

The disadvantages of support vector machines include:

If the number of features is much greater than the number of samples, avoid over-fitting in choosing Kernel functions and regularization term is crucial.

SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation (see Scores and probabilities, below).

The support vector machines in scikit-learn support both dense (numpy.ndarray and convertible to that by numpy.asarray) and sparse (any scipy.sparse) sample vectors as input. However, to use an SVM to make predictions for sparse data, it must have been fit on such data. For optimal performance, use C-ordered numpy.ndarray (dense) or scipy.sparse.csr_matrix (sparse) with dtype=float64.
"""

# result = chain.invoke({'text': text})
# print(result)

chain.get_graph().print_ascii()

