# Generated by Django 4.2.4 on 2023-08-29 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_id', models.CharField(max_length=40, primary_key=True, serialize=False, unique=True, verbose_name='사용자 계정')),
                ('password', models.CharField(max_length=128, verbose_name='비밀번호')),
                ('user_name', models.CharField(max_length=10, verbose_name='사용자 이름')),
                ('phone_number', models.CharField(max_length=11, unique=True, verbose_name='전화번호')),
                ('gender', models.CharField(max_length=10, verbose_name='성별')),
                ('email', models.CharField(max_length=40, unique=True, verbose_name='이메일')),
                ('email_notification_acceptance', models.BooleanField(default=False, verbose_name='이메일 수신여부')),
                ('birthdate', models.DateTimeField(verbose_name='생년월일')),
                ('sign_up_path', models.CharField(max_length=100, verbose_name='가입경로')),
                ('sign_up_date', models.DateTimeField(auto_now_add=True, verbose_name='가입시기')),
                ('user_update_date', models.DateTimeField(verbose_name='프로필 업데이트 시기')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
