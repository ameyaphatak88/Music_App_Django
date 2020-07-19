from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import SongForm
from django.http import HttpResponseRedirect
from .models import Song
from django.urls import reverse
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
			c =Song(name = name, singer = singer, movie = movie, genre = genre)
			c.save()
			return HttpResponseRedirect('songs/')
	else:
		form = SongForm()
	return render(request, 'musicapp/songform.html', {'form': form})


def songs_display(request):
	from musicapp.models import Song
	songs = Song.objects.all()

	context = {
		"songs" : songs
	}

	template = loader.get_template('musicapp/songs_display.html')
	return HttpResponse(template.render(context, request))


