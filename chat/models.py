from django.db import models
from user.models import User
from message.models import Message

class Chat(models.Model):
    first_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="first_user"
    )
    second_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="second_user"
    )
    last_message = models.ForeignKey(
        Message, on_delete=models.CASCADE, related_name="last_message"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'chat'