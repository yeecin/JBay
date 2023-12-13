from django.shortcuts import render ,get_object_or_404 ,redirect
from django.urls import reverse

from goods.models import TypeInfo
from order.models import OrderTotalInfo ,OrderPartInfo
from .models import GoodsInfo
from django.shortcuts import get_object_or_404
from datetime import datetime
from user.models import UserInfo,GoodsBrowser

from sklearn.metrics.pairwise import cosine_similarity

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def get_user_history_vector(user, all_goods):
    # 获取用户的浏览历史
    user_history = GoodsBrowser.objects.filter(user=user)
    # 创建一个向量来表示用户的浏览历史
    user_history_vector = [1 if goods in user_history else 0 for goods in all_goods]
    return user_history_vector

def compute_similarities(user, all_users):
    # 获取所有商品的列表
    all_goods = GoodsInfo.objects.all()
    # 获取用户的浏览历史向量
    user_vector = get_user_history_vector(user, all_goods)
    similarities = []
    for other_user in all_users:
        if user != other_user:
            # 获取其他用户的浏览历史向量
            other_user_vector = get_user_history_vector(other_user, all_goods)
            # 计算余弦相似度
            similarity = cosine_similarity(np.array(user_vector).reshape(1, -1), np.array(other_user_vector).reshape(1, -1))
            similarities.append((other_user, similarity[0][0]))
    return similarities


def recommend(user):
    # 获取用户的历史浏览信息
    user_history = GoodsBrowser.objects.filter(user=user)
    # 计算用户之间的相似度
    similarities = compute_similarities(user, UserInfo.objects.all())
    # 生成推荐列表
    recommendations = []
    # 创建一个集合来存储已经推荐的商品
    recommended_goods_set = set()
    for other_user, similarity in similarities:
        # 获取其他用户浏览过的商品
        other_user_history = GoodsBrowser.objects.filter(user=other_user)
        for goods in other_user_history:
            if goods not in user_history:
                good = GoodsInfo.objects.get(id=goods.goods_id)
                # 如果用户没有浏览过这个商品，并且这个商品还没有被推荐过
                if good not in recommended_goods_set:
                    # 把商品添加到推荐列表和推荐商品集合中
                    recommendations.append((good, similarity))
                    recommended_goods_set.add(good)
    # 根据相似度对推荐列表进行排序，推荐度高的商品排在前面
    recommendations.sort(key=lambda x: x[1], reverse=True)
    # 只返回商品信息
    recommended_goods = [rec[0] for rec in recommendations]
    return recommended_goods


def index(request):
    # 获取所有商品信息，并进行随机排序
    goods = GoodsInfo.objects.all().order_by('?')
    categories = TypeInfo.objects.all()

    # 检查用户是否已经登录
    if request.session.get('user_id'):
        user = UserInfo.objects.get(id=request.session.get('user_id'))
        # 调用推荐算法
        recommended_goods = recommend(user)
        # 创建一个集合来存储已经推荐的商品
        recommended_goods_set = set()
        for good in goods:
            if good not in recommended_goods:
                recommended_goods.append(good)
        # 将商品信息传递给模板
        return render(request, 'goods/index.html', {'categories': categories, 'goods': recommended_goods})
    else:
        # 用户未登录，显示随机排序的商品
        return render(request ,'goods/index.html' ,{'categories': categories ,'goods': goods})


from django.shortcuts import render ,get_object_or_404
from .models import TypeInfo ,GoodsInfo


def good_list( request ,type_id ):
    # 获取指定类型的商品信息
    type_info = get_object_or_404(TypeInfo ,pk = type_id)
    goods = GoodsInfo.objects.filter(goods_type = type_info).order_by('?')
    categories = TypeInfo.objects.all()
    # 将商品信息传递给模板
    return render(request ,'goods/index.html' ,{'categories': categories ,'goods': goods})





def detail(request, goods_id):
    # 获取指定ID的商品信息
    good = get_object_or_404(GoodsInfo, id=goods_id)

    # # 获取用户信息
    # user = get_object_or_404(UserInfo, user_id=request.session.get('user_id'))
    if request.session.get('user_id'):
        # 创建浏览记录
        GoodsBrowser.objects.create(user_id=request.session.get('user_id'), goods=good, browser_time=datetime.now())

    # 将商品信息传递给模板
    categories = TypeInfo.objects.all()
    return render(request, 'goods/detail.html', {'categories': categories, 'good': good})


from django.core.paginator import Paginator

def ordinary_search(request):
    # 获取查询参数
    query = request.GET.get('q', '')
    sort_order = request.GET.get('sort', 'goods_name')
    if query:
        # 根据查询参数获取商品信息
        if sort_order == 'goods_price':
            goods_list = GoodsInfo.objects.filter(goods_name__icontains=query).order_by('-goods_price')
        else:
            goods_list = GoodsInfo.objects.filter(goods_name__icontains=query).order_by(sort_order)
        # 使用分页
        paginator = Paginator(goods_list, 10)  # 每页显示10个商品
        page_number = request.GET.get('page')
        goods = paginator.get_page(page_number)
    else:
        goods = []
    # 将商品信息传递给模板
    return render(request, 'goods/ordinary_search.html', {'goods': goods, 'query': query, 'sort': sort_order})




