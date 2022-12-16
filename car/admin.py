from django.contrib import admin
from car.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass
