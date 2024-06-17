from django.shortcuts import render
from django.shortcuts import render
from product.models import Product
from .models import ServiceStatistics

def index(request):
    products = Product.objects.all()  # Lấy tất cả sản phẩm từ database
    stats = ServiceStatistics.objects.first()
    context = {
        'products': products,
        'services_sold': stats.services_sold if stats else 0,
        'customers_served': stats.customers_served if stats else 0,
        'repeat_customers': stats.repeat_customers if stats else 0,
    }
    return render(request, 'home/index.html', context)
def qr_pay(request):
    return render(request, 'home/qr_pay_instructions.html')
def statistics_view(request):
    stats = ServiceStatistics.objects.first()
    context = {
        'services_sold': stats.services_sold if stats else 0,
        'customers_served': stats.customers_served if stats else 0,
        'repeat_customers': stats.repeat_customers if stats else 0,
    }
    return render(request, 'home/index.html', context)