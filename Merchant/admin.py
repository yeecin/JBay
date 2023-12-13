from django.contrib import admin
from .models import Merchant

admin.site.site_header = '商家管理'
admin.site.site_title = '商家管理'


@admin.register(Merchant)
class MerchantAdmin(admin.ModelAdmin):
    # 列表里想要显示的字段
    list_display = ("id" ,"merchant_name" ,"real_name" ,"merchant_sex" ,"merchant_phone" ,"merchant_register_time")
    # 满10条自动分页
    list_per_page = 10
    # 设置哪些字段点击可以进入编辑界面
    list_display_links = ("id" ,"merchant_name")
    search_fields = ["merchant_name" ,"real_name"]
    list_filter = ("merchant_name" ,"real_name" ,"merchant_sex")
    # readonly_fields = ["merchant_name"]
