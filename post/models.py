from django.db import models
from user.models import User


class Post(models.Model):
    image = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField()
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'post'