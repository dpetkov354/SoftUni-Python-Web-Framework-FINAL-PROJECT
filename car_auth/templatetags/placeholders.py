from django.template import Library

register = Library()


@register.filter
def placeholder(filed, text):
    filed.field.widget.attrs['placeholder'] = text
    return filed
