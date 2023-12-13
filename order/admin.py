from django.contrib import admin
from .models import OrderTotalInfo ,OrderPartInfo

admin.site.site_header = '订单管理'
admin.site.site_title = '订单管理'


# 注册模型类
@admin.register(OrderTotalInfo)
class OrderTotalInfoAdmin(admin.ModelAdmin):
    # 列表里想要显示的字段
    list_display = ("orderID" ,"user" ,"order_addr")
    # 满10条自动分页
    list_per_page = 10
    list_filter = ["user" ,"order_time" ,"order_addr"]
    # 设置哪些字段点击可以进入编辑界面
    list_display_links = ("user" ,"order_addr")
    search_fields = ["user__username"]
    ordering = ["-order_time"]


@admin.register(OrderPartInfo)
class OrderPartInfoAdmin(admin.ModelAdmin):
    # 列表里想要显示的字段
    list_display = ("goods" ,"order" ,"price" ,"count")
    # 满10条自动分页
    list_per_page = 10
    # 设置哪些字段点击可以进入编辑界面
    list_display_links = ("goods" ,"order" ,"price" ,"count")
    list_filter = ["goods"]
