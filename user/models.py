from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=200)
    email = models.EmailField(max_length=100, unique=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_authenticated(self):
        return True

    class Meta:
        db_table = 'user'