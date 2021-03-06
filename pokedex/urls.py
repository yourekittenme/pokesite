from django.urls import path
from . import views


urlpatterns = [
    path('', views.pokemon_list, name='pokemon_list'),
    path('pokemon_add', views.pokemon_add, name='pokemon_add'),
    path('pokemon/<int:pk>/detail', views.PokemonDetail.as_view(), name='pokemon_detail'),
]


