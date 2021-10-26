from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet

from SuiseiRadio.models import Album, Artist, Song

from SuiseiRadio.serializers import ArtistSerializer, AlbumSerializer, SongSerializer

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

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['action'] = self.action
        return context


class AlbumViewset(PermissionMixin, ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class SongViewset(PermissionMixin, ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer