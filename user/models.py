from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=14, unique=True)
    password = models.CharField(max_length=14)
    last_ip = models.CharField(max_length=15)
    register_time = models.DateTimeField()