from django.urls import path
from .views import UserAPIView


urlpatterns = [
    path('auth/registration', UserAPIView.as_view())
]