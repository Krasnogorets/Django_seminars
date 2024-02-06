from django.urls import path
from . import views

urlpatterns = [
    path('<int:author_id>/', views.author_posts, name='author_posts'),
    path('article/<int:article_id>/', views.post_full, name='post_full')

]
