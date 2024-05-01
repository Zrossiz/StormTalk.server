from .views import PostAPIView
from django.urls import path


urlpatterns = [
    path('', PostAPIView.as_view())
]