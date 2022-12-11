from django.urls import path
from car.views import home_page, about_page, contacts_page, create_listing


urlpatterns = [
    path('', home_page, name='home page'),
    path('about/', about_page, name='about page'),
    path('contacts', contacts_page, name='contacts page'),
    path('create_listing', create_listing , name='create listing'),
    # path('car/<int:pk>/', include([
    #         path('', UserDetailsView.as_view(), name='car'),
    #         path('edit/', UserEditView.as_view(), name='edit car'),
    #         path('delete/', UserDeleteView.as_view(), name='delete car'),
    #     ])),
    ]