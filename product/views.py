from django.shortcuts import render
from signup.models import User

def redpill_view(request):
    return render(request, "redpill.html") 

def bluepill_view(request):
    return render(request, "bluepill.html") 

def brandstory_view(request):
    return render(request, "brandstory.html") 
