from django.db import models
from user.models import UserInfo
from goods.models import GoodsInfo


class ShoppingCartInfo(models.Model):
    user = models.ForeignKey(UserInfo ,on_delete = models.CASCADE ,verbose_name = "用户")
    goods = models.ForeignKey(GoodsInfo ,on_delete = models.CASCADE ,verbose_name = "商品")
    count = models.IntegerField(verbose_name = "数量" ,default = 0)

    def __str__( self ):
        return self.user.user_name + "的购物车"

    class Meta:
        verbose_name = "购物车"
        verbose_name_plural = "购物车"
