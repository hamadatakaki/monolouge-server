from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from monologue_api import urls as api_urls
from accounts import urls as account_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls.router.urls)),
    path('api/', include(account_urls.router.urls)),
    path('api/', include(account_urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/rest-auth/', include('rest_auth.urls')),
    path('api/rest-auth/registration/', include('rest_auth.registration.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
