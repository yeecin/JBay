# Generated by Django 5.0 on 2023-12-04 13:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TypeInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("isDelete", models.BooleanField(default=False)),
                ("type_name", models.CharField(max_length=20, verbose_name="分类")),
                ("serial_number", models.CharField(max_length=20, verbose_name="系统编号")),
            ],
            options={
                "verbose_name": "商品类型",
                "verbose_name_plural": "商品类型",
            },
        ),
        migrations.CreateModel(
            name="GoodsInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("isDelete", models.BooleanField(default=False)),
                (
                    "goods_name",
                    models.CharField(max_length=40, unique=True, verbose_name="商品名称"),
                ),
                (
                    "goods_image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="goods/image/%Y/%m",
                        verbose_name="商品图片",
                    ),
                ),
                (
                    "goods_price",
                    models.DecimalField(
                        decimal_places=2, max_digits=7, verbose_name="商品价格"
                    ),
                ),
                (
                    "goods_unit",
                    models.CharField(
                        default="500g", max_length=20, verbose_name="单位重量"
                    ),
                ),
                ("goods_click", models.IntegerField(default=0, verbose_name="点击量")),
                (
                    "goods_description",
                    models.CharField(max_length=128, verbose_name="商品简介"),
                ),
                (
                    "goods_inventories",
                    models.IntegerField(default=0, verbose_name="商品库存"),
                ),
                (
                    "goods_details",
                    models.CharField(max_length=256, verbose_name="商品详情"),
                ),
                (
                    "goods_suggest",
                    models.BooleanField(default=False, verbose_name="是否推荐"),
                ),
                (
                    "goods_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="goods.typeinfo",
                        verbose_name="分类",
                    ),
                ),
            ],
            options={
                "verbose_name": "商品信息",
                "verbose_name_plural": "商品信息",
            },
        ),
    ]