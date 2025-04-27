import unittest
from app import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        # Test client simulates the app
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        # Test if '/' returns 200 OK
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Hello, World from Eng. Mathias Flask App!")

if __name__ == "__main__":
    unittest.main()

