from django.contrib.auth.forms import UserCreationForm
from .models import User, Items, Contact
from django.forms import ModelForm

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class ItemForm(ModelForm):
    class Meta:
        model = Items
        fields = ['image', 'name', 'price', 'size', 'colour', 'subcat', 'description']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'username', 'email',  'items']

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['user_email', 'message']