from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, "signup.html")

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