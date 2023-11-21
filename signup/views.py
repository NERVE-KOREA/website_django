from django.shortcuts import render, redirect
from signup.models import User
from django.contrib import auth
from signup.forms import SignupForm
from django.contrib.auth.decorators import login_required
from myprofile.forms import UserProfileForm
from django.http import JsonResponse
# Create your views here.

def main(request):
    return render(request, "index.html")  

def signup_view(request):
    # signup 으로 POST 요청이 왔을 때, 새로운 유저를 만드는 절차를 밟는다.
    if request.method == 'POST':
        try :  
            user_id = request.POST['user_id']
            user = User.objects.get(user_id = user_id)
            return JsonResponse({'status': 'error', 'message': '아이디가 이미 사용 중입니다.'})
        except User.DoesNotExist: 
            form = SignupForm(request.POST)
        # form의 완성도 검증
            if form.is_valid():
                # user 객체를 새로 생성
                user = User.objects.create_user(user_id = form.cleaned_data['user_id'],
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
                return render(request, "login.html", {'message' : '성공적으로 가입되었습니다'})  
        # signup으로 GET 요청이 왔을 때, 회원가입 화면을 띄워준다.
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

def id_duplication_check(request):
    if request.method == 'GET' and 'user_id' in request.GET:
        user_id = request.GET['user_id']
        try : 
            User.objects.get(user_id = user_id)
            print(1)
            return JsonResponse({'status': 'error', 'message': '아이디가 이미 사용 중입니다.'})
        except User.DoesNotExist:
            print(2)
            return JsonResponse({'status': 'error', 'message': '사용 가능한 아이디입니다.'})
    return JsonResponse ({'status': 'error', 'message': '아이디가 이미 사용 중입니다.'})


