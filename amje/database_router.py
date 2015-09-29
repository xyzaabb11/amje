#!/usr/bin/env python
# encoding: utf-8
form amje.setting import *

class DatabaseRouter(object):
    """docstring for DatabaseRouter"""
    def db_for_read(self, model, **hints):
        if model._meta.app_label in DATABASES:
            return DATABASE_MAP.get(model._meta.app_label)
        return None
    def db_for_write(self, model, **hints):
        if model._meta.app_label in DATABASES:
            return DATABASE_MAP.get(model._meta.app_label)
        return None
    def allow_relation(self, obj1, obj2, **hints):
        if  obj1._meta.app_label ==DATABASE_MAP.get(obj1._meta.app_label) or \
            obj2._meta.app_label ==DATABASE_MAP.get(obj2._meta.app_label)  :
            return True
        return None
    def allow_migrate(self, db, app_label, model =None, **hints):
        #print(app_label)
        if db in DATABASE_MAP:
            return DATABASE_MAP.get(app_label) == db
        elif app_label in DATABASE_MAP:
            return False
        return None
