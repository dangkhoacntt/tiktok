from django.db import models
from django.utils import timezone

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name_product = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_product

class Service(models.Model):
    id = models.AutoField(primary_key=True)
    name_service = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='services')
    coin = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name_service} - {self.product.name_product}"
