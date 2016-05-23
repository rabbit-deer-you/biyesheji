# encoding=utf-8
import pymongo
from items import TweetsItem


class MongoDBPipleline(object):
    def __init__(self):
        clinet = pymongo.MongoClient("localhost", 27017)
        db = clinet["Sina1"]
        self.Tweets = db["Tweets"]

    def process_item(self, item, spider):
        """ 判断item的类型，并作相应的处理，再入数据库 """
        try:
            self.Tweets.insert(dict(item))
        except Exception:
            pass

        return item
