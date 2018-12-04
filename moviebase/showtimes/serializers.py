from rest_framework import serializers
from showtimes.models import Cinema
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