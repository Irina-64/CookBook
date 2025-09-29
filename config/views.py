# config/views.py
from django.shortcuts import render

def home(request):
    # Можно передать данные для рекомендаций
    context = {
        'recommended': [],  # Пока пустой список
        'categories': [],  # Категории для фильтров
    }
    return render(request, 'main/home.html', context)
