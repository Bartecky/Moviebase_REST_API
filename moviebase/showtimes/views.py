from showtimes.models import Cinema, Screening
from showtimes.serializers import CinemaSerializer, ScreeningSerializer, Next30dayScreeningSerializer
from rest_framework import generics
# from django_filters.rest_framework import DjangoFilterBackend

class CinemaListView(generics.ListCreateAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer


class CinemaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer


class ScreeningListView(generics.ListCreateAPIView):
    queryset = Screening.objects.all()
    serializer_class = ScreeningSerializer
    # filter_backends = (DjangoFilterBackend,)
    # filter_fields = ('cinema__name', 'movie__title')


class ScreeningView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Screening.objects.all()
    serializer_class = ScreeningSerializer


class Next30DaysScreeningsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cinema.objects.all()
    serializer_class = Next30dayScreeningSerializer