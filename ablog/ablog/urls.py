
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import urls
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('theblog.urls')),
    #accesses premade views from djangoo for login and logout
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
