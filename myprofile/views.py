from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from .forms import UserProfileForm, PasswordResetForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from .forms import UserProfileForm, PasswordResetForm

@login_required
def myprofile_view(request):
    user = request.user

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        password_form = PasswordResetForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('profile')

        if password_form.is_valid():
            new_password = password_form.cleaned_data['password1']
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)  # 세션의 인증 해시 갱신
            return redirect('profile')

    else:
        form = UserProfileForm(instance=user)
        password_form = PasswordResetForm()

    return render(request, 'myprofile.html', {'form': form, 'password_form': password_form})