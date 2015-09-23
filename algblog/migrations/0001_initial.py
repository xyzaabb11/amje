# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('tags', models.CharField(blank=True, max_length=200, null=True, help_text='用逗号分隔', verbose_name='标签')),
                ('content', models.TextField(verbose_name='正文')),
                ('view_times', models.IntegerField(default=0, verbose_name='浏览次数')),
                ('agree_times', models.IntegerField(default=0, verbose_name='被赞次数')),
                ('is_top', models.BooleanField(default=False, verbose_name='置顶')),
                ('rank', models.IntegerField(default=0, verbose_name='排序')),
                ('status', models.IntegerField(default=0, choices=[(0, '正常'), (1, '草稿'), (2, '删除')], verbose_name='状态')),
                ('pub_time', models.DateTimeField(default=False, verbose_name=' 发布时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='发布时间')),
                ('author', models.ForeignKey(verbose_name='作者', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['rank', '-is_top', '-pub_time', '-create_time'],
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='名称')),
                ('rank', models.IntegerField(default=0, verbose_name='排序')),
                ('status', models.IntegerField(default=0, choices=[(0, '正常'), (1, '草稿'), (2, '删除')], verbose_name='状态')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('parent', models.ForeignKey(blank=True, verbose_name='上级分类', default=None, to='algblog.Category', null=True)),
            ],
            options={
                'ordering': ['rank', '-create_time'],
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(verbose_name='分类', to='algblog.Category'),
        ),
    ]
