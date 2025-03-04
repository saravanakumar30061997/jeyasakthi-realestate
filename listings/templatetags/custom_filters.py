from django import template

register = template.Library()

@register.filter(name='indian_currency')
def indian_currency(value):
    try:
        value = int(value)  # Ensure it's an integer
        return "{:,.0f}".format(value).replace(",", ".").replace(".", ",")  # Indian style formatting
    except (ValueError, TypeError):
        return value  # Return original if conversion fails
