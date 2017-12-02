from django.db import models

class Message(models.Model):
    created = models.DateTimeField(auto_now=True)
    text = models.TextField()
    firstname = models.CharField(max_length=128, default="anonymous")
