from django.shortcuts import render
from django.http import HttpResponse
from algblog.models import Article, Category,Tags
from django.views.generic import View, TemplateView, ListView, DetailView

# Create your views here.
def  index(request):
    articles = Article.objects.all()
    categorys = Category.objects.all()
	#return HttpResponse('Hello algblog')
    return render(request, 'index.html', {'articles': articles, 'categorys': categorys})

def category(request):
    categorys = Category.objects.all()
    print(categorys+'111')
    return render(request, 'widgtes/category.py', {'categorys': categorys})

class BaseMixin(object):
    def get_context_data(self, *args, **kwargs):
        context = super(BaseMixin,self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['tags_list'] = Tags.objects.all()
        print(context)
        return context

class IndexView(BaseMixin, ListView):
    template_name = 'index.html'
    context_object_name = 'article_list'
    #paginate_by = 2

    def get_context_data(self, **kwargs):
        print(kwargs)
        return super(IndexView, self).get_context_data(**kwargs)
    def get_queryset(self):
        article_list = Article.objects.all()
        return article_list

class ArticleView(BaseMixin, DetailView):
    template_name = 'article_detail.html'
    model = Article
    def get_context_data(self, **kwargs):
        print(kwargs)
        context = super(ArticleView,self).get_context_data(**kwargs)
        #context['article_tags'] =
        return context
