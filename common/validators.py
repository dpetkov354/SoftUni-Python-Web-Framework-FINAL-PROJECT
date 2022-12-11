from django.core import exceptions


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise exceptions.ValidationError('Only letters are allowed')

def validate_integer(value):
    if value <= 0:
        raise exceptions.ValidationError('Cannot be less than or equal to zero.')
