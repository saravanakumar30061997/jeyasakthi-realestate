from django import template
import locale

register = template.Library()

@register.filter(name='indian_currency')
def indian_currency(value):
    try:
        value = int(value)  # Ensure it's an integer
        locale.setlocale(locale.LC_ALL, 'en_IN')  # Set locale to Indian format
        return locale.format_string("%d", value, grouping=True)  # Format number
    except (ValueError, TypeError):
        return value  # Return original if conversion fails
