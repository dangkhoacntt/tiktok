from django.urls import path
from . import views
from .views import qr_pay

urlpatterns = [
    path('', views.index, name='index'),  # Đường dẫn đến trang index
    path('coin/', qr_pay, name='qrpay'), 
  
]