import unittest
from word_count_service.word_count import count


class WordCountTests(unittest.TestCase):

        def test_count_words(self):
            text = "Hello world!"
            self.assertEqual(count(text), 2)  # Assuming 'Hello' and 'world!' are two words

        def test_count_empty_string(self):
            text = ""
            self.assertEqual(count(text), 0)

        def test_count_with_punctuation(self):
            text = "Well, this is a test."
            self.assertEqual(count(text), 5)  # Assuming punctuation is handled in 'preprocess_text'


if __name__ == '__main__':
    unittest.main()
