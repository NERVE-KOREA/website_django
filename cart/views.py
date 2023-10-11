from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.models import Cart
from django.shortcuts import get_object_or_404

# Create your views here.
@login_required
def cart_view(request):
    user = request.user
    user_id = user.user_id
    try:
        cart = Cart.objects.get(user_id = user_id)
        redpill_quantity = cart.redpill_quantity
        bluepill_quantity = cart.bluepill_quantity
    except Cart.DoesNotExist:
        new_cart = Cart.objects.create(user_id = user_id, redpill_quantity = 0, bluepill_quantity = 0)
        new_cart.save()
        cart = Cart.objects.get(user_id = user_id)
        redpill_quantity = cart.redpill_quantity
        bluepill_quantity = cart.bluepill_quantity
    if request.method == 'POST':
        redpill_quantity = request.POST.get('redpill_quantity')
        bluepill_quantity = request.POST.get('bluepill_quantity')
        cart = Cart.objects.get(user_id = user_id)
        cart.redpill_quantity = redpill_quantity
        cart.bluepill_quantity = bluepill_quantity
        cart.save()
        return redirect('order')
    return render(request, "cart.html",{'redpill_quantity': redpill_quantity, 'bluepill_quantity': bluepill_quantity})

@login_required
def order_view(request):
    user = request.user
    user_id = user.user_id
    cart = Cart.objects.get(user_id = user_id)
    redpill_quantity = cart.redpill_quantity
    bluepill_quantity = cart.bluepill_quantity
    return render(request, "order.html", {'redpill_quantity': redpill_quantity, 'bluepill_quantity': bluepill_quantity})



    # 나머지 품목 추가 로직 작성
    # 장바구니 페이지로 리다이렉션
        

# def add_cart(request,product_id):
#     product = Product.objects.get(id=product_id)
#     cart_item = Orders_Detail.objects.get()





# @login_required
# def product_add_and_payment(request):