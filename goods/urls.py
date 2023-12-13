from . import views
from django.urls import path

app_name = 'goods'

urlpatterns = [
    path('', views.index, name="index"),
    # path('list<int:type_id>/', views.good_list, name="goods_list"),
    path('goods_list/<int:type_id>/', views.good_list, name='goods_list'),
    path('<int:goods_id>/', views.detail, name="detail"),
    path('search/', views.ordinary_search, name='ordinary_search'), #全文检索
]
