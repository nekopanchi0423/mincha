from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class List(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1,)

    def __str__(self):
        return self.title
        
class Card(models.Model):
    title = models.CharField(max_length=200, default='##タイトルが未記入です##')
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1,)
    created_at = models.DateTimeField(default=timezone.now)
    list = models.ForeignKey(List, on_delete=models.CASCADE, default=1,)