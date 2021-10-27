from rest_framework import serializers
from rest_framework import serializers

from SuiseiRadio.models import Album, Artist, Rating, Review, Song

class ArtistSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Artist
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        artist = Artist.objects.create(
            author=request.user, **validated_data
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
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Album
        fields = ('id','author', 'title', 'about', 'album_cover')

    def create(self, validated_data):
        request = self.context.get('request')
        album = Album.objects.create(
            author=request.user, **validated_data
        )
        return album
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['songs'] = SongSerializer(
            instance.songs.all(), many=True
        ).data
        representation['reviews'] = ReviewSerializer(
            instance.reviews.all(), many=True
        ).data
        total_rate = 0
        representation['ratings'] = RatingSerializer(
            instance.ratings.all(), many=True
        ).data
        for rate in instance.ratings.all():
            total_rate += int(rate.rating)
            representation['ratings'] = total_rate / instance.ratings.all().count()
        return representation


class SongSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Song
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        song = Song.objects.create(
            author=request.user, **validated_data
        )
        return song
    
    def __str__(self):
        return super().__str__()


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Review
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        review = Review.objects.create(
            author=request.user, **validated_data
        )
        return review


class RatingSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Rating
        fields = '__all__'
        

    def create(self, validated_data):
        request = self.context.get('request')
        rating = Rating.objects.create(
            author=request.user, **validated_data
        )
        return rating
