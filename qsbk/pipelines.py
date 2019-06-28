# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

'''
    将items的模型存储到本地磁盘中
'''
import json
'''
    优化版
    使用JsonItemExporter、JsonLinesExporter 类不需要转换为 python存储类型
'''
from scrapy.exporters import JsonItemExporter, JsonLinesItemExporter
class QsbkPipeline(object):
    def __init__(self):
        self.fp = open("duanzi3.json",'wb') #创建文件 ，以“二进制形式”
        #JsonItemExporter -- 将数据全部添加到内存中，再统一写入磁盘，存储数据满足json格式
            #self.exporter = JsonItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')
        #JsonLinesItemExporter -- 每次调用self.exporter.export_item(item)的时，就把这个item存储到磁盘中，整个文件不是json格式，不会耗内存，数据较安全
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')
        self.exporter.start_exporting()

    def open_spider(self,spider):
        print('爬虫开始了...')

    def process_item(self, item, spider): #当有对象传递过来的时候，调用这个方法
        self.exporter.export_item(item)
        return item

    def close_spider(self,spider):
        self.exporter.finish_exporting()
        self.fp.close()
        print('爬虫结束了...')


''' pipline 版本一 原始版本 -- 存储不符合 json 格式
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
'''