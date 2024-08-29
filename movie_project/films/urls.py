from django.urls import path
from .views import film_create, film_list

urlpatterns = [
    path('add/', film_create, name='film_create'),
    path('', film_list, name='film_list'),
]