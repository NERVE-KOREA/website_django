from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from login.forms import CustomAuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView
from django.contrib import messages

class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = CustomAuthenticationForm

    def form_valid(self, form):
        # 로그인 성공 시 부모 클래스의 form_valid 메서드를 호출하여 로그인 처리를 수행합니다.
        response = super().form_valid(form)
        
        # 로그인 성공 후 리디렉션할 URL을 설정합니다.
        redirect_to = self.get_success_url()
        
        # 리디렉션을 위한 HttpResponse 객체를 생성합니다.
        from django.http import HttpResponseRedirect
        return HttpResponseRedirect(redirect_to)
    

class CustomLogoutView(LogoutView):
    template_name = 'index.html'
    # 로그아웃 메서드 오버라이드
    def logout(self, request):
        
        # 로그아웃 동작 수행
        super().logout(request)
        
        # 로그아웃 후에 index.html로 리디렉션
        return redirect('index')  # 'index'는 index.html로 리디렉션할 URL 패턴의 이름