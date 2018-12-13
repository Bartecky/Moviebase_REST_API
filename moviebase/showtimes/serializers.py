from rest_framework import serializers
from showtimes.models import Cinema, Screening
from movielist.models import Movie
from datetime import datetime, timedelta


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


class Next30dayScreeningSerializer(serializers.ModelSerializer):
    movies = serializers.SerializerMethodField()

    class Meta:
        model = Cinema
        fields = '__all__'

    def get_movies(self, obj):
        today = datetime.now()
        month_later = today + timedelta(30)
        return [movie.title for movie in obj.movies.filter(screening__date__gte=today,
                                                           screening__date__lt=month_later)]
