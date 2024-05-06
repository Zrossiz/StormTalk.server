from django.db import models
from user.models import User

class Chat(models.Model):
    first_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="first_user"
    )
    second_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="second_user"
    )
    last_message = models.TextField(max_length=2500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'chat'