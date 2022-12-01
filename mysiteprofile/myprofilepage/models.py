from django.db import models
from django.forms import ModelForm
# Create your models here.
from django.utils import timezone


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    messages = models.TextField(max_length=2000)
    subjects = models.CharField(max_length=100, default=None)
    date_message = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
