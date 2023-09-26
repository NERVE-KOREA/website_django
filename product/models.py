from django.db import models

class Product(models.Model):
    product_id = models.IntegerField("상품번호", max_length = 40, primary_key=True, unique=True)
    name = models.CharField("상품명", max_length= 50)
    price = models.IntegerField("상품가격", max_length= 11)
    stock = models.IntegerField("재고", max_length= 11)
    cumulative_stock_volume = models.IntegerField("누적 판매량", max_length= 11)
    views_count = models.IntegerField("상품 조회수", max_length = 11)
    product_register_date = models.DateField(auto_now_add=True)
    product_update_date = models.DateTimeField(auto_now=True)

# Create your models here.
