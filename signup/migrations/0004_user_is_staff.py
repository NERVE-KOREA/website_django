# Generated by Django 4.2.4 on 2023-08-29 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0003_user_is_active_user_is_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
