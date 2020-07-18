from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Song
from .forms import SongForm
from django.views import generic

def index(request):
    return HttpResponse("Hi")


def song_form(request):
	from musicapp.models import Song
	songs = Song.objects.all()
	if request.method == 'POST':
		form = SongForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			singer = form.cleaned_data['singer']
			movie = form.cleaned_data['movie']
			genre = form.cleaned_data['genre']
			print(name)
			print(singer)
			print(movie)
			print(genre)
	return render(request, 'musicapp/songform.html', {'form': form})

