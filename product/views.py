from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from signup.models import User

def redpill_view(request):
    return render(request, "redpill.html") 

def bluepill_view(request):
    return render(request, "bluepill.html") 

def brandstory_view(request):
    return render(request, "brandstory.html") 



# @login_required
# def product_add_to_cart(request):
#     user = request.user
#     if request.mehtod == 'POST':
        

    





# @login_required
# def product_add_and_payment(request):