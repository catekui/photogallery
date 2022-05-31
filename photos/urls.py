from django.urls import path 
from . import views
# from importlib.resources import path, include


urlpatterns = [
    # url(r'^$', views.gallery, name='gallery'),
    path('', views.gallery, name='gallery'),
    path('index/', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    path('add/', views.addPhoto, name='add')

]