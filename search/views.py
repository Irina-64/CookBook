from django.http import HttpResponse

def index(request):
    return HttpResponse("Поиск рецептов работает!")