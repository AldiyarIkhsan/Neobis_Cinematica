from movies.serializers import MoviesSerializer
from rest_framework.viewsets import ModelViewSet
from movies.models import Movies


class MoviesViewSet(ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer
