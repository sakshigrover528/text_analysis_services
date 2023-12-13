import spacy

# Load spaCy model for entity recognition
nlp = spacy.load("en_core_web_sm")


def recognize(text):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]
