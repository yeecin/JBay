from django.db import models


class Merchant(models.Model):
    gender = (
        ('male' ,"男") ,
        ('female' ,"女") ,
    )
    # merchant_id = models.AutoField(verbose_name = "商家id" ,primary_key = True)
    merchant_name = models.CharField(verbose_name = "商家用户名" ,max_length = 200)
    real_name = models.CharField(verbose_name = "真实姓名" ,max_length = 200)
    merchant_password = models.CharField(verbose_name = "商家密码" ,max_length = 200)
    merchant_sex = models.CharField(verbose_name = "性别" ,max_length = 20 ,choices = gender ,default = "male")
    merchant_phone = models.CharField(verbose_name = "商家手机号" ,max_length = 20)
    merchant_register_time = models.DateTimeField(verbose_name = "商家注册时间" ,auto_now_add = True)

    def __str__( self ):
        return self.merchant_name

    class Meta:
        ordering = ['-merchant_register_time']
        verbose_name = "商户信息"
        verbose_name_plural = "商户信息"
