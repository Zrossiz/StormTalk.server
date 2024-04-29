from django.db import models
from user.models import User


class Subscribe(models.Model):
    listener = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listener_id")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author_id")

    class Meta: 
        db_table = 'subscribe'