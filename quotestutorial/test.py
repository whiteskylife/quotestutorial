#!/usr/bin/env python
# -*-coding:utf-8 -*-
from lxml import etree

# class QuoteItem():
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     text = 1
#     author = 2
#     tags = 3
#
# obj = QuoteItem()
# obj['text'] = 2
#



# def extendList(val, list=[]):
#     list.append(val)
#     print(id(list))
#     return list
#
# list1 = extendList(10)
# list2 = extendList(123, [])
# list3 = extendList('a')
# print(list1)
# print(list2)
# print(list3)

# class Foo(object):
#
#     def __init__(self):
#         print('in init')
#
#     def test(self):
#         print('in test function')
#
#
#
# obj = Foo()
# # print(obj.__class__.__name__)
# print(Foo.__class__)
#
# class Foo:
#     def test(self):
#         cls = self.__class__
#         cls_module = self.__class__.__module__
#         cls_name = self.__class__.__name__
#         return cls, cls_name, cls_module
#
# # a = getattr(Foo, 'test')
# # print(a.__code__)
#
# a = Foo()
# print(a.test())
# dic = {'asd': '11111','asddddd':{'inner': 'keysss'}, 'o': 'ppppp'}
# a = dic.values()
# print(a)

# a = [1, 2, 3, 4]
class Foo:

    def test(self):
        return self._test()

    def _test(self):
        return 'in _test'


obj = Foo()
a = obj.test()
print(a)

import scrapy_redis