import re

def extract_emails(text):
    return re.findall(r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b', text)

def extract_urls(text):
    return re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', text)

def extract_phone_numbers(text):
    return re.findall(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', text)

def extract_credit_cards(text):
    return re.findall(r'\b(?:\d{4}[-\s]?){3}\d{4}\b', text)

def extract_times(text):
    return re.findall(r'\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b', text)

