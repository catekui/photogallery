from django.urls import path
from . import views


urlpatterns = [
   
    path('', views.gallery),
    path('index/', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    path('add/', views.addPhoto, name='add')

]