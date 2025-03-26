"""
URL configuration for core app.
"""

from django.urls import path

from apps.core.views import health_check

app_name = 'core'

urlpatterns = [
    # Health check endpoint
    path('health/', health_check, name='health-check'),
]