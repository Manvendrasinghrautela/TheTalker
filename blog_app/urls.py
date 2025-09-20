from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('search/', views.search_results, name='search_results'),
]
