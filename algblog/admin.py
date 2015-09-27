from django.contrib import admin
from algblog.models import Article, Category
# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    """Docstring for ArticleAdmin. """

    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
