# Generated by Django 4.2.4 on 2023-10-11 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_orders_orders_address_extra_detail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='reciever',
            field=models.CharField(max_length=10, verbose_name='수령인'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='reciever_phone_number',
            field=models.CharField(max_length=11, verbose_name='수령인 전화번호'),
        ),
    ]
