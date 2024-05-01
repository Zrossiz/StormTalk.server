from django.db import models
from user.models import User

class AuthToken(models.Model):
    token = models.CharField(max_length=200)
    exp = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'auth_token'