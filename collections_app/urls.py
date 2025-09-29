from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='collections_index'),
]
