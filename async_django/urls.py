from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import home_view, main_view, main_view_async

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="home-view"),
    path('sync/', main_view, name="sync-main-view"),
    path('async/', main_view_async, name="async-main-view"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
