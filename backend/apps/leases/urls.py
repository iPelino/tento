"""
URL configuration for leases app.
"""

from django.urls import path

from apps.leases.views import placeholder_view

app_name = 'leases'

urlpatterns = [
    # Placeholder URL pattern
    path('', placeholder_view, name='lease-list'),
]