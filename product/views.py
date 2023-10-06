from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def redpill_view(request):
    return render(request, "redpill.html") 

def bluepill_view(request):
    return render(request, "bluepill.html") 

def brandstory_view(request):
    return render(request, "brandstory.html") 



