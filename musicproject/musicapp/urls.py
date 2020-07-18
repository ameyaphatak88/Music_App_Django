from django.urls import path

from . import views

urlpatterns = [
    path('musicapp/', views.index, name = "index"),
    path('input_song/', views.song_form, name = "song_form"),
]