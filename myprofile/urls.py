# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # 다른 URL 패턴들...
    path('', views.myprofile_view, name='myprofile'),
]