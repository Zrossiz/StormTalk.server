from django.db import models
from user.models import User
import uuid

class Chat(models.Model):
    initiator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="initiator_chat"
    )
    acceptor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="acceptor_name"
    )
    short_id = models.CharField(max_length=255, default=uuid.uuid4, unique=True)

    class Meta:
        db_table = 'chat'