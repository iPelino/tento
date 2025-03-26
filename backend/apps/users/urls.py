"""
URL configuration for users app.
"""

from django.urls import path

from apps.users.views import placeholder_view

app_name = 'users'

urlpatterns = [
    # Placeholder URL pattern
    path('', placeholder_view, name='user-list'),
]