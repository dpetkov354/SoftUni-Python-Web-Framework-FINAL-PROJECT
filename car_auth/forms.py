from django.contrib.auth import forms as auth_forms
from django.contrib.auth import views as auth_views, get_user_model
from django.contrib.auth.forms import UsernameField

UserModel = get_user_model()

class UserCreateForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("username", "email")
        field_classes = {'username': auth_forms.UsernameField}

class UserEditForm(auth_forms.UserChangeForm):
    class Meta:
        model = UserModel
        fields = ('first_name',)
        field_classes = {'username': auth_forms.UsernameField}