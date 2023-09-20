from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


# custom user model 사용 시 UserManager 클래스와 create_user, create_superuser 함수가 정의되어 있어야 함
class UserManager(BaseUserManager):
	# 필수로 필요한 데이터를 선언
    def create_user(self, user_id,  user_name, phone_number, email, gender, email_notification_acceptance, birthdate, sign_up_path, password):
        if not user_id:
            raise ValueError("Users msut have id")
        user = self.model(
            user_id = user_id,
            user_name = user_name,
            phone_number = phone_number,
            email = self.normalize_email(email),
            gender = gender,
            email_notification_acceptance = email_notification_acceptance,
            birthdate = birthdate,
            sign_up_path = sign_up_path
        )

        user.set_password(password) # change user password
        user.save(using=self._db)
        return user 

    # python manage.py createsuperuser 사용 시 해당 함수가 사용됨
    def create_superuser(self, user_id,  user_name, phone_number, email, gender, birthdate, password=None):
      
        user = self.create_user(
            user_id = user_id,
            user_name = user_name,
            phone_number = phone_number,
            email = self.normalize_email(email),
            gender = gender,
            email_notification_acceptance = False,
            birthdate = birthdate,
            password = password
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):
    user_id = models.CharField("사용자 계정", max_length= 40, primary_key=True, unique=True)
    password = models.TextField("비밀번호")
    user_name = models.CharField("사용자 이름", max_length=10)
    phone_number = models.CharField("전화번호", max_length=11, unique=True)
    email = models.CharField("이메일", max_length=40, unique=True)
    gender = models.CharField("성별", max_length=10)
    email_notification_acceptance = models.BooleanField("이메일 수신여부", default=False)
    birthdate = models.DateField("생년월일")
    sign_up_path = models.CharField("가입경로", max_length=100)
    sign_up_date = models.DateTimeField("가입시기", auto_now_add=True)
    user_update_date = models.DateTimeField("프로필 업데이트 시기", auto_now=True)

    

    # 활성화 여부 (기본값은 True)
    is_active = models.BooleanField(default=True)
    # 관리자 권한 여부 (기본값은 False)
    is_admin = models.BooleanField(default=False)
    # 
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['user_name', 'phone_number','gender','email','birthdate']

    objects = UserManager()

    @property
    def is_staff(self):
        return self.is_admin
    
    def __str__(self):
        return f"{self.user_id} / {self.user_name} / {self.email}"
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
 
