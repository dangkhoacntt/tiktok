from django.urls import path
from . import views

app_name = 'cart'


urlpatterns = [
    # path('choose_product/', views.choose_product, name='choose_product'),
    # path('choose_product_service/', views.choose_product_service_html, name='choose_product_service_html'),
    path('create_order/', views.create_order, name='create_order'),
    path('choose_product_service/', views.choose_product_service, name='choose_product_service'),
    path('order_detail/<int:order_id>/', views.order_detail, name='order_detail'),
    # Bạn có thể thêm các URL khác nếu cần
]
