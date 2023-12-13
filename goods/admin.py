from django.contrib import admin
from .models import TypeInfo ,GoodsInfo

admin.site.site_header = '商品管理'
admin.site.site_title = '商品管理'


# 注册模型类
@admin.register(TypeInfo)
class TypeInfoAdmin(admin.ModelAdmin):
    # 列表里想要显示的字段
    list_display = ("id" ,"type_name")
    # 满10条自动分页
    list_per_page = 10
    # 设置哪些字段点击可以进入编辑界面
    list_display_links = ("id" ,"type_name")
    search_fields = ["type_name"]


@admin.register(GoodsInfo)
class GoodsInfoAdmin(admin.ModelAdmin):
    # 列表里想要显示的字段
    list_display = (
    "id" ,"goods_name" ,"goods_price" ,"goods_unit" ,"goods_click" ,"goods_description" ,"goods_inventories" ,
    "goods_type" ,"goods_suggest")
    # 满10条自动分页
    list_per_page = 20
    # 设置哪些字段点击可以进入编辑界面
    list_display_links = ("id" ,"goods_name")
    search_fields = ("goods_name" ,"goods_description" ,"goods_details")
    list_editable = ["goods_inventories"]
    readonly_fields = ["goods_click"]
