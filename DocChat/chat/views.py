from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from .forms import RegisterForm
 

# Create your views here.
def home(request):
    return render(request, 'chat/home.html')

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'registration/sign-up.html', {'form': form})