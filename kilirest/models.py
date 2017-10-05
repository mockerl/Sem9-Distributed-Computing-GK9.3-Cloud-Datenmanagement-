from django.db import models

# Create your models here.


class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    username = models.CharField(max_length=100, blank=False)
    name = models.CharField(max_length=100, blank=False)
    surname = models.CharField(max_length=100, blank=False)
    password = models.CharField(max_length=100, blank=False)

