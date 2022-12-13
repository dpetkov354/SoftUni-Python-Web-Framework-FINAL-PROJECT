from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, get_user_model
from car_auth.forms import UserCreateForm
from car.models import Car
from car.forms import CreateCarForm, EditCarForm, CarDeleteForm
from car.utils import get_car_by_name_and_username, is_owner
from django.core.paginator import Paginator
from django.views import generic as views


UserModel = get_user_model()


def home_page(request):
    user = UserModel
    contex = {
        "user": user,
    }
    return render(request,
                  "home_page.html",
                  contex
                  )


def about_page(request):
    return render(request,
                  "about.html"
                  )


def contacts_page(request):
    return render(request,
                  "contact.html"
                  )

@login_required
def create_listing(request):
    if request.method == 'GET':
        form = CreateCarForm()
    else:
        form = CreateCarForm(request.POST)
        if form.is_valid():
            care = form.save(commit=False)
            care.user = request.user
            care.save()
            return redirect('home page')

    context = {
        'form': form,
    }

    return render(request,
                  "car_create.html",
                  context
                  )


class MyListingsView(views.DetailView):
    template_name = 'my_listings.html'
    model = UserModel
    cars_paginate_by = 1

    def get_cars_page(self):
        return self.request.GET.get('page', 1)

    def get_paginated_cars(self):
        car = self.get_cars_page()

        cars = self.object.car_set \
            .order_by('-publication_date')

        paginator = Paginator(cars, self.cars_paginate_by)
        return paginator.get_page(page)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user == self.object

        context['cars'] = self.object.car_set.all()

        context['cars_count'] = self.object.car_set.count()

        return context


def details_car(request, username, car_slug):
    car = get_car_by_name_and_username(car_slug, username)

    context = {
        'car': car,
        'username': username,
        'is_owner': car.user == request.user,
    }

    return render(
        request,
        'car_details.html',
        context,
    )

@login_required
def edit_car(request, username, car_slug):
    car = get_car_by_name_and_username(car_slug, username)

    if not is_owner(request, car):
        return redirect('details car', username=username, car_slug=car_slug)

    if request.method == 'GET':
        form = EditCarForm(instance=car)
    else:
        form = EditCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('details car', username=username, car_slug=car_slug)

    context = {
        'form': form,
        'car_slug': car_slug,
        'username': username,
    }

    return render(
        request,
        'car_edit.html',
        context,
    )

def delete_car(request, username, car_slug):
    car = get_car_by_name_and_username(car_slug, username)

    if request.method == 'GET':
        form = CarDeleteForm(instance=car)
    else:
        form = CarDeleteForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('my listings', pk=request.user.pk)

    context = {
        'form': form,
        'car_slug': car_slug,
        'username': username,
    }

    return render(
        request,
        'car_delete.html',
        context,
    )