from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters

from rest_framework.viewsets import ModelViewSet

from SuiseiRadio.models import Album, Artist, Rating, Review, Song, Like

from SuiseiRadio.serializers import ArtistSerializer, AlbumSerializer, LikeSerializer, \
    RatingSerializer, ReviewSerializer, SongSerializer

from rest_framework.permissions import IsAuthenticated

from SuiseiRadio.permissions import IsAuthorPermission


class PermissionMixin:
    def get_permissions(self):
        if self.action == 'create':
            permissions = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permissions = [IsAuthorPermission]
        else:
            permissions = []
        return [permission() for permission in permissions]


class ArtistViewset(PermissionMixin, ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['about', 'artist']

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['action'] = self.action
        return context


class AlbumViewset(PermissionMixin, ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['artist']
    search_fields = ['title', 'about']


class SongViewset(PermissionMixin, ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class ReviewViewset(PermissionMixin, ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class LikeViewset(PermissionMixin, ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class RatingViewset(PermissionMixin, ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
