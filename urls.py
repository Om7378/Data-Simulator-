"""
URL configuration for datasimulator project.
The `urlpatterns` list routes URLs to views.
"""
from django.contrib import admin
from django.urls import include, path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('temperature/', include('temperature.urls')),

    path('datasimulator/', lambda request: render(
        request,
        'datasimulator.html'
    ), name='datasimulator'),

    path('datasimulator/settings/', lambda request: render(
        request, 'settings.html'
        ), name='settings'),

    path('datasimulator/vibration/', include('vibration.urls')),

path('datasimulator/settings/postgresql/', views.postgresql_settings, name='postgresql_settings'),
]