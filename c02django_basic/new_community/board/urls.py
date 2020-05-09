from django.urls import path
from . import views

urlpatterns = [
    path('', views.board),
    path('write/', views.write),
    path('detail/<int:pk>/', views.detail),
]
