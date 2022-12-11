from django import forms
from car.models import Car
from django.contrib.auth import views as auth_views, get_user_model

UserModel = get_user_model()

class CreateCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"
