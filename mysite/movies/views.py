from django.shortcuts import render
from . models import Movies


def movies_view(requests):
    movies = Movies.objects.all()

    return render(requests, 'movies/movies_view.html', context={'movies': movies})