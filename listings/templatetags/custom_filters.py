from django import template
import re

register = template.Library()

@register.filter(name='indian_currency')
def indian_currency(value):
    try:
        value = int(value)  # Ensure it's an integer
        # Convert number to string and apply Indian number system formatting
        value_str = f"{value:,}"  # Standard thousand separator formatting
        # Modify formatting to match Indian system (1,00,000 instead of 100,000)
        indian_format = re.sub(r'(\d)(?=(\d\d)+\d$)', r'\1,', value_str)
        return indian_format
    except (ValueError, TypeError):
        return value  # Return original if conversion fails
