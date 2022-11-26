from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backend.bills.urls')),
    path('api/', include('backend.accounts.urls')),
    path('api/get-token', TokenObtainPairView.as_view(), name='get_token'),
    path('api/refresh-token', TokenRefreshView.as_view(), name='refresh_token'),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
