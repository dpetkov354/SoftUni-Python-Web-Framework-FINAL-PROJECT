from django.urls import path, include
from car.views import home_page, about_page, contacts_page, create_listing, details_car, edit_car, delete_car, MyListingsView, search_cars


urlpatterns = [
    path('', home_page, name='home page'),
    path('about/', about_page, name='about page'),
    path('contacts', contacts_page, name='contacts page'),
    path('create_listing', create_listing , name='create listing'),
    path('search_cars', search_cars , name='search cars'),
    path('my_listings/<int:pk>/', MyListingsView.as_view() , name='my listings'),
    path('<str:username>/car/<slug:car_slug>/', include([
            path('', details_car, name='details car'),
            path('edit/', edit_car, name='edit car'),
            path('delete/', delete_car, name='delete car'),
        ])),
    ]