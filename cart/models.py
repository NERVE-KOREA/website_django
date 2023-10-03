from django.db import models

# Create your models here.
class Cart(models.Model):
    cart_id = models.IntegerField("장바구니 번호",primary_key = True, unique= True)
    user_id = models.CharField("사용자 계정", max_length= 40, unique=True)
    redpill_quantity = models.IntegerField("레드필 수량")
    blupill_quantity = models.IntegerField("블루필 수량")
    cart_register_date = models.DateTimeField("장바구니 생성일자", auto_now_add=True)
    cart_update_date = models.DateTimeField("장바구니 업데이트일자", auto_now= True)
