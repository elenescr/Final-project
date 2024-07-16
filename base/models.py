from django.db import models
from django.contrib.auth.models import AbstractUser

class Subcat(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30)
    subcats = models.ManyToManyField(Subcat, blank=True, related_name="categories")

    def __str__(self):
        return self.name

class Items(models.Model):
    creator = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True, related_name="created_items")
    name = models.CharField(max_length=30)
    image = models.ImageField(blank=True, null=True)
    price = models.CharField(max_length=10)
    size = models.CharField(max_length=10)
    colour = models.CharField(max_length=30)
    subcat = models.ForeignKey(Subcat, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name

class State(models.Model):
    uploaded = models.DateField()
    is_sold = models.BooleanField()
    item = models.ForeignKey(Items, on_delete=models.CASCADE)  # Example: CASCADE deletes related states when an item is deleted

class User(AbstractUser):
    items = models.ManyToManyField(Items, blank=True, related_name="users_items")  # Adjusted related_name to avoid clash
    avatar = models.ImageField(null=True, default='avatar.svg')
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-created']
    def __str__(self):
        return self.body

