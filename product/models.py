from django.db import models

class Product(models.Model):
    product_id = models.IntegerField("상품번호", primary_key=True, unique=True)
    name = models.CharField("상품명", max_length= 50)
    price = models.IntegerField("상품가격")
    stock = models.IntegerField("재고")
    cumulative_stock_volume = models.IntegerField("누적 판매량")
    views_count = models.IntegerField("상품 조회수")
    product_register_date = models.DateTimeField("상품 등록 일자",auto_now_add=True)
    product_update_date = models.DateTimeField("상품 업데이트 일자",auto_now=True)

# Create your models here.
