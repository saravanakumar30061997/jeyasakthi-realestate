from django import template
import re

register = template.Library()

@register.filter(name='indian_currency')
def indian_currency(value):
    """
    Converts a number into Indian currency format (e.g., 1,00,000 instead of 100,000).
    """
    try:
        value = int(value)  # Ensure it's an integer
        value_str = str(value)  # Convert to string

        # Split last three digits (thousands)
        last_three = value_str[-3:]
        rest = value_str[:-3]

        # Format the rest of the number in pairs of two digits
        if rest:
            rest = re.sub(r'(\d)(?=(\d{2})+(?!\d))', r'\1,', rest)
            value_str = rest + ',' + last_three
        else:
            value_str = last_three  # For numbers less than 1000

        return value_str
    except (ValueError, TypeError):
        return value  # Return original if conversion fails
