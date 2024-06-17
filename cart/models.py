from django.db import models
from product.models import Service,Product  # Import model Service từ ứng dụng product
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model
User = get_user_model()
class Order(models.Model):
    user_name = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    link = models.URLField()
    confirmed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order for {self.user_name} - {self.service.name_service}"

    @property
    def coin_required(self):
        return self.service.coin
