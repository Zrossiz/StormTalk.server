from django.urls import path
from .views import CreateChatAPIView, UpdateChatAPIView

urlpatterns = [
    path('', CreateChatAPIView.as_view()),
    path('<int:chat_id>', UpdateChatAPIView.as_view())
]