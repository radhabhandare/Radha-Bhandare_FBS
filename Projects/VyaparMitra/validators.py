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


def read_optional_int(prompt, current_value=None, minimum=0):

    while True:
        value = input(prompt).strip()

        if not value:
            return current_value

        try:
            number = int(value)

            if number < minimum:
                print(f"Enter a number greater than or equal to {minimum}.")
                continue

            return number

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


def read_optional_money(prompt, current_value=None, minimum=0.0):
    """Press Enter to keep the current amount."""

    while True:
        value = input(prompt).strip()

        if not value:
            return current_value

        try:
            number = float(value)

            if number < minimum:
                print(f"Enter an amount greater than or equal to {minimum}.")
                continue

            return round(number, 2)

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

        pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

        if re.fullmatch(pattern, value):
            return value

        print("Enter a valid email address.")
