"""
URL configuration for payments app.
"""

from django.urls import path

from apps.payments.views import placeholder_view

app_name = 'payments'

urlpatterns = [
    # Placeholder URL pattern
    path('', placeholder_view, name='payment-list'),
]