# encoding=utf-8

from scrapy import Item, Field


class TweetsItem(Item):
    """ 微博信息 """
    _id = Field()  # 用户ID-微博ID
    ID = Field()  # 用户ID
    Content = Field()  # 微博内容
    PubTime = Field()  # 发表时间
    Tools = Field()  # 发表工具/平台

