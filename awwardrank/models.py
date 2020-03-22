from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.description
