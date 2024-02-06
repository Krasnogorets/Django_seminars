from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('orel/<int:num>/', views.orel, name='orel'),
    path('dice/<int:num>/', views.dice, name='dice'),
    path('rnd/<int:num>/', views.rnd_, name='rnd'),
]
