"""
URL configuration for maintenance app.
"""

from django.urls import path

from apps.maintenance.views import placeholder_view

app_name = 'maintenance'

urlpatterns = [
    # Placeholder URL pattern
    path('', placeholder_view, name='maintenance-list'),
]