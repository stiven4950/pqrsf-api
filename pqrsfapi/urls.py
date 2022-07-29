from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from core.urls import core_patterns

urlpatterns = [
    path("api/v1/", include(core_patterns)),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
