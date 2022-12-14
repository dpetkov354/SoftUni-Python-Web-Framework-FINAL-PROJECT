from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, get_user_model
from car_auth.forms import UserCreateForm
from car.models import Car
from car.forms import CreateCarForm, EditCarForm, CarDeleteForm
from car.utils import get_car_by_name_and_username, is_owner
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic as views
from car.models import Car

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
    cars_paginate_by = 3

    def get_cars_page(self):
        return self.request.GET.get('page', 1)

    def get_paginated_cars(self):
        page = self.get_cars_page()

        cars = self.object.car_set \
            .order_by('car_make')

        paginator = Paginator(cars, self.cars_paginate_by)
        return paginator.get_page(page)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user == self.object

        context['cars'] = self.get_paginated_cars()

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

def search_cars(request):
    query_cars = Car.objects.all()

    search_make_query = request.GET.get("search_make")
    search_model_query = request.GET.get("search_model")

    search_year_query = request.GET.get("search_year")
    search_price_query = request.GET.get("search_price")

    if search_make_query != '' and search_make_query is not None:
        query_cars = query_cars.filter(car_make__icontains=search_make_query)

    if search_model_query != '' and search_model_query is not None:
        query_cars = query_cars.filter(car_model__icontains=search_model_query)

    if search_year_query != '' and search_year_query is not None:
        query_cars = query_cars.filter(model_year__gte=search_year_query)

    if search_price_query != '' and search_price_query is not None:
        query_cars = query_cars.filter(price__lte=search_price_query)

    paginator = Paginator(query_cars, 3)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        "query_cars": query_cars,
        "listing_count": query_cars.count(),
        'posts': posts,
    }

    return render(request, "search_listings.html", context)
