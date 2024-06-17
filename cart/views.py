from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Order, Service
from product.models import Product  # Đảm bảo import đúng model Product

@login_required
def choose_product_service(request):
    products = Product.objects.all()
    services = Service.objects.all()
    context = {
        'products': products,
        'services': services,
    }
    return render(request, 'cart/choose_product_service.html', context)

@login_required
def create_order(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        service_id = request.POST.get('service_id')
        link = request.POST.get('link', '')

        product = get_object_or_404(Product, pk=product_id)
        service = get_object_or_404(Service, pk=service_id)

        user = request.user

        if user.coin >= service.coin:
            user.coin -= service.coin
            user.save()

            order = Order.objects.create(
                user_name=user.username,
                product=product,
                service=service,
                link=link
            )

            messages.success(request, 'Đã thanh toán và lưu đơn hàng thành công!')
            return redirect('cart:order_detail', order_id=order.id)
        else:
            messages.error(request, 'Số coin của bạn không đủ để thanh toán dịch vụ này.')

    return redirect('cart:choose_product_service')

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    context = {
        'order': order,
    }
    return render(request, 'cart/order_detail.html', context)

