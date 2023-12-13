import spacy
from nltk.sentiment import SentimentIntensityAnalyzer

# Load spaCy model for entity recognition
nlp = spacy.load("en_core_web_sm")


def analyze(text):
    sia = SentimentIntensityAnalyzer()
    sentiment_score = sia.polarity_scores(text)
    if sentiment_score['compound'] >= 0.05:
        return 'Positive'
    elif sentiment_score['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'
