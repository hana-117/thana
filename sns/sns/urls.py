from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path

from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('microposts/', include('microposts.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)