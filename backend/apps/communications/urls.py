"""
URL configuration for communications app.
"""

from django.urls import path

from apps.communications.views import placeholder_view

app_name = 'communications'

urlpatterns = [
    # Placeholder URL pattern
    path('', placeholder_view, name='communication-list'),
]