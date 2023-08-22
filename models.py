# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cart(models.Model):
    cart_id = models.PositiveIntegerField(primary_key=True)
    member_id = models.PositiveIntegerField()
    redpill_quantity = models.PositiveIntegerField()
    bluepill_quantity = models.PositiveIntegerField()
    total_price = models.PositiveIntegerField()
    cart_register_date = models.DateTimeField()
    cart_update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cart'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Inquiry(models.Model):
    inquiry_id = models.PositiveIntegerField(primary_key=True)
    member_id = models.PositiveIntegerField()
    category = models.CharField(max_length=40)
    inquiry_status = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    detail = models.CharField(max_length=300)
    image_path = models.CharField(max_length=1000, blank=True, null=True)
    inquiry_register_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'inquiry'


class InquiryAnswer(models.Model):
    inquiry_answer_id = models.PositiveIntegerField(primary_key=True)
    inquiry_id = models.PositiveIntegerField()
    member_id = models.PositiveIntegerField()
    inquiry_register_date = models.DateTimeField()
    answer_title = models.CharField(max_length=50)
    answer_detail = models.CharField(max_length=1000)
    answer_register_date = models.DateTimeField()
    answer_update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'inquiry_answer'


class Member(models.Model):
    member_id = models.PositiveIntegerField(primary_key=True)
    password = models.PositiveIntegerField()
    member_name = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=11)
    gender = models.PositiveIntegerField()
    email = models.CharField(max_length=40)
    email_notification_acceptance = models.PositiveIntegerField()
    birthdate = models.DateTimeField()
    sign_up_path = models.CharField(max_length=100)
    sign_up_date = models.DateTimeField()
    member_update_date = models.DateTimeField()
    last_login_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'member'


class OrderDetail(models.Model):
    order_detail_id = models.PositiveIntegerField(primary_key=True)
    orders_id = models.PositiveIntegerField()
    product_id = models.PositiveIntegerField()
    product_name = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    total_price = models.PositiveIntegerField()
    order_detail_status = models.CharField(max_length=10)
    refundable_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'order_detail'


class Orders(models.Model):
    orders_id = models.PositiveIntegerField(primary_key=True)
    member_id = models.PositiveIntegerField()
    orders_date = models.DateTimeField()
    orders_status = models.CharField(max_length=10)
    orders_zipcode = models.PositiveIntegerField()
    orders_address = models.CharField(max_length=30)
    orders_address_detail = models.CharField(max_length=100)
    receiver = models.CharField(max_length=10)
    receiver_phone_number = models.CharField(max_length=11)
    receiver_demand = models.CharField(max_length=60)
    orders_update_date = models.DateTimeField()
    payment_method = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'orders'


class Product(models.Model):
    product_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    stock = models.IntegerField()
    cumulative_sales_volume = models.IntegerField()
    views_count = models.IntegerField()
    product_register_date = models.DateTimeField()
    product_modification_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'product'


class ShippingAddress(models.Model):
    shipping_address_id = models.PositiveIntegerField(primary_key=True)
    member_id = models.PositiveIntegerField()
    zipcode = models.PositiveIntegerField()
    address = models.CharField(max_length=30)
    address_detail = models.CharField(max_length=100)
    shipping_request = models.CharField(max_length=60)
    receiver = models.CharField(max_length=10)
    receiver_phone_number = models.CharField(max_length=11)
    receiver_demand = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shipping_address'