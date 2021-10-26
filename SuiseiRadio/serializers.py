from django.db import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework import serializers

from SuiseiRadio.models import Album, Artist

class ArtistSerializer(serializers.ModelSerializer):
    added_by = serializers.ReadOnlyField(source='added_by.username')

    class Meta:
        model = Artist
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        artist = Artist.objects.create(
            added_by=request.user, **validated_data
        )
        return artist

class AlbumSerializer(serializers.ModelSerializer):
    added_by = serializers.ReadOnlyField(source='added_by.username')

    class Meta:
        model = Album
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        artist = Album.objects.create(
            added_by=request.user, **validated_data
        )
        return artist
    
    def __str__(self):
        return self.name

