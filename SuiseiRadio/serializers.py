from rest_framework import serializers
from rest_framework import serializers

from SuiseiRadio.models import Artist

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