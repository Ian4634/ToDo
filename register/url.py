from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('register/create_user/', views.create_user, name='create_user'),
    path('login/verify', views.verify_user, name='verify_user')

]
