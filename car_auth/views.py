from django.shortcuts import render
from django.contrib.auth import views as auth_views, get_user_model
from django.views import generic as views
from car_auth.forms import UserCreateForm
from django.urls import reverse_lazy

UserModel = get_user_model()

class SignInView(auth_views.LoginView):
    template_name = "login.html"

class SignUpView(views.CreateView):
    template_name = 'register.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('home page')

class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('home page')

class UserDetailsView(views.DetailView):
    template_name = 'profile.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user == self.object

        return context

class UserEditView(views.UpdateView):
    template_name = 'edit_profile.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'gender', 'email', 'profile_picture')

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={
            'pk': self.request.user.pk,
        })

class UserDeleteView(views.DeleteView):
    template_name = 'delete_profile.html'
    model = UserModel
    success_url = reverse_lazy('home page')
