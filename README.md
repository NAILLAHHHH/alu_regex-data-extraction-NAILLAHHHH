# alu_regex-data-extraction-NAILLAHHH

Hey there! This is a simple Python tool that helps you pull out useful bits of info from any text — things like emails, URLs, phone numbers, credit card numbers, and times. It not only finds them but also tells you which ones look valid and which ones might be a bit off.

---

## What Can It Do?

* **Emails:** Finds all the email addresses and flags the weird ones.
* **URLs:** Snags website links starting with `http://`, `https://`, or just `www`.
* **Phone Numbers:** Picks up phone numbers in common formats like `(123) 456-7890`.
* **Credit Cards:** Finds credit card numbers written with spaces or dashes.
* **Times:** Spots times in both 24-hour style (`14:30`) and 12-hour AM/PM style (`2:30 PM`).

---

## How to Use It

There’s a demo you can run that shows how each extraction works with some example text. Just run this:

```bash
python3 test_extractors.py
```

It’ll print out all the valid and invalid matches it finds for each category.

---

## What’s Inside?

* `extractor.py`: The heart of the project, where all the magic happens using regular expressions to find and validate data.
* `test_extractors.py`: A simple script that runs tests and shows you how extraction works on sample texts.

---

## Quick Peek at the Functions

* `extract_emails(text)`: Finds emails, separates good ones from the bad.
* `extract_urls(text)`: Finds URLs and checks if they look legit.
* `extract_phone_numbers(text)`: Grabs phone numbers in common formats.
* `extract_credit_cards(text)`: Finds credit card numbers with spaces or dashes.
* `extract_times(text)`: Picks up valid time formats and tells you if something looks wrong.

---

## Example Output

Here’s what you might see when you run the demo:

```
=== Email Extraction ===
Valid emails: ['user@example.com', 'firstname.lastname@company.co.uk']
Invalid emails: ['Invalid email: wrong@.com', 'Invalid email: user@site']

=== URL Extraction ===
Valid URLs: ['https://www.example.com', 'http://bad_url', 'www.example.com/page']
Invalid URLs: ['Invalid URL: wrong_link']

=== Phone Number Extraction ===
Valid phone numbers: ['(123) 456-7890', '123-456-7890', '123.456.7890', '1234567890']
Invalid phone numbers: ['Invalid phone number: (1234567890']

=== Credit Card Extraction ===
Valid credit cards: ['1234 5678 9012 3456', '1234-5678-9012-3456']
Invalid credit cards: ['Invalid credit card number: 1234567890123456']

=== Time Extraction ===
Valid times: ['14:30', '2:30 PM', '02:30 pm', '7:00AM', '7:00']
Invalid times: ['Invalid time format: 25:00']
```

---

## What You Need

Just Python 3 — no extra packages required! It uses Python’s built-in `re` module for regex matching.

---

