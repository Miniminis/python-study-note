from django.contrib import admin
from django.urls import path
from .import views 

urlpatterns = [
    path('/', views.home, name='home'),
    path('/', views.detail, name='detail'),
    path('/', views.about, name='about'),
]
