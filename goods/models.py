from django.db import models
from datetime import datetime
from tinymce.models import HTMLField

from Merchant.models import Merchant


class TypeInfo(models.Model):
    # 商品分类信息
    isDelete = models.BooleanField(default = False)  # 分类信息属于重要信息，需要使用逻辑删除，及假删除
    type_name = models.CharField(verbose_name = "分类" ,max_length = 20)
    serial_number = models.CharField(verbose_name = "系统编号" ,max_length = 20)

    def __str__( self ):
        return self.type_name

    class Meta:
        verbose_name = "商品类型"
        verbose_name_plural = "商品类型"


class GoodsInfo(models.Model):
    # 具体商品信息
    # id = models.AutoField(verbose_name = "商家id" ,primary_key = True)
    isDelete = models.BooleanField(default = False)  # 商品信息属于重要信息，需要使用逻辑删除，及假删除
    goods_name = models.CharField(verbose_name = "商品名称" ,max_length = 40 ,unique = True)
    goods_image = models.ImageField(verbose_name = "商品图片" ,upload_to = 'goods/image/%Y/%m' ,null = True ,
                                    blank = True)
    goods_price = models.DecimalField(verbose_name = "商品价格" ,max_digits = 7 ,
                                      decimal_places = 2)  # 要存储的数字最大长度为7位，而带有两个小数位
    goods_unit = models.CharField(verbose_name = "单位重量" ,max_length = 20 ,default = '500g')
    goods_click = models.IntegerField(verbose_name = "点击量" ,default = 0)
    goods_description = models.CharField(verbose_name = "商品简介" ,max_length = 128)
    goods_inventories = models.IntegerField(verbose_name = "商品库存" ,default = 0)
    goods_details = models.CharField(verbose_name = "商品详情" ,max_length = 256)
    goods_type = models.ForeignKey(TypeInfo ,on_delete = models.CASCADE ,verbose_name = "分类")
    goods_suggest = models.BooleanField(verbose_name = "是否推荐" ,default = False)
    merchant = models.ForeignKey(Merchant ,on_delete = models.CASCADE ,verbose_name = "商家",default = 1)  # 添加商家作为外键
    def __str__( self ):
        return self.goods_name

    class Meta:
        verbose_name = "商品信息"
        verbose_name_plural = "商品信息"
