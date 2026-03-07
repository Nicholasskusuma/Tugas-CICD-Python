import unittest
from validator import validate_email

class TestValidator(unittest.TestCase):
    def test_valid_email(self):
        self.assertTrue(validate_email("test@example.com"))

    def test_invalid_email(self):
        self.assertFalse(validate_email("email-salah.com"))

if __name__ == '__main__':
    unittest.main()