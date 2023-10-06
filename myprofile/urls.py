# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # 다른 URL 패턴들...
    path('', views.myprofile_view, name='myprofile'),
    path('password/', views.myprofile_password_authentication, name= 'myprofile_password_authentication'),
    path('password_reset/',views.myprofile_password_reset, name= 'myprofile_password_reset'),

]