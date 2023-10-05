from django.contrib import admin
from django.urls import path, include
from signup.views import main
from login import views

urlpatterns = [
    path('', main ),
    path('signup/', include('signup.urls')),
    path('login/', include('login.urls')),
    path('admin/', admin.site.urls),
    path('myprofile/',include('myprofile.urls')),
    path('product/', include('product.urls')),
    
    # 다른 앱의 URL 패턴들을 여기에 추가할 수 있습니다.
    # 루트 경로에 대한 URL 패턴을 정의해야 합니다.

]

