from django.urls import path
from .views import CreateSubcsribeAPIView, UpdateSubscribeAPIView

urlpatterns = [
    path('', CreateSubcsribeAPIView.as_view()),
    path('<int:post_id>', UpdateSubscribeAPIView.as_view())
]