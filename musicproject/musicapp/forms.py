from django import forms
from django.utils.safestring import mark_safe

from musicapp.models import Song
songs = Song.objects.all()

playlists = []
for asong in songs:
	if asong.playlist not in playlists:
		playlists.append(asong.playlist)

CHOICES = []
for aplaylist in playlists:
	CHOICES.append((aplaylist,aplaylist))

#like = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
class SongForm(forms.Form):
	name = forms.CharField(label=mark_safe('name'), max_length=100, required=False)
	singer = forms.CharField(label='singer', max_length=100)
	movie = forms.CharField(label='movie', max_length=100)
	genre = forms.CharField(label='genre', max_length=100)
	#playlist = forms.CharField(label='playlist', max_length=100, required = False)
	playlist = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)


class Edit1(forms.Form):
	name = forms.CharField(label=mark_safe('name'), max_length=100, required=False)
	singer = forms.CharField(label='singer', max_length=100)
	movie = forms.CharField(label='movie', max_length=100)
	genre = forms.CharField(label='genre', max_length=100)
	playlist = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)