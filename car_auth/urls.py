from django.urls import path, include
from car_auth.views import SignUpView, SignInView, SignOutView, UserDetailsView, UserEditView, UserDeleteView

urlpatterns = [
    path('register/', SignUpView.as_view(), name='register'),
    path('login/', SignInView.as_view(), name='login page'),
    path('logout/', SignOutView.as_view(), name='logout page'),
    path('profile/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='profile'),
        path('edit/', UserEditView.as_view(), name='edit user'),
        path('delete/', UserDeleteView.as_view(), name='delete user'),
    ])),
]