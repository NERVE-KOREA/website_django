from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.models import Cart, Orders
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
    if request.method == 'POST':
        user_id = user_id
        orders_status ='주문확인중'
        orders_zipcode = request.POST['orders_zipcode']
        orders_address = request.POST['orders_address']
        orders_address_detail = request.POST['orders_address_detail']
        reciever = request.POST['reciever']
        reciever_phone_number = request.POST['reciever_phone_number']
        reciever_demand = request.POST['reciever_demand']
        payment_demand = '카드'
        new_cart = Orders.objects.create(
            user_id = user_id,
            orders_status = orders_status,
            orders_zipcode = orders_zipcode,
            orders_address = orders_address,
            orders_address_detail = orders_address_detail,
            reciever = reciever,
            reciever_demand = reciever_demand,
            reciever_phone_number = reciever_phone_number,
            payment_demand = payment_demand
        )
        new_cart.save()
        return render(request, "index.html")  

    return render(request, "order.html", {'redpill_quantity': redpill_quantity, 'bluepill_quantity': bluepill_quantity})




    # 나머지 품목 추가 로직 작성
    # 장바구니 페이지로 리다이렉션
        

# def add_cart(request,product_id):
#     product = Product.objects.get(id=product_id)
#     cart_item = Orders_Detail.objects.get()





# @login_required
# def product_add_and_payment(request):