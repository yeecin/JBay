from django.contrib import admin
from .models import UserInfo ,GoodsBrowser

admin.site.site_header = '用户管理'
admin.site.site_title = '用户管理'


# 注册模型类
@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    # 列表里想要显示的字段
    list_display = ("id" ,"user_name")
    # 满10条自动分页
    list_per_page = 10
    # 设置哪些字段点击可以进入编辑界面
    list_display_links = ("id" ,"user_name")
    search_fields = ["user_name"]
    list_filter = ("user_name" ,"user_postal_code")
    # readonly_fields = ["user_name"]


@admin.register(GoodsBrowser)
class GoodsBrowserAdmin(admin.ModelAdmin):
    # 列表里想要显示的字段
    list_display = ("id" ,"user" ,"goods")
    # 满10条自动分页
    list_per_page = 10
    list_filter = ("user__user_name" ,"goods__goods_name")
    # 设置哪些字段点击可以进入编辑界面
    list_display_links = ["id" ,"goods"]
    search_fields = ("user__user_name" ,"goods__goods_name")
    readonly_fields = ("user" ,"goods")
    refresh_time = (3 ,5)
