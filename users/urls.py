from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.custom_user_login, name='user_login'),
    path('register/', views.custom_user_register, name='user_register'),
    path('logout/', views.custom_user_logout, name='user_logout'),
]
