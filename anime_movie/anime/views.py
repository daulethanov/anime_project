from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from .models import *


class AnimeView(ListView, ):
    model = Anime
    queryset = Anime.objects.filter(draft=False, )
    template_name = 'anime/index.html'
    context_object_name = 'anime_list'


class AnimeDetailView(DetailView):
    model = Anime
    slug_field = 'url'


class SerialView(ListView):
    model = Anime
    queryset = Anime.objects.filter(draft=False)
    template_name = 'anime/serial.html'


class ContactView(View):
    template_name = 'anime/contact.html'


class FilmsView(ListView):
    model = Anime
    queryset = Anime.objects.filter(draft=False)
    template_name = 'anime/films.html'
