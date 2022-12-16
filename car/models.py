from django.contrib.auth import get_user_model
from django.db import models
from django.core import validators
from common.validators import validate_only_letters, validate_integer
from common.model_mixins import StrFromFieldsMixin
from django.utils.text import slugify

UserModel = get_user_model()


class Car(StrFromFieldsMixin, models.Model):
    str_fields = ('id', 'model')

    MAX_LENGHT = 30
    MIN_LENGHT = 2

    GASOLINE = "Gasoline"
    DIESEL = "Diesel"
    ELECTRIC = "Electric"
    HYBRID = "Hybrid"

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
        )
    )

    engine_type = models.CharField(
        max_length=MAX_LENGHT,
        choices=ENGINE_CHOICES,
        default=GASOLINE,
    )

    price = models.IntegerField(
        null=False,
        blank=False,
        validators=(
            validate_integer,
        )
    )

    mileage = models.IntegerField(
        null=False,
        blank=False,
        validators=(
            validate_integer,
        )
    )
    
    model_year = models.IntegerField(
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

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
       UserModel,
       on_delete=models.CASCADE,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.car_model}')
        return super().save(*args, **kwargs)
