from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Items
from .models import User, Subcat, Category
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import MyUserCreationForm, ItemForm
def home (request):
    q = request.GET.get('q') if request.GET.get('q') != None else ""
    items = Items.objects.filter(Q(name__icontains=q) | Q(description__icontains=q)| Q(subcat__name__icontains=q))
    subcats = Subcat.objects.all()
    categories = Category.objects.all()
    context = {"items" : items, "subcats":subcats,"categories":categories}
    return render(request,'base/home.html', context)
def account(request):
    return render(request,'base/account.html')
@login_required(login_url='login')
def favourites (request, pk):
    user= User.objects.get(id= int(pk))
    q = request.GET.get('q') if request.GET.get('q') != None else ""
    items = user.item.filter(Q(name__icontains=q) | Q(description__icontains=q) | Q(subcat__name__icontains=q))
    context = {"items": items, "user" : user}
    return render(request,'base/favourites.html', context)
def cart(request):
    return render(request,'base/cart.html')
def charity(request):
    return render(request,'base/charity.html')
def adding(request, id):
    item = Items.objects.get(id=id)
    user = request.user
    user.item.add(item)
    return redirect("home")

def delete(request, id):
    item = Items.objects.get(id=id)
    if request.method== "POST":
       request.user.item.remove(item)
       return redirect('favourites', request.user.id)
    return render(request,'base/delete.html', {'item':item})

def login_page(request):
  if request.user.is_authenticated:
      return redirect('home')
  if request.method == 'POST':
      username= request.POST.get('username')
      password = request.POST.get('password')
      try:
          user= User.objects.get (username=username)
      except:
          pass
      user = authenticate(request, username=username, password=password)
      if user is not None:
          login(request, user)
          return redirect('home')
      else:
        pass

  return render(request,'base/login.html' )
def logout_user(request):
    logout(request)
    return redirect('home')
def register_page(request):
 form = MyUserCreationForm()
 context = {'form':form}
 if request.method == 'POST':
     form = MyUserCreationForm(request.POST)
     if form.is_valid():
         user= form.save()
         login(request,user)
         return redirect('home')
 return render(request, 'base/register.html', context )

def add_item (request):
    form = ItemForm()

    items= Items.objects.all()
    # if request.method == 'POST':
    #   form = ItemForm(request.POST)
    #   new_item = Items(image = request.FILES['image'], name = form.data['name'], price = form.data['price'],
    #                    size = form.data['size'], colour = form.data['colour'], subcat=form.cleaned_data.get('subcat'),
    #                    description = form.data['description'])
    #   new_item.save()
    #   return redirect('home')
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            if 'image' in request.FILES:
                new_item.image = request.FILES['image']
            new_item.save()
            return redirect('home')
    else:
        form = ItemForm()
    context={'form':form}
    return render(request, 'base/add_item.html', context)