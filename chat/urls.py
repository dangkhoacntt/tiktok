# chat/urls.py

from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.chat_home, name='chat_home'),
    path('admin/send/', views.admin_send_message, name='admin_send_message'),
    path('admin/chat/', views.admin_chat, name='admin_chat'),
]
