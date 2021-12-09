from django.urls import path
from Appcoder import views

urlpatterns = [
    path ('inicio', views.inicio),
    path ('jugadores', views.jugadores),
]
