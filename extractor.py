import re

def extract_emails(text):
    pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
    return re.findall(pattern, text)

def extract_urls(text):
    pattern =r'\b(?:https?://|www\.)[^\s"<>()]+'
    return re.findall(pattern, text)

def extract_phone_numbers(text):
    pattern = r'(?:\(\d{3}\)[-. ]?\d{3}[-. ]?\d{4}|\d{3}[-. ]\d{3}[-. ]\d{4})\b'
    return re.findall(pattern, text)

def extract_credit_cards(text):
    pattern = r'\b(?:\d{4}[-\s]){3}\d{4}\b'
    return re.findall(pattern, text)

def extract_times(text):
    pattern = r'\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b'
    return re.findall(pattern, text)

