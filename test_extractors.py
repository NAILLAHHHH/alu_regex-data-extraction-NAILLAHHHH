# test_extractors.py
import unittest
from extractor import *

class TestRegexExtractors(unittest.TestCase):

    def test_extract_emails(self):
        text = "user@example.com firstname.lastname@company.co.uk wrong@.com user@site"
        valid, invalid = extract_emails(text)
        self.assertEqual(valid, ['user@example.com', 'firstname.lastname@company.co.uk'])
        self.assertIn("Invalid email: wrong@.com", invalid)
        self.assertIn("Invalid email: user@site", invalid)

    def test_extract_urls(self):
        text = "https://www.example.com http://bad_url www.example.com/page wrong_link"
        valid, invalid = extract_urls(text)
        self.assertIn("https://www.example.com", valid)
        self.assertIn("www.example.com/page", valid)
        self.assertTrue(any("Invalid URL: http://bad_url" in msg for msg in invalid))

    def test_extract_phone_numbers(self):
        text = "(123) 456-7890 123-456-7890 123.456.7890 1234567890 (1234567890"
        valid, invalid = extract_phone_numbers(text)
        self.assertEqual(valid, ['(123) 456-7890', '123-456-7890', '123.456.7890'])
        self.assertIn("Invalid phone number: 1234567890", invalid)

    def test_extract_credit_cards(self):
        text = "1234 5678 9012 3456 1234-5678-9012-3456 1234567890123456"
        valid, invalid = extract_credit_cards(text)
        self.assertEqual(valid, ['1234 5678 9012 3456', '1234-5678-9012-3456'])
        self.assertIn("Invalid credit card number: 1234567890123456", invalid)

    def test_extract_times(self):
        text = "14:30 2:30 PM 02:30 pm 7:00AM 7:00 25:00"
        valid, invalid = extract_times(text)
        self.assertEqual(valid, ['14:30', '2:30 PM', '02:30 pm', '7:00AM', '7:00'])
        self.assertIn("Invalid time format: 25:00", invalid)from extractors import *

text = "user@example.com firstname.lastname@company.co.uk wrong@.com user@site"
valid, invalid = extract_emails(text)
print("Valid emails:", valid)
print("Invalid emails:", invalid)

text = "https://www.example.com http://bad_url www.example.com/page wrong_link"
valid, invalid = extract_urls(text)
print("Valid URLs:", valid)
print("Invalid URLs:", invalid)

# Similarly for phone numbers, credit cards, times...



if __name__ == '__main__':
    unittest.main()
