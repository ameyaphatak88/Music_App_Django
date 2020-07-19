from django import forms

gen = [('pop', 'pop'),
	    ('rock', 'rock'),
		('jazz', 'jazz'),
		('romantic', 'romantic'),
		('kids', 'kids'),
		('classical', 'classical')]


class SongForm(forms.Form):
	name = forms.CharField(label='name', max_length=100, required=False)
	singer = forms.CharField(label='singer', max_length=100)
	movie = forms.CharField(label='movie', max_length=100)
	genre = forms.CharField(label='genre', max_length=100)