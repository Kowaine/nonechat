from django.db import models

# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey("user.User", on_delete=models.CASCADE)
    content = models.CharField(max_length=128)
    time = models.DateTimeField()
