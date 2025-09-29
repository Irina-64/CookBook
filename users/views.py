from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    """Главная страница модуля пользователей"""
    return render(request, 'users/index.html')

def login(request):
    return render(request, 'main/login.html')

def register(request):
    return render(request, 'main/register.html')

def profile(request):
    return render(request, 'main/profile.html')