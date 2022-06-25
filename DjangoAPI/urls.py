from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
""" module that defines URLs """


urlpatterns = [
    path('api/admin/', admin.site.urls),
    path("api/", include('app.urls'))
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
