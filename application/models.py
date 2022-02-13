from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Link(models.Model):
    long_url = models.TextField()
    short_url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='links')

    class Meta:
        ordering = ('created_at', )
