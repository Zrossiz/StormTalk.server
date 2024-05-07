from django.urls import path
from .views import CreateChatAPIView

urlpatterns = [
    path('', CreateChatAPIView.as_view())
]