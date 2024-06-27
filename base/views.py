from django.shortcuts import render
from django.http import HttpResponse
from .models import Items
from django.db.models import Q
def home (request):
    q = request.GET.get('q') if request.GET.get('q') != None else ""
    items = Items.objects.filter(Q(name__icontains=q) | Q(description__icontains=q))
    context = {"items" : items}
    return render(request,'base/home.html', context)
def account(request):
    return render(request,'base/account.html')
def favourites (request):
    return render(request,'base/favourites.html')
def cart(request):
    return render(request,'base/cart.html')
def charity(request):
    return render(request,'base/charity.html')