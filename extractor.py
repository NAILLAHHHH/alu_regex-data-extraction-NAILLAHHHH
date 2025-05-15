# extractor.py
import re

def extract_emails(text):
    pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
    all_candidates = re.findall(r'\S+@\S+', text)
    valid = re.findall(pattern, text)
    invalid = [email for email in all_candidates if email not in valid]
    return valid, [f"Invalid email: {e}" for e in invalid]

def extract_urls(text):
    pattern = r"\bhttps?://[^\s<>\"']+|www\.[^\s<>\"']+\b"
    matches = re.findall(pattern, text)
    valid = []
    invalid = []
    for match in matches:
        if re.match(r'^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', match) or re.match(r'^www\.[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', match):
            valid.append(match)
        else:
            invalid.append(f"Invalid URL: {match}")
    return valid, invalid

def extract_phone_numbers(text):
    pattern = r'(\(\d{3}\)[-.\s]?\d{3}[-.\s]?\d{4}|\d{3}[-.\s]\d{3}[-.\s]\d{4})\b'
    valid = re.findall(pattern, text)
    all_candidates = re.findall(r'\d{3}[-.\s]?\d{2,4}[-.\s]?\d{2,4}', text)
    invalid = [n for n in all_candidates if n not in valid]
    return valid, [f"Invalid phone number: {n}" for n in invalid]

def extract_credit_cards(text):
    pattern = r'\b(?:\d{4}[-\s]){3}\d{4}\b'
    valid = re.findall(pattern, text)
    all_candidates = re.findall(r'\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}', text)
    invalid = [c for c in all_candidates if c not in valid]
    return valid, [f"Invalid credit card number: {c}" for c in invalid]

def extract_times(text):
    pattern = r'\b((1[0-2]|0?[1-9]):[0-5]\d\s?[APap][Mm]|(2[0-3]|[01]?\d):[0-5]\d)\b'
    valid_matches = re.findall(pattern, text)
    valid = [match[0] for match in valid_matches if match[0]]
    all_times = re.findall(r'\d{1,2}:\d{2}(?:\s?[APap][Mm])?', text)
    invalid = [t for t in all_times if t not in valid]
    return valid, [f"Invalid time format: {t}" for t in invalid]
