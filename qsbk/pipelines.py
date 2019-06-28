# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

'''
    将items的模型存储到本地磁盘中
'''
import json
class QsbkPipeline(object):
    def __init__(self):
        self.fp = open("duanzi.json",'w',encoding='utf-8') #创建文件

    def open_spider(self,spider):
        print('爬虫开始了...')

    def process_item(self, item, spider): #当有对象传递过来的时候，调用这个方法
        # 传话成json字符串 json.dumps 序列化时对中文默认使用的ascii编码.想输出真正的中文需要指定ensure_ascii=False：
        # 转化成字典才能dump成json
        item_json = json.dumps(dict(item),ensure_ascii=False)
        self.fp.write(item_json+'\n') #写入文件中
        return item

    def close_spider(self,spider):
        self.fp.close() #关闭流
        print('爬虫结束了...')