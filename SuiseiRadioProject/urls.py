from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from SuiseiRadio.views import AlbumViewset, ArtistViewset, LikeViewset, ReviewViewset,\
    SongViewset, RatingViewset, AlbumFavouriteView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="SuiseiSpotify API",
      default_version='v1',
      description="Still still stellar...",
      terms_of_service="https://www.suisei.com/policies/terms/",
      contact=openapi.Contact(email="star@suisei.local"),
      license=openapi.License(name="Suicopath license"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)   

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
    path('music/favourites/', AlbumFavouriteView.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
