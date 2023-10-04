from django.shortcuts import render, redirect
from signup.models import User, UserManager
from django.contrib import auth
from signup.forms import SignupForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from myprofile.forms import UserProfileForm
# Create your views here.

def main(request):
    return render(request, "index.html")  

def index(request):
    return render(request,'./index.html',context_dict)
def redpill(request):
    return render(request,'./redpill.html',context_dict)
def bluepill(request):
    return render(request,'./bluepill.html',context_dict)

def signup_view(request):
    # signup 으로 POST 요청이 왔을 때, 새로운 유저를 만드는 절차를 밟는다.
    if request.method == 'POST':
        form = SignupForm(request.POST)
        # form의 완성도 검증
        if form.is_valid():
            # user 객체를 새로 생성
            user = User.objects.create_user( user_id = form.cleaned_data['user_id'],
                                            password=form.cleaned_data['password1'],
                                            user_name=form.cleaned_data['user_name'], 
                                            phone_number=form.cleaned_data['phone_number'], 
                                            gender=form.cleaned_data['gender'], 
                                            email=form.cleaned_data['email'], 
                                            email_notification_acceptance=form.cleaned_data['email_notification_acceptance'], 
                                            birthdate=form.cleaned_data['birthdate'],
                                            sign_up_path = form.cleaned_data['sign_up_path'])
            # 로그인 한다
            auth.login(request, user)
            # home으로 돌려보내준다     
            return render(request, "login.html")  
        # signup으로 GET 요청이 왔을 때, 회원가입 화면을 띄워준다.
        else:
            pass
            ################################
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def profile_view(request):
    user = request.user

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = UserProfileForm(instance=user)

    return render(request, 'profile.html', {'form': form})


