from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


from django.contrib import admin
from django.urls import path

import login.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login.views.index, name='index'),
]
