#!/usr/bin/env python
# encoding: utf-8

import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(is_safe=True)  #注册template filter
@stringfilter  #希望字符串作为参数
def custom_markdown(value):
    #extensions = ["nl2br", ]

    return mark_safe(markdown.markdown(value,
        extensions = ['markdown.extensions.fenced_code', 'markdown.extensions.codehilite','markdown.extensions.nl2br'],
                                       safe_mode=True,
                                       enable_attributes=False))
