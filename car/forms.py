from django import forms
from car.models import Car
from django.contrib.auth import views as auth_views, get_user_model

UserModel = get_user_model()

class CreateCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('car_make', 'car_model', 'engine_type', 'price', 'mileage', 'model_year', 'current_location',
                  'contact_number', 'picture', 'description')

class EditCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('car_make', 'car_model', 'engine_type', 'price', 'mileage', 'model_year', 'current_location',
                  'contact_number', 'picture', 'description')

class CarDeleteForm(CreateCarForm):

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance