from rest_framework import serializers
from showtimes.models import Cinema, Screening
from movielist.models import Movie


class CinemaSerializer(serializers.ModelSerializer):
    movies = serializers.HyperlinkedRelatedField(
        many=True,
        allow_null=True,
        view_name='movie-detail',
        queryset=Movie.objects.all(),
    )

    class Meta:
        model = Cinema
        fields = '__all__'


class ScreeningSerializer(serializers.ModelSerializer):
    cinema = serializers.SlugRelatedField(slug_field='name', queryset=Cinema.objects.all())
    movie = serializers.SlugRelatedField(slug_field='title', queryset=Movie.objects.all())

    class Meta:
        model = Screening
        fields = '__all__'
