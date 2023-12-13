from . import views
from django.urls import path

app_name = 'shoppingCart'

urlpatterns = [
    path('', views.user_cart, name="cart"),
    path('add<int:goods_id>_<int:count>/', views.add, name="add"),
    path('sub<int:goods_id>_<int:count>/', views.sub, name="sub"),
    path('edit<int:cart_id>_<int:count>/', views.edit, name="edit"),
    path('delete<int:cart_id>/', views.delete, name="delete"),
    path('clear/', views.clear, name="clear"),
]
