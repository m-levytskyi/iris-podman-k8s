import unittest
from predict import app

class PredictTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<!DOCTYPE html>', response.data)

    def test_predict(self):
        response = self.app.post('/predict', data=dict(
            sepal_length=5.1,
            sepal_width=3.5,
            petal_length=1.4,
            petal_width=0.2
        ))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'setosa', response.data)

if __name__ == '__main__':
    unittest.main()