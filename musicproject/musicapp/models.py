from django.db import models
from django import forms

class Song(models.Model):
	name = models.CharField(max_length = 20)
	singer = models.CharField(max_length = 20)
	movie = models.CharField(max_length = 20)
	genre = models.CharField(max_length = 20)
	
