from django.contrib import admin, messages
from django.db.models import QuerySet

from .models import Movie, Director,Actor, DressingRoom


# Register your models here.

admin.site.register(Director)
admin.site.register(Actor)
# admin.site.register(DressingRoom)

# создаём новую админку, дя этого коментирем admin.site.register(DressingRoom)
@admin.register(DressingRoom)
class DressingRoom(admin.ModelAdmin):
    list_display = ['floor', 'number', 'actor']



# class MovieAdmin(admin.ModelAdmin):
#     list_display = ['name', 'rating', 'year', 'budget']
#
#
# admin.site.register(Movie, MovieAdmin)

# Можно использовать декоратор
class RatingFilter(admin.SimpleListFilter):
    title = 'Фильтр по рейтингу'
    parameter_name = 'rating'
    def lookups(self, request, model_admin):
        return [
            ('<40', 'Низкий'),
            ('от 40 до 59', 'Средний'),
            ('от 60 до 79', 'Высокий'),
            ('>=80', 'Высочайший'),
        ]
    def queryset(self, request, queryset: QuerySet):
        if self.value()=='<40':
            return queryset.filter(rating__lt=40)
        if self.value()=='от 40 до 59':
            return queryset.filter(rating__gte=40).filter(rating__lt=60)
        if self.value()=='от 60 до 79':
            return queryset.filter(rating__gte=60).filter(rating__lt=79)
        if self.value() == '>=80':
            return queryset.filter(rating__gte=80)
        return queryset

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ['rating', 'name']- оставляет поля
    # list_editable- изменяет поля. # ordering - сортирует список
    # list_per_page- видеть сколько будет значений на странице
    # exclude = ['year'] - скрывает поля; readonly_fields =['']-заморивает поле.
    # exclude = ['slug'],  prepopulated_fields = -предвычисляемые значения.
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'rating', 'director', 'budget', 'rating_status']
    list_editable = ['rating', 'director', 'budget']
    filter_horizontal = ['actors']
    ordering = ['-rating', '-name']
    list_per_page = 8
    actions = ['set_dollars', 'set_euro', 'set_rubles']
    search_fields = ['name__startswith', 'rating']
    list_filter = ['name', 'currency', RatingFilter]

    # Пишем патерн, для того что бы сортировать поле, в ordring=пишем, то что
    # что хотим сортировать. если хотим изенить поле rating_status, то
    # пишем, description= 'Статус'

    @admin.display(ordering='rating', description='Статус')
    def rating_status(self, mov: Movie):
        if mov.rating < 50:
            return 'Не стоит смотреть'
        if mov.rating < 70:
            return 'Раз посмотреть можно'
        if mov.rating <= 85:
            return 'Хороший фильм'
        return 'Огонь'
# Данный патер позволяет создать действие новое в админке.

    @admin.action(description='Установить валюту доллар')
    def set_dollars(self, requests, qs: QuerySet):
        qs.update(currency=Movie.USD)

    @admin.action(description='Установить валюту евро')
    def set_euro(self, requests, qs: QuerySet):
        count_update = qs.update(currency=Movie.EUR)
        self.message_user(
            requests,
            f'Было обновлено {count_update} записей',
            messages.ERROR
        )

    @admin.action(description='Установить валюту рубли')
    def set_rubles(self, requests, qs: QuerySet):
        count_update = qs.update(currency=Movie.RUB)
        self.message_user(
            requests,
            f'Было обновлено {count_update} записей',
        )