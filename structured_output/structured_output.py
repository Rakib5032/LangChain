from typing import TypedDict, Annotated
from model import model

review = """
I bought this wireless headphone last month and overall I’m quite satisfied. The sound quality is really clear, especially the bass which feels deep and immersive. Battery life is impressive — I can use it for almost two days without charging. The design is also comfortable for long use.

However, there are a few downsides. The ear cushions get a bit warm after extended use, and the Bluetooth connection sometimes drops when I move too far from my phone. Also, the build quality feels slightly cheap considering the price.

Still, for the features it offers, I think it’s a decent purchase and worth considering.
"""

class Review(TypedDict):
    summary: Annotated[str, "One line very short summary of the review"]
    sentimate: Annotated[str, "Sentimante of the review in one word"]
    
structured_model = model.with_structured_output(Review)

respond = structured_model.invoke(review)

print(respond['summary'])
print(respond['sentimate'])