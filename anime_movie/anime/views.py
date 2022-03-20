from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from .utils import *
from .forms import *


class CategoryGenre:
    def get_genre(self):
        return Genre.objects.all()

    def get_categories(self):
        return Category.objects.all()


class AnimeView(CategoryGenre, ListView):
    model = Anime
    queryset = Anime.objects.filter(draft=False)
    template_name = 'anime/index.html'
    context_object_name = 'anime_list'


class AnimeDetailView(CategoryGenre, DetailView):
    model = Anime
    slug_field = 'url'


class SerialView(CategoryGenre, ListView):
    model = Anime
    queryset = Anime.objects.filter(draft=False)
    template_name = 'anime/serial.html'


def contactmenu(request):
    return render(request, 'anime/contact.html')


class FilmsView(CategoryGenre, ListView):
    model = Anime
    queryset = Anime.objects.filter(draft=False)
    template_name = 'anime/films.html'


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'anime/register.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'anime/login.html'


def logout_user(request):
    logout(request)
    return redirect('home')


class AddReview(View):

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        anime = Anime.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.anime = anime
            form.save()
        return redirect(anime.get_absolute_url())


class ViewRating(ListView):
    queryset = Anime.objects.all()
    template_name = 'anime/rating.html'
    context_object_name = 'anime_list'


def get_new_anime(count=4):
    anime = Anime.objects.order_by('id')[:count]
    return {'new_anime': anime}


class Search(ListView):
    template_name = 'anime/index.html'

    def get_queryset(self):
        return Anime.objects.filter(title__icontains=self.request.GET.get('q'))
     
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = self.request.GET.get("q")
        return context


class Date(ListView):
    template_name = 'anime/index.html'

    def get_queryset(self):
        return Anime.objects.filter(year=self.request.GET.get('q'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = self.request.GET.get("q")
        return context


