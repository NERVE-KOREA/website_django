from django.db import models

# Create your models here.
class Cart(models.Model):
    cart_id = models.IntegerField("장바구니 번호",primary_key = True, unique= True, auto_created=True)
    user_id = models.CharField("사용자 계정", max_length= 40, unique=True)
    redpill_quantity = models.IntegerField("레드필 수량")
    blupill_quantity = models.IntegerField("블루필 수량")
    cart_register_date = models.DateTimeField("장바구니 생성일자", auto_now_add=True)
    cart_update_date = models.DateTimeField("장바구니 업데이트일자", auto_now= True)

from django.db import models

# Create your models here.

class Orders(models.Model):
    orders_id = models.CharField("주문번호", max_length=10, primary_key= True, auto_created=True)
    user_id = models.CharField("유저ID", max_length=40)
    orders_date = models.DateTimeField("주문일자", auto_now_add=True)
    orders_status = models.CharField("주문처리상태", max_length=20)
    orders_zipcode = models.CharField("주소(우편번호)", max_length=5)
    orders_address = models.CharField("주소(주소)", max_length=50)
    orders_address_detail = models.CharField("주소(상세주소)", max_length=50)
    reciever = models.CharField("수령자 이름", max_length=10)
    reciever_phone_number = models.CharField("수령자 전화번호", max_length=11)
    reciever_demand = models.CharField("배송시 요청사항", max_length=50)
    orders_update_date = models.DateTimeField("주문 수정일자", auto_now= True)
    payment_demand = models.CharField("결제방식", max_length=40)

class Orders_Deatil(models.Model):
    orders_detail_id = models.CharField("주문상세번호", max_length=10)
    orders_id = models.CharField("주문번호", max_length=10)
    product_id = models.CharField("제품번호", max_length=10)
    product_name = models.CharField("제품명", max_length=20)
    quantity = models.IntegerField("수량")
    total_price = models.IntegerField("총 가격")
    orders_detail_status = models.CharField("배송처리상태", max_length=15)
    refunable_status = models.BooleanField("환불가능여부", default= False) ## 상황별 개발 필요

