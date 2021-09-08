from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addgoal/', views.addgoal, name='addgoal'),
    path('delete/', views.delete, name = 'delete'),
    path('addgoal/creategoal/', views.creategoal, name='creategoal'),
    path('testing/', views.testing)
]
