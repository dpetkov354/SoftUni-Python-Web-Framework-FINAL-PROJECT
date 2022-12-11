from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('car.urls')),
    path('auth/', include('car_auth.urls'))
]
