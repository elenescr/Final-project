from django.db import models
from django.contrib.auth.models import AbstractUser

class Subcat(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=30)
    subcat = models.ManyToManyField(Subcat, blank=True, related_name="subcat")
    def __str__(self):
        return self.name





class Items(models.Model):
    name = models.CharField(max_length=30)
    image = models.CharField(max_length=200)
    price = models.CharField(max_length=10)
    size = models.CharField(max_length=10)
    colour = models.CharField(max_length=30)
    subcat = models.ForeignKey(Subcat, on_delete=models.SET("unknown"))
    description = models.TextField(max_length=200)

    def __str__ (self):
        return self.name

class State(models.Model):
        uploaded = models.DateField()
        is_sold = models.BooleanField()
        item = models.ForeignKey(Items, on_delete=models.SET("unknown"))
class User(AbstractUser):
    item = models.ManyToManyField(Items, blank=True, related_name="item")
