from django.contrib import admin

from SuiseiRadio.models import Album, Artist, Like, Rating,Review, \
    Song

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Review)
admin.site.register(Rating)
admin.site.register(Like)
