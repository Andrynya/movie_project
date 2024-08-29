from django.shortcuts import render, redirect
from .models import Film
from .forms import FilmForm
# Create your views here.
def film_create(request):
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем данные в базу
            return redirect('film_list')  # Перенаправляем на страницу со списком фильмов
    else:
        form = FilmForm()
    return render(request, 'films/film_form.html', {'form': form})

def film_list(request):
    films = Film.objects.all()  # Получаем все фильмы из базы данных
    return render(request, 'films/film_list.html', {'films': films})