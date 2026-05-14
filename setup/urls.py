from django.contrib import admin
from django.urls import path, include
from setup import settings
import django.conf.urls.static as static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')),
    path('', include('usuarios.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
