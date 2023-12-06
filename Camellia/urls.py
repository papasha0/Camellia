"""
Definition of urls for Camellia.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='app/encryption.html'), name='home'),
    path('encryption/', TemplateView.as_view(template_name='app/encryption.html'), name='encryption'),
    path('encrypt_photo/', views.encrypt_photo, name='encrypt_photo')
]

