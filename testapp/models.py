from django.db import models

# Create your models here.


class Band(models.Model):
    name = models.CharField(max_length=128, unique=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
