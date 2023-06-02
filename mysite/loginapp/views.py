# views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'profile.html')

def login(request):
    return render(request, 'login.html')
def home(request):
    return render(request, 'dashboard/home.html')