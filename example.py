import spacy
from spacy.lang.en import English

nlp = English()

# find percentages in text
doc = nlp(
    "In 1990, more than 60% of people in East Asia were in extreme poverty. "
    "Now less than 4% are.")

for token in doc:
    if token.like_num:
        next_token = doc[token.i + 1]
        if next_token.text == "%":
            print("Percentage found:", token.text)

# lang model
en_nlp = spacy.load('en_core_web_sm')

pizza = en_nlp('She ate the pizza')

for token in pizza:
    print(token.text, token.pos_, token.dep_, token.head.text)
