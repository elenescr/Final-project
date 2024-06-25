from django.shortcuts import render
from django.http import HttpResponse

def home (request):
    return render(request,'base/home.html')
def account(request):
    return render(request,'base/account.html')
