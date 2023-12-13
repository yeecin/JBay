from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('', views.order, name="order"),
    path('handle/', views.order_handle, name="order_handle"),
    path('pay/<int:order_id>/', views.pay, name="pay"),
    path('buy_now/<int:goods_id>/', views.buy_now, name='buy_now'),
]
