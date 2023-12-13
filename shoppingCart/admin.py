from django.contrib import admin
from .models import ShoppingCartInfo

admin.site.site_header = '购物车管理'
admin.site.site_title = '购物车管理'


@admin.register(ShoppingCartInfo)
class ShoppingCartInfoAdmin(admin.ModelAdmin):
    # 列表里想要显示的字段
    list_display = ("user" ,"goods" ,"count")
    # 满10条自动分页
    list_per_page = 10
    # 设置哪些字段点击可以进入编辑界面
    list_display_links = ["user"]
    search_fields = ("user__user_name" ,"goods__goodsname")
    list_filter = ["user" ,"goods" ,"count"]
    readonly_fields = ("user" ,"goods" ,"count")
