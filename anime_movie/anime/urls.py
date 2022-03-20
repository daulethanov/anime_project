from django.urls import path, include
from .views import *

urlpatterns = [
    path('', AnimeView.as_view(), name='home'),
    path('search/', Search.as_view(), name='search'),
    path('datanait', Date.as_view(), name='date'),
    path('serial/', SerialView.as_view(), name='serial'),
    path('contact/', contactmenu, name='contact'),
    path('films', FilmsView.as_view(), name='films'),
    path('rating/', ViewRating.as_view(), name='rating'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('<slug:slug>/', AnimeDetailView.as_view(), name='anime_detail'),
    path('review/<int:pk>/', AddReview.as_view(), name='add_review'),
    



]