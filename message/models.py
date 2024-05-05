from django.db import models
from user.models import User
from chat.models import Chat


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="messages")
    text = models.CharField(max_length=2500)
    read = models.BooleanField(False)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_message")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'message'