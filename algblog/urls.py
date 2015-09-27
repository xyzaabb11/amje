#!/usr/bin/env python
# encoding: utf-8
from algblog.views import IndexView, ArticleView


from django.conf.urls import include, url

urlpatterns = [
    #url(r'^$', 'algblog.views.index')

    url(r'^$', IndexView.as_view()),
    url(r'^article/(?P<pk>\d+)/$', ArticleView.as_view(), name = 'article_detail')
]
