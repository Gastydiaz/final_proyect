from django.urls import path
from movies.views import create_movie, list_movies, index,create_studio,list_studio,create_director, list_director, about_me,movie_update,MovieDeleteView,studio_update,StudioDeleteView,director_update,DirectorDeleteView

urlpatterns = [
    path('', index, name='index'),
    path('create-movies/',create_movie),
    path('list-movies/', list_movies),
    path('create-studio/', create_studio),
    path('list-studio/', list_studio),
    path('create-director/', create_director),
    path('list-director/', list_director),
    path('about-me/', about_me),
    path('movies-update/<int:pk>/',movie_update),
    path('movies-delete/<int:pk>/',MovieDeleteView.as_view()),
    path('studio-update/<int:pk>/',studio_update),
    path('studio-delete/<int:pk>/',StudioDeleteView.as_view()),
    path('director-update/<int:pk>/',director_update),
    path('director-delete/<int:pk>/',DirectorDeleteView.as_view()),


    ] 