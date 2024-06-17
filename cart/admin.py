# cart/admin.py
from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'product', 'service', 'link', 'confirmed', 'created_at', 'updated_at')
    list_filter = ('confirmed', 'created_at', 'updated_at')
    search_fields = ('user_name', 'product__name_product', 'service__name_service')