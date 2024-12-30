import re
from django import template

register = template.Library()

def indian_currency_format(value):
    """
    Converts a number into Indian currency format (lakhs and crores).
    Example: 5000000 becomes 50,00,000.00
    """
    if not isinstance(value, (int, float)):
        try:
            value = float(value)
        except ValueError:
            return value

    value = f"{value:.2f}"  # Ensure two decimal points
    parts = value.split(".")
    integer_part = parts[0]
    decimal_part = parts[1] if len(parts) > 1 else ""

    # Apply Indian number format regex
    integer_part = re.sub(r"(?<=\d)(?=(\d{2})+\d$)", ",", integer_part)

    return f"₹{integer_part}.{decimal_part}" if decimal_part else f"₹{integer_part}"

@register.filter
def inr(value):
    return indian_currency_format(value)
