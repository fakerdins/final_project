from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from SuiseiRadio.views import AlbumViewset, ArtistViewset, LikeViewset, ReviewViewset,\
    SongViewset, RatingViewset

router = DefaultRouter()
router.register('artists', ArtistViewset)
router.register('albums', AlbumViewset)
router.register('songs', SongViewset)
router.register('reviews', ReviewViewset)
router.register('ratings', RatingViewset)
router.register('likes', LikeViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('music/', include(router.urls)),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
