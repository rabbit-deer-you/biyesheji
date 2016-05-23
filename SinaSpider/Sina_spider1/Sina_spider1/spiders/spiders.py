# encoding=utf-8
import re
import datetime
from scrapy.spider import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request
from Sina_spider1.items import TweetsItem

class Spider(CrawlSpider):
    name = "sinaSpider"
    host = "http://weibo.cn"
    start_urls = [
        3217179555, 3217179555,
    ]
    scrawl_ID = set(start_urls)  # 记录待爬的微博ID
    finish_ID = set()  # 记录已爬的微博ID

    def start_requests(self):
        while True:
            ID = self.scrawl_ID.pop()
            self.finish_ID.add(ID)  # 加入已爬队列
            ID = str(ID)
            url_tweets = "http://weibo.cn/%s/profile?filter=0&page=328&is_all=1" % ID
            yield Request(url=url_tweets, meta={"ID": ID}, callback=self.parse2)  # 去爬微博

    def parse2(self, response):
        """ 抓取微博数据 """
        selector = Selector(response)
        tweets = selector.xpath('body/div[@class="c" and @id]')
        for tweet in tweets:
            tweetsItems = TweetsItem()
            id = tweet.xpath('@id').extract_first()  # 微博ID
            content = tweet.xpath('div/span[@class="ctt"]/text()').extract_first()  # 微博内容
            cooridinates = tweet.xpath('div/a/@href').extract_first()  # 定位坐标
            others = tweet.xpath('div/span[@class="ct"]/text()').extract_first()  # 求时间和使用工具（手机或平台）

            tweetsItems["ID"] = response.meta["ID"]
            tweetsItems["_id"] = response.meta["ID"] + "-" + id
            if content:
                tweetsItems["Content"] = content.strip(u"[\u4f4d\u7f6e]")  # 去掉最后的"[位置]"
            if others:
                others = others.split(u"\u6765\u81ea")
                tweetsItems["PubTime"] = others[0]
                if len(others) == 2:
                    tweetsItems["Tools"] = others[1]
                else:
                    tweetsItems["Tools"] = u""
            yield tweetsItems
        url_next = selector.xpath(
            u'body/div[@class="pa" and @id="pagelist"]/form/div/a[text()="\u4e0b\u9875"]/@href').extract()
        if url_next:
            yield Request(url=self.host + url_next[0], meta={"ID": response.meta["ID"]}, callback=self.parse2)
            print (self.host + url_next[0])