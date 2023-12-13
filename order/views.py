from django.shortcuts import render ,redirect ,reverse
from .models import OrderTotalInfo ,OrderPartInfo
from goods.models import GoodsInfo
from user.models import UserInfo


def order( request ):
    # 获取用户的所有订单
    orders = OrderTotalInfo.objects.filter(user = request.user)
    return render(request ,'order/place_order.html' ,{'orders': orders})


def order_handle( request ):
    # 获取表单数据
    goods_id = request.POST.get('goods_id')
    count = int(request.POST.get('count'))
    # 获取商品信息
    good = GoodsInfo.objects.get(id = goods_id)
    # 创建总订单
    order_total = OrderTotalInfo.objects.create(user = request.user ,order_total = good.goods_price * count)
    # 创建订单详情
    OrderPartInfo.objects.create(goods = good ,order = order_total ,price = good.goods_price ,count = count)
    return redirect(reverse("order:order"))


def pay( request ,order_id ):
    # 获取订单
    order = OrderTotalInfo.objects.get(id = order_id)
    # 设置订单状态为已支付
    order.order_pay = True
    order.save()
    return redirect(reverse("order:order"))


from django.shortcuts import redirect ,reverse
from .models import OrderTotalInfo ,OrderPartInfo
from goods.models import GoodsInfo


def buy_now( request ,goods_id ):
    # 获取商品信息
    good = GoodsInfo.objects.get(id = goods_id)
    # 创建总订单
    order_total = OrderTotalInfo.objects.create(user = request.user ,order_total = good.goods_price)
    # 创建订单详情
    OrderPartInfo.objects.create(goods = good ,order = order_total ,price = good.goods_price ,count = 1)
    # 重定向到订单页面
    return redirect(reverse("order:order"))
