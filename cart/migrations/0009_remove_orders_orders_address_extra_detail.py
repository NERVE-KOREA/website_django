# Generated by Django 4.2.4 on 2023-10-11 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_alter_orders_reciever_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='orders_address_extra_detail',
        ),
    ]