import unittest
from entity_recognition_service.entity_recognition import recognize


class EntityRecognitionTests(unittest.TestCase):
    def test_recognize_entities(self):
        text = "Apple Inc. is an American multinational technology company."
        expected_entities = [('Apple Inc.', 'ORG'), ('American', 'NORP')]  # Assuming spaCy recognizes "Apple Inc." as an organization
        self.assertEqual(recognize(text), expected_entities)

    def test_recognize_no_entities(self):
        text = "This is a simple sentence."
        self.assertEqual(recognize(text), [])

    def test_recognize_multiple_entities(self):
        text = "Google was founded in the United States."
        expected_entities = [('Google', 'ORG'), ('the United States', 'GPE')]
        self.assertEqual(recognize(text), expected_entities)


if __name__ == '__main__':
    unittest.main()