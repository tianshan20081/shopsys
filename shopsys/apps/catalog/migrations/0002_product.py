# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-18 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='名称')),
                ('slug', models.SlugField(help_text='根据name生成的，用于生成页面URL，必须唯一', max_length=255, unique=True, verbose_name='Slug')),
                ('brand', models.CharField(max_length=50, verbose_name='品牌')),
                ('sku', models.CharField(max_length=50, verbose_name='计量单位')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='价格')),
                ('old_price', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=9, verbose_name='旧价格')),
                ('image', models.ImageField(max_length=50, upload_to='products', verbose_name='图片')),
                ('is_active', models.BooleanField(default=True, verbose_name='设为激活')),
                ('is_bestseller', models.BooleanField(default=False, verbose_name='标为畅销')),
                ('is_featured', models.BooleanField(default=False, verbose_name='标为推荐')),
                ('quantity', models.IntegerField(verbose_name='数量')),
                ('description', models.TextField(verbose_name='描述')),
                ('meta_keywords', models.CharField(help_text='meta 关键词标签, 逗号分隔', max_length=255, verbose_name='Meta关键词')),
                ('meta_description', models.CharField(help_text='meta 描述标签', max_length=255, verbose_name='Meta描述')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('categories', models.ManyToManyField(to='catalog.Category')),
            ],
            options={
                'ordering': ['-created_at'],
                'db_table': 'tb_products',
            },
        ),
    ]
