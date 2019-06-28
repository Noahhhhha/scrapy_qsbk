# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

'''
    item：存放爬虫爬取下来数据的模型
'''
class QsbkItem(scrapy.Item):
    author = scrapy.Field() # 定义的固定写法
    content = scrapy.Field()
