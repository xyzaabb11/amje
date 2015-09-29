from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length = 100, verbose_name='名字')
    summary = models.TextField(verbose_name = '作者简介')

    class Meta:
        verbose_name_plural = '作者'
    def __str__(self):
        return self.name;

class Book(models.Model):
    name = models.CharField(max_length = 255, verbose_name = '书名')
    author = models.ManyToManyField(Author, verbose_name = '作者')
    summary = models.TextField(verbose_name = '简介')
    booktype = models.CharField(max_length = 50, verbose_name = '分类')
    wordcount = models.IntegerField(default = 0, verbose_name = '字数')
    create_time = models.DateTimeField(auto_now_add = True, verbose_name = '创建时间')

    class Meta:
        verbose_name_plural = '书籍'
        ordering = ['name']
    def __str__(self):
        return self.name

class Part(models.Model):
    title = models.CharField(max_length = 255, verbose_name = '章名')
    book = models.ForeignKey(Book, verbose_name = '书名')
    part_id = models.IntegerField(default = 0, verbose_name = '章序号')

    class Meta:
        verbose_name_plural = '章'
        ordering = ['book', '-part_id']

    def __str__(self):
        return self.name


class Chapter(models.Model):
    title = models.CharField(max_length = 255, verbose_name = '节标题')
    book = models.ForeignKey(Book, verbose_name = '书名')
    part = models.ForeignKey(Part, verbose_name = '章')
    chapter_id = models.IntegerField(default = 0, verbose_name = '节序号')
    content = models.TextField(verbose_name = '内容')
    create_time = models.DateTimeField(auto_now_add = True, verbose_name = '创建时间')
    class Meta:
        verbose_name_plural = '节'
        ordering = ['book', '-part', '-chapter_id']

    def __str__(self):
        return self.name
