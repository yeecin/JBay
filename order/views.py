from django.shortcuts import render ,redirect ,reverse

from shoppingCart.models import ShoppingCartInfo
from .models import OrderTotalInfo ,OrderPartInfo
from goods.models import GoodsInfo
from user.models import UserInfo


def order( request ):
    # 检查用户是否登录
    # if not request.session['user_id']:
    #     return redirect('user:login')
    # 获取用户的所有订单
    orders = ShoppingCartInfo.objects.filter(user_id = request.session.get('user_id'))
    return render(request ,'order/place_order.html' ,{'orders': orders})


def order_handle( request ):
    # 获取用户的所有订单
    orders = ShoppingCartInfo.objects.filter(user_id = request.session.get('user_id'))
    # 创建总订单
    order_total = OrderTotalInfo.objects.create(user_id = request.session.get('user_id') ,order_total = 0)
    total_price = 0
    # 生成订单
    for order in orders:
        # 创建订单详情
        OrderPartInfo.objects.create(order_id=order_total.orderID,goods_id = order.goods.id,price = order.goods.goods_price,count = order.count,merchant_id = order.goods.merchant_id)
        total_price += (order.goods.goods_price*order.count)
        order_total.order_total = total_price
        order_total.save()
    return redirect(reverse('order:pay',args=[order_total.orderID]))

    # # 获取表单数据
    # goods_id = request.POST.get('goods_id')
    # count = request.POST.get('count')
    # # 获取商品信息
    # good = GoodsInfo.objects.get(id = goods_id)
    # # 创建总订单
    # order_total = OrderTotalInfo.objects.create(user = request.user ,order_total = good.goods_price * count)
    # # 创建订单详情
    # OrderPartInfo.objects.create(goods = good ,order = order_total ,price = good.goods_price ,count = count)
    # return redirect(reverse("order:order"))


def pay( request ,order_id ):
    # 获取订单
    order = OrderTotalInfo.objects.get(orderID = order_id)
    orderpart=OrderPartInfo.objects.filter(order_id=order_id)
    # 设置订单状态为已支付
    order.order_pay = True
    order.save()
    for o in orderpart:
        # 清空购物车
        ShoppingCartInfo.objects.filter(user_id = request.session.get('user_id'),goods_id = o.goods_id).delete()
    return redirect(reverse("goods:index"))


from django.shortcuts import redirect ,reverse
from .models import OrderTotalInfo ,OrderPartInfo
from goods.models import GoodsInfo


def buy_now( request ,goods_id ):
    # 获取商品信息
    good = GoodsInfo.objects.get(id = goods_id)
    # 创建总订单
    order_total = OrderTotalInfo.objects.create(user_id = request.session.get('user_id') ,order_total = good.goods_price)
    # 创建订单详情
    order=OrderPartInfo.objects.create(goods = good ,order = order_total ,price = good.goods_price ,count = 1)
    # 重定向到订单页面
    return render(request ,'order/buynow.html' ,{'orders': order})
