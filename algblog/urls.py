#!/usr/bin/env python
# encoding: utf-8
from algblog.views import IndexView, ArticleView, ArticleInTagView, ArticleInCategoryView


from django.conf.urls import include, url

urlpatterns = [
    #url(r'^$', 'algblog.views.index')

    url(r'^$', IndexView.as_view()),
    url(r'^article/(?P<pk>\d+)/$', ArticleView.as_view(), name = 'article_detail'),
    url(r'^tag/(?P<pk>\d+)/$', ArticleInTagView.as_view(), name = 'articleintag'),
    url(r'^category/(?P<pk>\d+)/$', ArticleInCategoryView.as_view(), name = 'articleincategory'),
]
