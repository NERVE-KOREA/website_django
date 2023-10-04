# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # 다른 URL 패턴들...
    path('redpill', views.redpill_view, name='redpill'),
    path('bluepill', views.bluepill_view, name='bluepill'),
    path('brandstory', views.brandstory_view, name='brandstory'),
]