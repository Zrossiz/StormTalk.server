from django.urls import path
from .views import CreateSubcsribeAPIView

urlpatterns = [
    path('', CreateSubcsribeAPIView.as_view())
]