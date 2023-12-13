from django.shortcuts import render ,get_object_or_404 ,redirect
from django.urls import reverse

from goods.models import TypeInfo
from order.models import OrderTotalInfo ,OrderPartInfo
from .models import GoodsInfo


def index( request ):
    # 获取所有商品信息
    goods = GoodsInfo.objects.all()
    categories = TypeInfo.objects.all()
    # 将商品信息传递给模板
    return render(request ,'goods/index.html' ,{'categories': categories ,'goods': goods})


from django.shortcuts import render ,get_object_or_404
from .models import TypeInfo ,GoodsInfo


def good_list( request ,type_id ):
    # 获取指定类型的商品信息
    type_info = get_object_or_404(TypeInfo ,pk = type_id)
    goods = GoodsInfo.objects.filter(goods_type = type_info)
    categories = TypeInfo.objects.all()
    # 将商品信息传递给模板
    return render(request ,'goods/index.html' ,{'categories': categories ,'goods': goods})


def detail( request ,goods_id ):
    # 获取指定ID的商品信息
    good = GoodsInfo.objects.get(id = goods_id)
    # 将商品信息传递给模板
    categories = TypeInfo.objects.all()
    return render(request ,'goods/detail.html' ,{'categories': categories ,'good': good})


def ordinary_search( request ):
    # 获取查询参数
    query = request.GET.get('q')
    # 根据查询参数获取商品信息
    goods = GoodsInfo.objects.filter(goods_name__icontains = query)
    # 将商品信息传递给模板
    return render(request ,'goods/ordinary_search.html' ,{'goods': goods})
