from django.shortcuts import render
from .models import Movie
from .models import Director
from .models import Actor
from .models import Genre
from django.db.models import Q

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

def director(request, id):
    context = {
        "director": Director.objects.get(id=id)
    }
    return render(request, 'director.html', context)

def movies(request):
    movie_querystring = Movie.objects.all()
    search = request.GET.get('search')
    if search:
        movie_querystring = movie_querystring.filter(name__icontains=search)

    context = {
        'title': 'Filmy',
        'movies': movie_querystring,
        'search': search
    }
    return render(request, 'movies.html', context)

def movie(request, id):
    context = {
        'title': 'Film',
        'movie': Movie.objects.get(id=id)
    }
    return render(request, 'movie.html', context)

def actors(request):
    context = {
        "actors": Actor.objects.all()
    }
    return render(request, 'actors.html', context)

def actor(request, id):
    context = {
        "actor": Actor.objects.get(id=id)
    }
    return render(request, 'actor.html', context)