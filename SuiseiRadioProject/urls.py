from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from SuiseiRadio.views import AlbumViewset, ArtistViewset

router = DefaultRouter()
router.register('artists', ArtistViewset)
router.register('albums', AlbumViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('music/', include(router.urls)),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
