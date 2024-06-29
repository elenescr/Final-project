from django.db import models
class Items(models.Model):
    name = models.CharField(max_length=30)
    image = models.CharField(max_length=200)
    price = models.CharField(max_length=10)
    size = models.CharField(max_length=10)
    colour = models.CharField(max_length=30)
    description = models.TextField(max_length=300)