from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_view'),
    path('search/',views.search_view, name='search_view'),
    path('article/display/', views.get_article, name='get_article'),
]