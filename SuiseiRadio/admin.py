from django.contrib import admin

from SuiseiRadio.models import Album, Artist, Song

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Song)