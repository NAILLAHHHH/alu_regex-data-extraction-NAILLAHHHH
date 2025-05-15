from extractor import *

def demo_test_samples():
    print("=== Email Extraction ===")
    email_text = "user@example.com firstname.lastname@company.co.uk wrong@.com user@site"
    valid, invalid = extract_emails(email_text)
    print("Valid emails:", valid)
    print("Invalid emails:", invalid)
    print()

    print("=== URL Extraction ===")
    url_text = "https://www.example.com http://bad_url www.example.com/page wrong_link"
    valid, invalid = extract_urls(url_text)
    print("Valid URLs:", valid)
    print("Invalid URLs:", invalid)
    print()

    print("=== Phone Number Extraction ===")
    phone_text = "(123) 456-7890 123-456-7890 123.456.7890 1234567890 (1234567890"
    valid, invalid = extract_phone_numbers(phone_text)
    print("Valid phone numbers:", valid)
    print("Invalid phone numbers:", invalid)
    print()

    print("=== Credit Card Extraction ===")
    cc_text = "1234 5678 9012 3456 1234-5678-9012-3456 1234567890123456"
    valid, invalid = extract_credit_cards(cc_text)
    print("Valid credit cards:", valid)
    print("Invalid credit cards:", invalid)
    print()

    print("=== Time Extraction ===")
    time_text = "14:30 2:30 PM 02:30 pm 7:00AM 7:00 25:00"
    valid, invalid = extract_times(time_text)
    print("Valid times:", valid)
    print("Invalid times:", invalid)
    print()

if __name__ == "__main__":
    demo_test_samples()
