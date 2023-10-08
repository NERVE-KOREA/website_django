from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from .forms import UserProfileForm, PasswordResetForm
from django.contrib import messages
import pdb


@login_required
def myprofile_view(request):
    user = request.user
    return render(request, 'myprofile.html')


def myprofile_password_authentication(request):
    user = request.user
    if request.method == 'POST':
        password = request.POST['password']
        if user.check_password(password):
            return redirect('/myprofile/password_reset')
        else:
            messages.error(request, '비밀번호가 일치하지 않습니다.')
    return render(request, 'password.html')

def myprofile_password_reset(request):
    user = request.user
    if request.method == 'POST':
        new_password = request.POST['new_password']
        if new_password == user.password:
            messages.error(request, '새로운 비밀번호는 기존 비밀번호와 동일할 수 없습니다.')
            return redirect('/myprofile/password_reset')
        
        user.set_password(new_password)
        user.save()
        update_session_auth_hash(request, user)  # 세션 유지
        messages.success(request, '비밀번호가 변경되었습니다.')
        return redirect('myprofile')  # 변경 완료 후 프로필 페이지로 이동
    return render(request, 'password_reset.html')
