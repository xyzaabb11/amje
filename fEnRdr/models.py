from django.db import models

# Create your models here.
'''
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
'''
class Author(models.Model):
    name = models.CharField(max_length = 100, verbose_name = '作者')

    class Meta:
        verbose_name_plural = '作者'

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length = 100, verbose_name = '类别名称')
    parent = models.ForeignKey('self', default = None, blank = True, null = True, verbose_name='上级分类')

    class Meta:
        verbose_name_plural = '分类'
    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length = 255, verbose_name = '书名')
    author = models.ManyToManyField(Author, verbose_name = '作者')
    category = models.ForeignKey(Category, verbose_name = '类别')
    mainpage = models.CharField(max_length = 255, verbose_name = '主页')
    cover = models.CharField(max_length = 255, verbose_name = '封面')
    summary = models.TextField(verbose_name = '简介')
    epub = models.CharField(max_length = 255, default = None, null = True, verbose_name = 'epub')
    kindle = models.CharField(max_length = 255,default = None, null = True,  verbose_name = 'kindle')
    html = models.CharField(max_length = 255, default = None, null = True, verbose_name = 'html')
    txt = models.CharField(max_length = 255, default = None, null = True, verbose_name = 'txt')

    class Meta:
        verbose_name_plural = '书'
        ordering = ['name']

    def __str__(self):
        return self.name

class BookContent(models.Model):
    name = models.CharField(max_length = 255, verbose_name = '名称')
    book = models.ForeignKey(Book, verbose_name = '书名')
    content = models.TextField(verbose_name = '内容')

    class Meta:
        verbose_name_plural = '内容'

    def __str__(self):
        return self.name
