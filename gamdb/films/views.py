from django.shortcuts import render
from .models import Movie
from .models import Director

def homepage(request):
    context = {
        'movies': Movie.objects.all(),
    }
    return render(request, 'main.html', context)

def directors(request):
    context = {
        'title': 'Nej režiséři',
        'directors': Director.objects.all()
    }
    return render(request, 'directors.html', context)

def movies(request):
    context = {
        'title': 'Filmy',
        'movies': Movie.objects.all()
    }
    return render(request, 'movies.html', context)

def movie(request):
    context = {
        'title': 'Film',
        'movie': Movie.objects.all()
    }
    return render(request, 'movie.html', context)