from django.urls import path, include
from .views import *

urlpatterns = [
    path('', AnimeView.as_view()),
    path('serial/', SerialView.as_view(), name='serial'),
    path('films', FilmsView.as_view(), name='films'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('<slug:slug>/', AnimeDetailView.as_view(), name='anime_detail'),

]