""" Demonstration of Named Entity Recognition (NER) in spaCy. """
import spacy
nlp = spacy.load("en_core_web_sm")

gardenpathSentences = [
    "John saw the man with the telescope in Paris yesterday.",
    "Tesla reported the results that analysts at "
    "Bloomberg predicted accurately",
    "The company offered a discount of 50% on products sold on Black Friday.",
    "At 2:00 PM the train departed the passengers waved goodbye.",
    "The linguist studying Spanish taught by "
    "native speakers found it challenging.",
    "Mary gave the child a Band-Aid",
    "That Jill is never here hurts",
    "The cotton clothing is made of grows in Mississippi"
]

list_of_entities = []

# Tokenise and perform NER on each sentence
for s in gardenpathSentences:
    doc = nlp(s)
    tokenised = [token.text for token in doc]
    entities = [
        (ent.text, ent.start_char, ent.end_char, ent.label_)
        for ent in doc.ents
        ]
    list_of_entities.append({"tokens": tokenised, "entities": entities})

for item in list_of_entities:
    print(f"Tokens: {item['tokens']}")
    print(f"Entities: {item['entities']}")
    print('\u2500'*100)

# Explain the NER categorisation
print('\u2500'*100)
print(f"NORP: {spacy.explain('NORP')}")
print(f"EVENT: {spacy.explain('EVENT')}")
print(f"GPE: {spacy.explain('GPE')}")
print(f"ORG: {spacy.explain('ORG')}")
print('\u2500'*100)
