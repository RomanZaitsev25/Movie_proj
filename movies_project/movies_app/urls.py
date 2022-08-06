from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_all_movie),
    # path('movie/<int:id_movie>', views.show_one_movie, name='movie_detail'),
    path('movie/<str:slug_movie>', views.show_one_movie, name='movie_detail'),
    # path('director/str:slug_director', views.director_movie, name='director')

]
