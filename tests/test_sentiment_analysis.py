import unittest
from sentiment_analysis_service.sentiment_analysis import analyze


class SentimentAnalysisTests(unittest.TestCase):

    def test_positive_sentiment(self):
        self.assertEqual(analyze("I love sunny days!"), "Positive")

    def test_negative_sentiment(self):
        self.assertEqual(analyze("I hate rainy days."), "Negative")

    def test_neutral_sentiment(self):
        self.assertEqual(analyze("It's an ordinary day."), "Neutral")

        
if __name__ == '__main__':
    unittest.main()
