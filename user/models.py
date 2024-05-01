from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    is_active = models.BooleanField(default=False)

    class Meta:
        db_table = 'user'