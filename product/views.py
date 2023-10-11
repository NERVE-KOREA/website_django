from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from cart.models import Cart

def redpill_view(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == '장바구니에 추가':
            product_add_to_cart_red(request)
            return redirect('redpill')
        if action == '구매하기':
            product_add_to_cart_red(request)
            return render(request, "cart.html")
    return render(request, "redpill.html") 

def bluepill_view(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == '장바구니에 추가':
            product_add_to_cart_blue(request)
            return redirect('bluepill')
        if action == '구매하기':
            product_add_to_cart_blue(request)
            return render(request, "cart.html")
    return render(request, "bluepill.html")

def brandstory_view(request):
    return render(request, "brandstory.html") 

def product_add_to_cart_red(request):
    redpill_quantity = request.POST.get('redpill_quantity')
    user = request.user
    user_id = user.user_id
    try:
        cart = Cart.objects.get(user_id = user_id)
        cart.redpill_quantity += int(redpill_quantity)
        cart.save()
    except Cart.DoesNotExist:
        new_cart = Cart.objects.create(user_id = user_id, redpill_quantity = redpill_quantity, bluepill_quantity = 0)
        new_cart.save()

def product_add_to_cart_blue(request):
    bluepill_quantity = request.POST.get('bluepill_quantity')
    user = request.user
    user_id = user.user_id
    try:
        cart = Cart.objects.get(user_id = user_id)
        cart.bluepill_quantity += int(bluepill_quantity)
        cart.save()
    except Cart.DoesNotExist:
        new_cart = Cart.objects.create(user_id = user_id, redpill_quantity = 0, bluepill_quantity = bluepill_quantity)
        new_cart.save()

