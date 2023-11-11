from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
 

# Create your views here.
def homepage(request):
    return render(request, 'chat/home.html')

