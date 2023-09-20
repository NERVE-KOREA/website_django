from django import forms

GENDER_CHOICES = [
    ('male', '남성'),
    ('female', '여성'),
]

SIGN_UP_PATH = [
    ('1', '경로를 선택해주세요'),
    ('2','인스타그램'),
    ('3','페이스북'),
    ('4','와디즈'),
]

class SignupForm(forms.Form):
    user_id = forms.CharField(max_length= 40, required= True)
    password1 = forms.CharField(widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, required=True)
    user_name = forms.CharField(max_length=10, required=True)
    phone_number = forms.CharField(max_length=11, required=True) ### 전화번호 형식 통일
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)
    email = forms.EmailField(
        label="이메일",
        widget=forms.EmailInput(attrs={'placeholder': '이메일 주소를 입력하세요'}),
        help_text="유효한 이메일 주소를 입력하세요."
    )   
    email_notification_acceptance = forms.BooleanField(required=True)
    birthdate = forms.DateField(required=True, widget=forms.SelectDateWidget(years=range(1920, 2023)))
    sign_up_path = forms.ChoiceField(choices=SIGN_UP_PATH, required=True)

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise forms.ValidationError("비밀번호가 일치하지 않습니다. 다시 확인하세요.")

