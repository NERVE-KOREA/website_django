from django.shortcuts import render, redirect
from signup.models import User, UserManager
from django.contrib import auth
from signup.forms import SignupForm
from django.contrib.auth import authenticate, login
# Create your views here.

def main(request):
    return render(request, "index.html")  

def signup_view(request):
    # signup 으로 POST 요청이 왔을 때, 새로운 유저를 만드는 절차를 밟는다.
    if request.method == 'POST':
        form = SignupForm(request.POST)
        print(form)
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





# def login(request):
#     if request.method == 'POST':
# def signup(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         name = request.POST['name']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#         phone_number = request.POST['phone_number']

#         is_same_username = User.objects.filter(username=username)
#         if len(is_same_username):
#             return render(request, 'error.html', {'errorMsg': '아이디가 중복되었습니다.'})
#         if password1 != password2:
#             return render(request, 'error.html', {'errorMsg': '비밀번호가 다릅니다.'})
        
#         # 비밀번호 제약 조건 확인
#         PASSWORD_VALIDATION = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,16}$'
#         if not re.match(PASSWORD_VALIDATION, password1):
#             return render(request, 'error.html', {'errorMsg': '비밀번호는 8자-16자, 특수문자[!@#$%^*+=-] 1개 이상, 숫자를 포함하여야 합니다.'})
        
#         new_user = User.objects.create_user(
#             username = username,
#             name = name,
#             password = password1,
#             phone_number = phone_number
#         )
#         new_user.save()
#         auth.login(request, new_user)
#         return redirect('/')
#     else:
#         return render(request, 'users/signup.html')

