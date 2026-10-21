import re

def validate_name(name):
    return bool(re.fullmatch(r'[A-Za-z ]{2,100}', name.strip()))

def validate_username(username):
    return bool(re.fullmatch(r'[A-Za-z0-9_]{3,50}', username))

def validate_quantity(quantity):
    try:
        return int(quantity) > 0
    except ValueError:
        return False

def validate_location(location):
    return bool(
        re.fullmatch(r'[A-Za-z0-9 ,.-]{2,100}', location.strip())
    )


def validate_priority(priority):
    return priority.lower() in ['low', 'medium', 'high']

def validate_category(category):
    return bool(category.strip()) and len(category) <= 50
