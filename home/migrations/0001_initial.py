# Generated by Django 3.2 on 2024-06-16 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('services_sold', models.PositiveIntegerField(default=0, verbose_name='Số dịch vụ đã bán')),
                ('customers_served', models.PositiveIntegerField(default=0, verbose_name='Số khách hàng đã sử dụng dịch vụ')),
                ('repeat_customers', models.PositiveIntegerField(default=0, verbose_name='Số khách hàng sử dụng lại dịch vụ')),
            ],
            options={
                'verbose_name': 'Service Statistic',
                'verbose_name_plural': 'Service Statistics',
            },
        ),
    ]
