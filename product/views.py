from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from cart.models import Cart

def redpill_view(request):
    if request.method == 'POST':
        redpill_quantity = request.POST.get('redpill_quantity')
        user = request.user
        user_id = user.user_id
        try:
            cart = Cart.objects.get(user_id = user_id)
            print(cart)
            cart.redpill_quantity += int(redpill_quantity)
            cart.save()
        except Cart.DoesNotExist:
            new_cart = Cart.objects.create(user_id = user_id, redpill_quantity = redpill_quantity, bluepill_quantity = 0)
            new_cart.save()
    return render(request, "redpill.html") 

def bluepill_view(request):
    return render(request, "bluepill.html") 

def brandstory_view(request):
    return render(request, "brandstory.html") 

