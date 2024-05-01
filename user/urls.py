from django.urls import path
from .views import RegistrationUserAPIView, LoginUserAPIView


urlpatterns = [
    path('auth/registration', RegistrationUserAPIView.as_view()),
    path('auth/login', LoginUserAPIView.as_view())
]