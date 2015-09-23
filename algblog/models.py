from django.db import models
from django.conf import settings


STATUS = {
	0: '正常',
	1: '草稿',
	2: '删除',
}

# Create your models here.
'''
class Nav(models.Model):
	"""docstring for Nav"""
	name = models.CharField(max_length=40, verbose_name='导航条内容')
	url = models.CharField(max_length = 200, verbose_name='地址')

	status = models.IntegerField(default = 0, choices = STATUS.items(), verbose_name = '状态')
	create_time = models.DateTimeField('创建时间', auto_now_add = True)

	class Meta:
		verbose_name_plural = '导航条'
		verbose_name = '导航条'
		ordering = ['-create_time']
		#app_label = '博客管理' #string_with_title('blog', '博客管理')

	def __str__(self):
		return self.name
'''
class Category(models.Model):
	"""docstring for Category"""
	name = models.CharField('名称', max_length = 40)
	parent = models. ForeignKey('self', default = None, blank = True, null = True, verbose_name='上级分类')
	rank = models.IntegerField('排序',  default = 0)
	status = models.IntegerField('状态', default = 0, choices = STATUS.items())

	create_time = models.DateTimeField('创建时间', auto_now_add = True)

	class Meta:
		verbose_name_plural = verbose_name = '分类'
		ordering = ['rank', '-create_time']
	def __str__(self):
		if self.parent:
			return '%s --> %s' % (self.parent, self.name)
		else:
			return self.name

class Article(models.Model):
	"""docstring for Article"""
	author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name = '作者')
	category = models.ForeignKey(Category, verbose_name = '分类')
	title = models.CharField(max_length = 100, verbose_name='标题')
	#en_title = models.CharField(max_length = 100, verbose_name = '英文标题')
	#img = models.CharField(max_length = 200, default = r'/static/img/article/default.jpg', verbose_name='封面')
	tags = models.CharField(max_length = 200, null = True, blank = True, verbose_name='标签', help_text='用逗号分隔')
	#summary = models.TextField(verbose_name = '摘要')
	content = models.TextField(verbose_name = '正文')
	#summary = UEditorField('摘要', width =860, height = 500, toolbars = 'full', imagePath = 'algblog/static/upload',filePath = 'algblog/static/upload', \
	#	upload_settings = {'imageMaxSize':1024000}, settings = {}, command= None, blank=True)
	#content = UEditorField('正文', width =860, height = 500, toolbars = 'full', imagePath = 'algblog/static/upload',filePath = 'algblog/static/upload', \
	#	upload_settings = {'imageMaxSize':1024000}, settings = {}, command= None, blank=True)
	

	view_times = models.IntegerField(default = 0, verbose_name='浏览次数')
	agree_times = models.IntegerField(default = 0, verbose_name='被赞次数')
	is_top = models.BooleanField(default = False, verbose_name = '置顶')
	rank = models.IntegerField(default = 0, verbose_name='排序')
	status = models.IntegerField(default = 0, choices = STATUS.items(), verbose_name ='状态')

	pub_time = models.DateTimeField(default = False, verbose_name = ' 发布时间')
	create_time = models.DateTimeField('创建时间', auto_now_add = True)
	update_time = models.DateTimeField('发布时间', auto_now = True)


	def get_tags(self):
		return self.tags.split(',')

	class Meta:
		verbose_name = verbose_name_plural = '文章'
		ordering = ['rank', '-is_top', '-pub_time', '-create_time']

	def __str__(self):
		return self.title

'''
class Column(models.Model):
	"""docstring for Column"""
	name = models.CharField(max_length = 40, verbose_name = '专栏文章')
	summary = models.TextField(verbose_name = '专栏摘要')
	article = models.ManyToManyField(Article, verbose_name = '文章')
	status = models.IntegerField(default = 0, choices = STATUS.items(), verbose_name = '状态')
	create_time = models.DateTimeField('创建时间', auto_now_add = True)

	class Meta:
		verbose_name = verbose_name_plural = '专栏'
		ordering = ['-create_time']

	def __str__(self):
		return self.name
'''		
		