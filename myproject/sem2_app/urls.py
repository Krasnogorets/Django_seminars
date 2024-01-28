from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('orel/', views.orel, name='orel'),
    path('dice/', views.dice, name='dice'),
    path('rnd/', views.rnd_, name='rnd'),
]
