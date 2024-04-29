from django.db import models
from user.models import User

class Token(models.Model):
    token = models.TextField(200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'auth_token'
