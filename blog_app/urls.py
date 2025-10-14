from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('article/<slug:slug>/', views.post_detail, name='article_detail'),
    path('category/<int:category_id>/', views.category_posts, name='category_posts'),
    path('search/', views.search_results, name='search_results'),
]
