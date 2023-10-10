from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.models import Cart
from django.shortcuts import get_object_or_404

# Create your views here.
@login_required
def cart_view(request):
    user = request.user
    return render(request, "cart.html")

@login_required
def order_view(request):
    user = request.user
    return render(request, "order.html")

@login_required
def product_add_to_cart_redpill(request):
    user = request.user
    user_id = user.user_id
    try:
        cart = Cart.objects.get(user_id=user_id)
        # 카트가 이미 있는 경우, 품목 개수를 +1 업데이트
        Cart.redpill_quantity += 1
        cart.save()
    except Cart.DoesNotExist:
        # 카트가 없는 경우, 새로운 카트 생성 후 품목 추가
        cart = Cart.objects.create(user_id=user_id, redpill_quantity = user.repill_quantity)
    # 나머지 품목 추가 로직 작성
    return redirect('cart.html')  # 장바구니 페이지로 리다이렉션
        

# def add_cart(request,cart_id):
#     product =  Cart.objects.get(product_id=product_id(request))
#     cart_item = Cart_Detail.objects.get()





# @login_required
# def product_add_and_payment(request):