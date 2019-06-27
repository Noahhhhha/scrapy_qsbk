# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

'''
    将items的模型存储到本地磁盘中
'''
class QsbkPipeline(object):
    def process_item(self, item, spider):
        return item
