# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100, verbose_name='名字')),
                ('summary', models.TextField(verbose_name='作者简介')),
            ],
            options={
                'verbose_name_plural': '作者',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255, verbose_name='书名')),
                ('summary', models.TextField(verbose_name='简介')),
                ('booktype', models.CharField(max_length=50, verbose_name='分类')),
                ('wordcount', models.IntegerField(default=0, verbose_name='字数')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('author', models.ManyToManyField(to='fEnRdr.Author', verbose_name='作者')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': '书籍',
            },
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=255, verbose_name='节标题')),
                ('chapter_id', models.IntegerField(default=0, verbose_name='节序号')),
                ('content', models.TextField(verbose_name='内容')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('book', models.ForeignKey(verbose_name='书名', to='fEnRdr.Book')),
            ],
            options={
                'ordering': ['book', '-part', '-chapter_id'],
                'verbose_name_plural': '节',
            },
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=255, verbose_name='章名')),
                ('part_id', models.IntegerField(default=0, verbose_name='章序号')),
                ('book', models.ForeignKey(verbose_name='书名', to='fEnRdr.Book')),
            ],
            options={
                'ordering': ['book', '-part_id'],
                'verbose_name_plural': '章',
            },
        ),
        migrations.AddField(
            model_name='chapter',
            name='part',
            field=models.ForeignKey(verbose_name='章', to='fEnRdr.Part'),
        ),
    ]
