from django.http import HttpResponseRedirect
from django.shortcuts import render ,redirect ,reverse
from .models import ShoppingCartInfo
from goods.models import GoodsInfo ,TypeInfo


def user_cart( request ):
    # 检查用户是否登录
    if not request.session['user_id']:
        return redirect('user:login')

    # 获取用户的购物车项
    cart_items = ShoppingCartInfo.objects.filter(user_id = request.session.get('user_id'))
    # cart_items = ShoppingCartInfo.objects.all()
    categories = TypeInfo.objects.all()
    # 将购物车项传递给模板
    return render(request ,'shoppingCart/cart.html' ,{'categories': categories ,'ShoppingCartInfo': cart_items})


from django.shortcuts import render ,redirect
from .models import ShoppingCartInfo


def add( request ,goods_id ,count ):
    # 检查用户是否登录
    if not request.session.get('user_id'):
        return redirect('user:login')

    # 获取用户和商品
    user_id = request.session.get('user_id')
    goods_id = goods_id

    # 检查购物车中是否已经有这个商品
    cart_item = ShoppingCartInfo.objects.filter(user_id = user_id ,goods_id = goods_id).first()

    if cart_item:
        # 如果购物车中已经有这个商品，增加数量
        cart_item.count += count
        cart_item.save()
    else:
        # 如果购物车中没有这个商品，创建一个新的购物车项
        ShoppingCartInfo.objects.create(user_id = user_id ,goods_id = goods_id ,count = count)

    # 获取用户的购物车项
    # cart_items = ShoppingCartInfo.objects.filter(user_id = request.session.get('user_id'))
    return HttpResponseRedirect(reverse('shoppingCart:cart'))


def sub( request ,goods_id ,count ):
    # 检查用户是否登录
    if not request.session.get('user_id'):
        return redirect('user:login')

    # 获取用户和商品
    user_id = request.session.get('user_id')
    goods_id = goods_id

    # 检查购物车中是否已经有这个商品
    cart_item = ShoppingCartInfo.objects.filter(user_id = user_id ,goods_id = goods_id).first()

    if cart_item:
        # 如果购物车中已经有这个商品，减少数量
        cart_item.count -= count
        cart_item.save()
    else:
        # 如果购物车中没有这个商品了，重载购物车
        return HttpResponseRedirect(reverse('shoppingCart:cart'))

    # 获取用户的购物车项
    # cart_items = ShoppingCartInfo.objects.filter(user_id = request.session.get('user_id'))
    return HttpResponseRedirect(reverse('shoppingCart:cart'))


def edit( request ,cart_id ,count ):
    # 获取购物车
    cart = ShoppingCartInfo.objects.get(id = cart_id)
    # 修改购物车中的商品数量
    cart.goods.set([cart.goods.first()] * count)
    return redirect(reverse("shoppingCart:cart"))


def delete( request ,cart_id ):
    # 获取购物车
    cart = ShoppingCartInfo.objects.get(id = cart_id)
    # 清空购物车
    cart.delete()
    return redirect(reverse("shoppingCart:cart"))


def clear( request ):
    # 检查用户是否登录
    if not request.session.get('user_id'):
        return redirect('user:login')
    # 获取用户的购物车项
    cart_items = ShoppingCartInfo.objects.filter(user_id = request.session.get('user_id'))
    # 清除购物车中的所有商品
    for cart in cart_items:
        cart.delete()
    return redirect(reverse("shoppingCart:cart"))
