from cart.views import cart_view
from django.urls import path, include
from . import views
urlpatterns = [
    # 다른 URL 패턴들...
    path('', views.cart_view, name='cart_view'),
]