import unittest
import json
from app import app


class TextAnalysisServicesTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add_service(self):
        # Test adding a new service
        response = self.app.post('/services/add',
                                 data=json.dumps({'name': 'sentiment_analysis', 'url': '"http://localhost:8001/analyze"'}),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(f'Service sentiment_analysis added', response.data.decode())

    def test_remove_service(self):
        # Test removing a service
        self.app.post('/services/add',
                      data=json.dumps({'name': 'test_service', 'function': 'test_function'}),
                      content_type='application/json')
        response = self.app.delete('/services/test_service')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Service test_service removed', response.data.decode())

    def test_list_services(self):
        # Test listing all services
        response = self.app.get('/services')
        self.assertEqual(response.status_code, 200)

    def test_analyze_text(self):
        # Test the analyze endpoint
        self.app.post('/services/add',
                      data=json.dumps({'name': 'sentiment_analysis', 'url': '"http://localhost:8001/analyze"'}),
                      content_type='application/json')
        response = self.app.post('/analyze',
                                 data=json.dumps({'service': 'sentiment_analysis', 'text': 'Hello world'}),
                                 content_type='application/json')
        # Assuming 'test_service' is a valid service that returns a result
        self.assertEqual(response.status_code, 200)
        # Validate response format or content here


if __name__ == '__main__':
    unittest.main()
