from django.urls import path

from . import views

urlpatterns = [
    path('musicapp/', views.index, name = "index"),
    path('input_song/', views.song_form, name = "song_form"),
    path('input_song/songs/', views.songs_display, name = "songs_display"),
    path('playlists_display/', views.playlists_display, name = "playlists_display"),
    path('playlist_edit/<str:song_name>/', views.edit_song),
    path('playlist_edit/<str:song_name>/songs/', views.songs_display),
    path('api/songs/', views.get_songs),
    path('querry_post/<str:song_name>/<str:song_singer>/<str:song_movie>/<str:song_genre>/<str:song_playlist>', views.query_post)
]