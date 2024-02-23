from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:author_id>/', views.author_posts, name='author_posts'),
    path('article/<int:article_id>/', views.post_full, name='post_full'),
    path('author/', views.author_input, name='author_input'),
    path('author1/', views.author_input_1, name='author_input_1'),
    path('add/', views.article_input, name='article_input'),

]
