from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from cart.models import Cart

def redpill_view(request):
    user = request.user
    user_id = user.user_id
    if request.method == 'POST':
        redpill_quantity = request.POST['redpill_quantity']
        try:
            cart = Cart.objects.filter(user_id = user_id)
        except Cart.DoesNotExist:
            new_cart = Cart(user_id = user_id, redpill_quantity = redpill_quantity)
            new_cart.save()
            pass
        else:
            cart.redpill_quantity += redpill_quantity
            cart.save()
    return render(request, "redpill.html") 

def bluepill_view(request):
    return render(request, "bluepill.html") 

def brandstory_view(request):
    return render(request, "brandstory.html") 

