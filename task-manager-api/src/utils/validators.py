import re

EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$')


def validate_email(email):
    return bool(EMAIL_PATTERN.match(email)) if email else False


def is_valid_color(color):
    return bool(color and len(color) == 7 and color.startswith('#'))
