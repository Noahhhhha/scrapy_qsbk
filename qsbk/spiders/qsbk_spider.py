# -*- coding: utf-8 -*-
import scrapy

#继承 scrapy.Spider 类
from qsbk.items import QsbkItem


class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider' # 爬虫的名字，在项目是唯一的
    allowed_domains = ['qiushibaike.com'] #域名的限定
    start_urls = ['https://www.qiushibaike.com/text/page/1/'] #起始地址
    base_domain = "https://www.qiushibaike.com"

    def parse(self, response): #收到的回复
        #返回类型为 requset 模块中 SelectorList
        duanzidivs = response.xpath("//div[@id='content-left']/div")
        for duanzidiv in duanzidivs :
            print("=" * 30)
            #返回类型为 Selector
            #Selector是基于lxml来构建的，支持Xpath选择器、CSS选择器以及正则表达式
            author = duanzidiv.xpath(".//h2/text()").get().strip() #get() 如果有多个匹配，返回第一个匹配并转化为字符串，没有就返回null，等价于extract_first()方法
            content = duanzidiv.xpath(".//div[@class='content']//text()").getall() #getall() 返回包含所有结果，转换为一个列表，等价于extract()方法
            content = "".join(content).strip() # 去除掉换行符等

            # duanzi = {"author" : author, "content" : content}
            # yield duanzi #将每一个段子移交给引擎engine，引擎调用pipline

            # 将数据返回给engine，调用pipline
            # 使用item更专业，一个特定的类，而非字典
            item = QsbkItem(author = author, content = content)
            yield  item
        next_url = response.xpath("//ul[@class='pagination']/li[last()]/a/@href").get() #找到下一页的链接
        if not next_url: # 如果没有下一页了
            return
        else:
            #yield 函数类似于迭代器加return关键字
            yield scrapy.Request(self.base_domain+next_url,callback=self.parse) #回调方法