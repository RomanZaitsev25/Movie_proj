from django.db.models import F, Max, Min, Avg, Value
from django.shortcuts import render, get_object_or_404

from .models import Movie, Director


# Надо импортировать все фильмы из файла models, вызвав клаа Movie,
# И передать его контекст render в виде словоря. Далее можем обращаться
# к шаблону.


# Create your views here.


def show_all_movie(requets):
    # movies = Movie.objects.order_by(F('year').desc(nulls_last=True))
    movies = Movie.objects.annotate(
        true_bool=Value(True),
        false_bool=Value(False),
        str_fild=Value('Hello'),
        int_fild=Value(1254),
        new_budget=F('budget') + 100,
        rating_year=F('year') + F('rating'),
    )
    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'))
    # for movie in movies:
    #     movie.save()
    return render(requets, 'movies_app/all_movies.html', {
        'movies': movies,
        'agg': agg,
        'total': movies.count()

    })


# def show_one_movie(requets, id_movie:int):
def show_one_movie(requets, slug_movie: str):
    # movie = Movie.objects.get(id=id_movie)
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(requets, 'movies_app/one_movies.html', {
        'movie': movie
    })


#


# def director_movie(requets, slug_director: str):
#     director = get_object_or_404(Director, slug=slug_director)
#     return render(requets, 'movies_app/one_directors', {
#         'director': director
#     } )

    # # movie = Movie.objects.get(id=id_movie)
    # movie = get_object_or_404(Movie, slug=slug_movie)
    # return render(request, 'movie_app/one_movie.html', {
    #     'movie': movie,
    # })
