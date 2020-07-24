import json
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import SongForm, Edit1
from django.http import HttpResponseRedirect
from .models import Song, Edit
from django.urls import reverse
from django.views import generic
import numpy as np
from django.views.decorators.csrf import csrf_exempt



def index(request):
    return HttpResponse("Hi")


def song_form(request):
	from musicapp.models import Song
	songs = Song.objects.all()
	if request.method == 'POST':
		print("in if")
		form = SongForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			singer = form.cleaned_data['singer']
			movie = form.cleaned_data['movie']
			genre = form.cleaned_data['genre']
			playlist = form.cleaned_data['playlist']
			c =Song(name = name, singer = singer, movie = movie, genre = genre, playlist = playlist)
			c.save()
			return HttpResponseRedirect('songs/')
	else:
		print("in else")
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

def playlists_display(request):
	from musicapp.models import Song
	songs = Song.objects.all()
	for asong in songs:
		if asong.playlist not in playlists:
			playlists.append(asong.playlist)
	playlist_dict = {}
	for aplaylist in playlists:
		playlist_dict[aplaylist] = []
	for asong in songs:
		if asong.playlist in playlist_dict:
			playlist_dict[asong.playlist].append(asong.name)
    
	print(playlist_dict.keys())
	context = {
		"playlist_dict" : playlist_dict
	}

	print("------------printing playlist------------------------------------------")
	print(context["playlist_dict"])
	print("------------------------------------------------------")
	template = loader.get_template('musicapp/playlists_display.html')
	return HttpResponse(template.render(context, request))
				

def edit_song(request, song_name = "ameya"):
	flag = 0
	thatsong = 0
	from musicapp.models import Song
	songs = Song.objects.all()

	for asong in songs:
		if asong.name == song_name:
			flag = 1			
			thatsong = asong

	print(thatsong)
	if flag == 0:
		return HttpResponse("Invalid song eneterd")

	if request.method == 'POST':
		print("in if")
		form = Edit1(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			singer = form.cleaned_data['singer']
			movie = form.cleaned_data['movie']
			genre = form.cleaned_data['genre']
			playlist = form.cleaned_data['playlist']
			thatsong.name = name
			thatsong.singer = singer
			thatsong.movie = movie
			thatsong.genre = genre
			thatsong.playlist = playlist
			thatsong.save()
			return HttpResponseRedirect('songs/')
	else:
		print("else")
		form = Edit1()
	
	return render(request, 'musicapp/edit1.html', {'form': form})


def _extract_song_object_to_dict(song):
	songDict = {}
	songDict["name"] = song.name
	songDict["singer"] = song.singer
	songDict["movie"] = song.movie
	songDict["genre"] = song.genre
	songDict["playlist"] = song.playlist
	return songDict

@csrf_exempt 
def get_songs(request):
	#todo: interact with models to get list of songs
	from musicapp.models import Song
	
	if request.method == 'GET':
		songs = []
		for asong in Song.objects.all():
			songs.append(_extract_song_object_to_dict(asong))

		songs_json = json.dumps(songs)
		return HttpResponse(songs_json)
	else:
		
			#print('Name : "%s"' %request.body)

			#print('Name: "%s"' % request.body["name"])
			thatsong = json.loads(request.body)
			songs = Song.objects.all()
			print(thatsong["singer"])
			c = Song(name = thatsong["name"], singer = "viraj", movie = thatsong["movie"], genre = thatsong["genre"], playlist = thatsong["playlist"])
			c.save()
			return HttpResponse("OK")





