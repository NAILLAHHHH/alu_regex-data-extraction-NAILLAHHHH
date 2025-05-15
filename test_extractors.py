import unittest
from extractor import *

class TestRegexExtractors(unittest.TestCase):

    def test_extract_emails(self):
        text = """
        user@example.com
        firstname.lastname@company.co.uk
        invalid-email@com
        test@@example.com
        another.valid123-email@domain.io
        """
        expected = [
            'user@example.com',
            'firstname.lastname@company.co.uk',
            'another.valid123-email@domain.io'
        ]
        self.assertEqual(extract_emails(text), expected)

    def test_extract_urls(self):
        text = """
        https://www.example.comLinks to an external site.
        https://subdomain.example.org/pageLinks to an external site.
        www.example-site.com
        not-a-url.com
        http:/broken.url
        """
        expected = [
            'https://www.example.comLinks',
            'https://subdomain.example.org/pageLinks',
            'www.example-site.com'
        ]
        self.assertEqual(extract_urls(text), expected)

    def test_extract_phone_numbers(self):
        text = """
        (123) 456-7890
        123-456-7890
        123.456.7890
        1234567890
        123-45-6789
        123)456-7890
        """
        expected = [
            '(123) 456-7890',
            '123-456-7890',
            '123.456.7890'
        ]
        self.assertEqual(extract_phone_numbers(text), expected)

    def test_extract_credit_cards(self):
        text = """
        1234 5678 9012 3456
        1234-5678-9012-3456
        1234567890123456
        1234 5678 9012
        1234-5678-9012-345
        """
        expected = [
            '1234 5678 9012 3456',
            '1234-5678-9012-3456'
        ]
        self.assertEqual(extract_credit_cards(text), expected)

    def test_extract_times(self):
        text = """
        14:30
        2:30 PM
        02:30 pm
        25:00
        13:61
        7:00AM
        7:00
        7:60
        """
        expected = [
            '14:30',
            '2:30 PM',
            '02:30 pm',
            '7:00AM',
            '7:00'
        ]
        self.assertEqual(extract_times(text), expected)

if __name__ == '__main__':
    unittest.main()

