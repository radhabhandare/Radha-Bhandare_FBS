import re
from decimal import Decimal, InvalidOperation

def required_text(prompt):
    while True:
        value = input(prompt).strip()
        if value: return value
        print("This field cannot be empty.")

def read_int(prompt, minimum=0):
    while True:
        try:
            value = int(input(prompt).strip())
            if value >= minimum: return value
            print(f"Enter a whole number of at least {minimum}.")
        except ValueError: print("Enter a valid whole number.")

def read_optional_int(prompt, current):
    while True:
        value = input(f"{prompt} [{current}]: ").strip()
        if not value: return int(current)
        try:
            number = int(value)
            if number >= 0: return number
            print("Enter zero or a positive number.")
        except ValueError: print("Enter a valid whole number.")

def read_money(prompt):
    while True:
        try:
            value = Decimal(input(prompt).strip())
            if value.is_finite() and value >= 0: return value.quantize(Decimal("0.01"))
            print("Enter an amount of zero or more.")
        except (InvalidOperation, ValueError): print("Enter a valid amount, e.g. 125.50.")

def read_optional_money(prompt, current):
    while True:
        value = input(f"{prompt} [{current}]: ").strip()
        if not value: return Decimal(str(current)).quantize(Decimal("0.01"))
        try:
            amount = Decimal(value)
            if amount.is_finite() and amount >= 0: return amount.quantize(Decimal("0.01"))
            print("Enter an amount of zero or more.")
        except InvalidOperation: print("Enter a valid amount.")

def read_phone(prompt, optional=False):
    while True:
        value = input(prompt).strip()
        if optional and not value: return None
        digits = re.sub(r"\D", "", value)
        if len(digits) == 10: return digits
        print("Enter a valid 10-digit phone number.")

def read_email(prompt):
    while True:
        value = input(prompt).strip()
        if not value: return None
        if re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", value): return value
        print("Enter a valid email or leave it blank.")
