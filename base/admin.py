from django.contrib import admin
from .models import Items, User, State, Category, Subcat, Comment
# Register your models here.
admin.site.register(Items)
admin.site.register(State)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Subcat)
admin.site.register(Comment)