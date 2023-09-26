from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # 로그인 페이지
    path('', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
]
    # 다른 URL 패턴들을 여기에 추가할 수 있습니다.
