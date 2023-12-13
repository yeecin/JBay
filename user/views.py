from django.http import JsonResponse ,HttpResponse
from django.shortcuts import render ,redirect ,reverse
from django.contrib.auth import authenticate ,login ,logout

from goods.models import TypeInfo
from .models import UserInfo

from django.shortcuts import render ,redirect
from user.forms import RegisterForm


def register( request ):
    categories = TypeInfo.objects.all()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:login')
    else:
        form = RegisterForm()
    return render(request ,'user/register.html' ,{'form': form,'categories': categories})


def register_handle( request ):
    return redirect(reverse('user:login'))


def register_exist( request ):
    username = request.GET.get('username')
    if UserInfo.objects.filter(username = username).exists():
        return JsonResponse({'status': 'error' ,'msg': '用户名已存在'})
    else:
        return JsonResponse({'status': 'success' ,'msg': '用户名可用'})


from django.contrib.auth import authenticate ,login as auth_login

from django.contrib.auth import authenticate ,login
from django.contrib.auth.hashers import check_password
from .models import UserInfo


def user_login( request ):
    categories = TypeInfo.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = UserInfo.objects.get(user_name = username)
        except UserInfo.DoesNotExist:
            # 如果用户不存在，重定向到注册页面
            # 用户不存在，返回登录表单并显示错误消息
            return redirect(reverse('user:register'))

        if check_password(password ,user.user_pwd):
            request.session['user_id'] = user.id  # 在session中保存用户ID
            request.session['username'] = username  # 在session中保存用户名
            return redirect(reverse('goods:index'))
        else:
            return render(request ,'user/login.html' ,{'error': '密码错误'})
    else:
        return render(request ,'user/login.html',{'categories': categories})


# def user_login( request ):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request ,username = username ,password = password)
#         if user is not None:
#             auth_login(request ,user)
#             return redirect(reverse('goods:index'))
#         else:
#             # 如果用户不存在，重定向到注册页面
#             return redirect(reverse('user:register'))
#     else:
#         return render(request ,'user/login.html')


def login_handle( request ):
    return redirect(reverse('user:login'))


def user_logout( request ):
    try:
        del request.session['user_id']  # 删除session中的用户ID
    except KeyError:
        pass  # 如果session中没有用户ID，那么什么都不做
    return redirect(reverse('goods:index'))  # 重定向到首页


def info( request ):
    user = request.user
    return render(request ,'user/user_center_info.html' ,{'user': user})


def order( request ,index ):
    user = request.user
    orders = user.order_set.all()
    return render(request ,'user/user_center_order.html' ,{'orders': orders})


def site( request ):
    user = request.user
    return render(request ,'user/user_center_site.html' ,{'user': user})
