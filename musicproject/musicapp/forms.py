from django import forms
from django.utils.safestring import mark_safe

class SongForm(forms.Form):
	name = forms.CharField(label=mark_safe('name'), max_length=100, required=False)
	singer = forms.CharField(label='singer', max_length=100)
	movie = forms.CharField(label='movie', max_length=100)
	genre = forms.CharField(label='genre', max_length=100)