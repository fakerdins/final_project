from django.db import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework import serializers

from SuiseiRadio.models import Album, Artist, Song

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

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['albums'] = AlbumSerializer(
            instance.albums.all(), many=True
        ).data
        action = self.context.get('action')
        if action=='retrieve':
            representation['albums'] = AlbumSerializer(
                instance.albums.all(), many=True
            ).data
        elif action=='list':
            representation['albums'] = instance.albums.count()
        return representation

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

class SongSerializer(serializers.ModelSerializer):
    added_by = serializers.ReadOnlyField(source='added_by.username')

    class Meta:
        model = Song
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        artist = Song.objects.create(
            added_by=request.user, **validated_data
        )
        return artist

    
