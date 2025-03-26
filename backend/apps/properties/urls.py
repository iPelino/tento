"""
URL configuration for properties app.
"""

from django.urls import path

from apps.properties.views import placeholder_view

app_name = 'properties'

urlpatterns = [
    # Placeholder URL pattern
    path('', placeholder_view, name='property-list'),
]