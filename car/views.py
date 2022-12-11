from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, get_user_model
from car_auth.forms import UserCreateForm
from car.models import Car
from car.forms import CreateCarForm

UserModel = get_user_model()

def home_page(request):
    user = UserModel
    contex = {
        "user": user,
    }
    return render(request, "home_page.html", contex)

def about_page(request):
    return render(request, "about.html")

def contacts_page(request):
    return render(request, "contact.html")

def create_listing(request):
    user = UserModel
    car = Car.objects.all()
    if request.method == 'POST':
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateCarForm()
    context = {
        'form': form,
        "user": user,
    }
    return render(request, "car_create.html", context)
