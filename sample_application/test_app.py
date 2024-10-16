# test_app.py
import unittest
from app import hello

class TestHelloFunction(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), "Hello, CI/CD!")

if __name__ == '__main__':
    unittest.main()

