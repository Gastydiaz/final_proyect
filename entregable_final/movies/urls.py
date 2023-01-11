from django.urls import path
from movies.views import create_movie, list_movies, index,create_studio,list_studio,create_director, list_director


urlpatterns = [
    path('', index, name='index'),
    path('create-movies/',create_movie),
    path('list-movies/', list_movies),
    path('create-studio/', create_studio),
    path('list-studio/', list_studio),
    path('create-director/', create_director),
    path('list-director/', list_director),

    ] 