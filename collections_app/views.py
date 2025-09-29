from django.http import HttpResponse

def index(request):
    return HttpResponse("Раздел коллекций работает!")
