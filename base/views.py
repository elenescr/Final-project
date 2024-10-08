from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import Items
from .models import User, Subcat, Category, Comment
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import MyUserCreationForm, ItemForm, UserForm, ContactForm
from .seeder import seeder_func
from django.contrib import messages

from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
def home (request):

    q = request.GET.get('q') if request.GET.get('q') != None else ""
    items = Items.objects.filter(Q(name__icontains=q) | Q(description__icontains=q)| Q(subcat__name__icontains=q) )
    subcats = Subcat.objects.all()
    categories = Category.objects.all()
    # seeder_func()
    context = {"items" : items, "subcats":subcats,"categories":categories, 'q' : q}
    if request.GET.get('q') != None:
        return render(request, 'base/product.html', context)
    else:
        return render(request,'base/home.html', context)
def account(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ""
    items = Items.objects.filter(Q(name__icontains=q) | Q(description__icontains=q) | Q(subcat__name__icontains=q) )

    context = {"items": items}
    return render(request,'base/account.html', context)

def contact(request):

    return render(request,'base/contact.html')
@login_required(login_url='login')
def favourites (request, pk):
    user= User.objects.get(id= int(pk))
    q = request.GET.get('q') if request.GET.get('q') != None else ""
    items = user.items.filter(Q(name__icontains=q) | Q(description__icontains=q) | Q(subcat__name__icontains=q))
    context = {"items": items, "user" : user}
    return render(request,'base/favourites.html', context)
def product(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ""
    items = Items.objects.filter(Q(name__icontains=q) | Q(description__icontains=q)| Q(subcat__name__icontains=q) )
    subcats = Subcat.objects.all()
    categories = Category.objects.all()
    context = {"items": items, "subcats": subcats, "categories": categories}
    return render(request,'base/product.html', context)
def about(request, id):
    item= Items.objects.get(id=id)
    item_comments= item.comment_set.all()

    if request.method == "POST":
        comment = Comment.objects.create(
            user = request.user,
            item = item,
            body = request.POST.get('body')
        )
    context = {'item':item, 'comments': item_comments }
    return render(request,'base/about.html', context)
def charity(request):
    return render(request,'base/charity.html')
def adding(request, id):
    item = Items.objects.get(id=id)
    user = request.user
    user.items.add(item)
    return redirect('favourites', request.user.id)


def delete(request, id):
    item = Items.objects.get(id=id)
    if request.method== "POST":
       request.user.items.remove(item)
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
          messages.error(request,"This username doesn't exist!")
      user = authenticate(request, username=username, password=password)
      if user is not None:
          login(request, user)
          return redirect('home')
      else:
          messages.error(request, "This username or password is incorrect!")

  return render(request,'base/login.html' )
def logout_user(request):
    logout(request)
    return redirect('home')
def register_page(request):
 form = MyUserCreationForm()
 context = {'form':form}
 if request.user.is_authenticated:
      return redirect('home')

 if request.method == 'POST':
     form = MyUserCreationForm(request.POST)

     if form.is_valid():
         user= form.save()
         login(request,user)
         return redirect('home')

 return render(request, 'base/register.html', context )


def add_item(request):
    form = ItemForm()
    items = Items.objects.all()
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            if 'image' in request.FILES:
                new_item.image = request.FILES['image']
            new_item.creator_id = request.user.id  #
            new_item.save()
            return redirect('home')
        else:
            pass
    else:
        form = ItemForm()

    context = {'form': form, 'items': items}
    return render(request, 'base/add_item.html', context)



def delete_item(request, id) :
    item = get_object_or_404(Items, id=id)

    if request.method == 'POST':
        item.image.delete()
        item.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': item})

@login_required(login_url='login')
def update_user(request):
    user = request.user
    form = UserForm(instance=user)
    if request.method =='POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('account')
    return render(request, 'base/update_user.html',{'form':form})


def delete_comment(request, id) :
    print('reached delete cooment')
    comment = Comment.objects.get(id=id)
    item= comment.item
    if request.method == 'POST':
        print('reached post request')
        comment.delete()
        print('deleted')
        return redirect('about', item.id)
    return render(request, 'base/delete.html', {'obj': comment})

@login_required(login_url='login')
def update_item(request, item_id):
    item = get_object_or_404(Items, id=item_id)
    form = ItemForm(instance=item)
    if request.method =='POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('account')
    return render(request, 'base/update_item.html',{'form':form})

def contact_view (request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'base/contact.html',{'form':form})

def info_view (request):
    return render(request, 'base/info.html')

def success(request):

    return render(request,'base/success.html')
# def check() :
#     item = Items.objects.filter(id=1).first()
#     print(item)
# check()