from django.db import models
from datetime import datetime
from goods.models import GoodsInfo


class UserInfo(models.Model):
    gender = (
        ('male' ,"男") ,
        ('female' ,"女") ,
    )

    user_name = models.CharField(verbose_name = "用户名" ,max_length = 40 ,unique = True)
    user_pwd = models.CharField(verbose_name = "用户密码" ,max_length = 128 ,blank = False)
    user_real_name = models.CharField(verbose_name = "真实姓名" ,max_length = 40)
    user_sex = models.CharField(verbose_name = "性别" ,max_length = 20 ,choices = gender ,default = "male")
    user_email = models.EmailField(verbose_name = "邮箱" ,unique = True)
    user_addr = models.CharField(verbose_name = "收货地址" ,max_length = 128 ,default = "")
    user_postal_code = models.CharField(verbose_name = "邮编" ,max_length = 6 ,default = "")
    user_tel = models.CharField(verbose_name = "联系方式" ,max_length = 11 ,default = "")
    user_register_time = models.DateTimeField(verbose_name = "注册时间" ,auto_now_add = True)

    def __str__( self ):
        return self.user_name

    class Meta:
        ordering = ['-user_register_time']
        verbose_name = "用户信息"
        verbose_name_plural = "用户信息"


class GoodsBrowser(models.Model):
    user = models.ForeignKey(UserInfo ,on_delete = models.CASCADE ,verbose_name = "用户ID")
    goods = models.ForeignKey(GoodsInfo ,on_delete = models.CASCADE ,verbose_name = "商品ID")
    browser_time = models.DateTimeField(verbose_name = "浏览时间" ,default = datetime.now)

    def __str__( self ):
        return "{0}浏览记录{1}".format(self.user.user_name ,self.goods.goods_name)

    class Meta:
        verbose_name = "用户浏览记录"
        verbose_name_plural = "用户浏览记录"

