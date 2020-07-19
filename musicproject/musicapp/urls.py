from django.urls import path

from . import views

urlpatterns = [
    path('musicapp/', views.index, name = "index"),
    path('input_song/', views.song_form, name = "song_form"),
    path('input_song/songs/', views.songs_display, name = "songs_display"),
]