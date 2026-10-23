import re

def required_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")

def read_int(prompt, minimum=0):
    while True:
        try:
            value = int(input(prompt).strip())
            if value < minimum:
                print(f"Enter a number greater than or equal to {minimum}.")
                continue
            return value
        except ValueError:
            print("Please enter a whole number.")

def read_money(prompt, minimum=0.0):
    while True:
        try:
            value = float(input(prompt).strip())
            if value < minimum:
                print(f"Enter an amount greater than or equal to {minimum}.")
                continue
            return round(value, 2)
        except ValueError:
            print("Please enter a valid amount, for example 125.50.")

def read_phone(prompt, optional=False):
    while True:
        value = input(prompt).strip()
        if optional and not value:
            return None
        if re.fullmatch(r"[0-9]{10}", value):
            return value
        print("Enter a valid 10-digit phone number.")

def read_email(prompt, optional=True):
    while True:
        value = input(prompt).strip()
        if optional and not value:
            return None
        if re.fullmatch(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", value):
            return value
        print("Enter a valid email address.")
