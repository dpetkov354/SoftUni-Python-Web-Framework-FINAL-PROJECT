from django.contrib.auth import get_user_model
from django.db import models
from django.core import validators
from common.validators import validate_only_letters, validate_integer

UserModel = get_user_model()

class Car(models.Model):
    MAX_LENGHT = 30
    MIN_LENGHT = 2

    GASOLINE = "GS"
    DIESEL = "DS"
    ELECTRIC = "EL"
    HYBRID = "HB"

    ENGINE_CHOICES = (
        (GASOLINE, "Gasoline"),
        (DIESEL, "Diesel"),
        (ELECTRIC, "Electric"),
        (HYBRID, "Hybrid"),
    )

    car_make = models.CharField(
        max_length=MAX_LENGHT,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(MIN_LENGHT),
            validate_only_letters,
        )
    )

    car_model = models.CharField(
        max_length=MAX_LENGHT,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(MIN_LENGHT),
            validate_only_letters,
        )
    )

    engine_type = models.CharField(
        max_length=MAX_LENGHT,
        choices=ENGINE_CHOICES,
        default=GASOLINE,
    )

    price = models.IntegerField(
        max_length=MAX_LENGHT,
        null=False,
        blank=False,
        validators=(
            validate_integer,
        )
    )

    mileage = models.IntegerField(
        max_length=MAX_LENGHT,
        null=False,
        blank=False,
        validators=(
            validate_integer,
        )
    )
    
    model_year = models.IntegerField(
        max_length=MAX_LENGHT,
        null=False,
        blank=False,
        validators=(
            validate_integer,
        )
    )

    current_location = models.CharField(
        max_length=MAX_LENGHT,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(MIN_LENGHT),
        )
    )

    contact_number = models.CharField(
        max_length=MAX_LENGHT,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(MIN_LENGHT),
        )
    )

    picture = models.URLField(
        null=False,
        blank=False,
    )

    description = models.CharField(
        max_length=150,
        null=True,
        blank=True,
        validators=(
            validators.MinLengthValidator(MIN_LENGHT),
        )
    )
