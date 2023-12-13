from django.db import models

from Merchant.models import Merchant
from goods.models import GoodsInfo
from user.models import UserInfo


class OrderTotalInfo(models.Model):
    orderID = models.CharField(verbose_name = "总订单ID" ,max_length = 30 ,primary_key = True)
    user = models.ForeignKey(UserInfo ,on_delete = models.CASCADE ,verbose_name = "订单用户")
    order_time = models.DateTimeField(verbose_name = "下单时间" ,auto_now = True)
    order_pay = models.BooleanField(verbose_name = "是否支付" ,default = False)
    order_total = models.DecimalField(verbose_name = "订单总价" ,max_digits = 10 ,decimal_places = 2)
    order_addr = models.CharField(verbose_name = "订单收货地址" ,max_length = 128)
    merchant = models.ForeignKey(Merchant ,on_delete = models.CASCADE ,verbose_name = "商家" ,
                                 default = 1)  # 添加商家作为外键

    def __str__( self ):
        return "{0}在{1}的订单".format(self.user.user_name ,self.order_time)

    class Meta:
        verbose_name = "订单"
        verbose_name_plural = "订单"


class OrderPartInfo(models.Model):
    goods = models.ForeignKey(GoodsInfo ,on_delete = models.CASCADE ,verbose_name = "商品")
    order = models.ForeignKey(OrderTotalInfo ,on_delete = models.CASCADE ,verbose_name = "订单")
    price = models.DecimalField(verbose_name = "商品价格" ,max_digits = 7 ,decimal_places = 2)
    count = models.IntegerField(verbose_name = "商品数量" ,default = 0)

    def __str__( self ):
        return "{0}的数量为{1}".format(self.goods.goods_name ,self.count)

    class Meta:
        verbose_name = "订单详情"
        verbose_name_plural = "订单详情"
