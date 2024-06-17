from django.db import models

class ServiceStatistics(models.Model):
    services_sold = models.PositiveIntegerField(default=0, verbose_name="Số dịch vụ đã bán")
    customers_served = models.PositiveIntegerField(default=0, verbose_name="Số khách hàng đã sử dụng dịch vụ")
    repeat_customers = models.PositiveIntegerField(default=0, verbose_name="Số khách hàng sử dụng lại dịch vụ")

    class Meta:
        verbose_name = "Service Statistic"
        verbose_name_plural = "Service Statistics"

    def __str__(self):
        return "Service Statistics"