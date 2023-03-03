import re
import hashlib

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_phone(phone):
    pattern = r'^\+?[0-9]{10,}$'
    return bool(re.match(pattern, phone))

def encrypt_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
