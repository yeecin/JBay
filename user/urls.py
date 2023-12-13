from . import views
from django.urls import path

app_name = 'user'

urlpatterns = [
    path('register/', views.register, name="register"),
    path('register_handle/', views.register_handle, name="register_handle"),
    path('register_exist/', views.register_exist, name="register_exist"),
    path('login/', views.user_login, name="login"),
    path('login_handle/', views.login_handle, name="login_handle"),
    path('info/', views.info, name="info"),
    path('order/<int:order_id>/', views.order, name="order"),
    path('site/', views.site, name="site"),
    path('logout/', views.user_logout, name="logout"),
]
