from django import forms
from signup.models import User

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_id']


class PasswordResetForm(forms.Form):
    password1 = forms.CharField(label='새 비밀번호', widget=forms.PasswordInput)
    password2 = forms.CharField(label='새 비밀번호 확인', widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('비밀번호가 일치하지 않습니다.')
        
        return password2