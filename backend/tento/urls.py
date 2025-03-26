"""
URL configuration for tento project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# Schema view for API documentation
schema_view = get_schema_view(
    openapi.Info(
        title="Tento API",
        default_version='v1',
        description="API for Tento housing platform",
        terms_of_service="https://www.tento.com/terms/",
        contact=openapi.Contact(email="contact@tento.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# API URL patterns
api_urlpatterns = [
    # Include app-specific URLs
    path('users/', include('apps.users.urls')),
    path('properties/', include('apps.properties.urls')),
    path('leases/', include('apps.leases.urls')),
    path('payments/', include('apps.payments.urls')),
    path('maintenance/', include('apps.maintenance.urls')),
    path('communications/', include('apps.communications.urls')),
    path('core/', include('apps.core.urls')),

    # Authentication URLs
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
]

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),

    # API URLs
    path('api/v1/', include(api_urlpatterns)),

    # API documentation
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]

# Serve static and media files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
