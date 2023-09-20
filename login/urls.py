from django.contrib.auth.views import LoginView
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # 로그인 페이지
    path('login/', LoginView.as_view(), name='login'),
    path('', LoginView.as_view(), name='login'),
    # 다른 URL 패턴들을 여기에 추가할 수 있습니다.
]