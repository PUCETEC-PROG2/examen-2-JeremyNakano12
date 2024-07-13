from django.shortcuts import render
from .models import Movies
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def index(request):
    movie = Movies.objects.order_by('genre')
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'movie': movie}, request))

def movie(request, movie_id):
    movie = Movies.objects.get(pk = movie_id)
    template = loader.get_template('display_movie.html')
    context = {
        'movie': movie
    }
    return HttpResponse(template.render(context, request))