from django.db import models
from movielist.models import Movie


class Cinema(models.Model):
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    movies = models.ManyToManyField(Movie, through='Screening')

    def __str__(self):
        return self.name


class Screening(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date = models.DateTimeField()
