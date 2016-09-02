# -*- coding: utf-8 -*-

from pymongo import MongoClient, ASCENDING
from scrapy.exceptions import DropItem

from linkedin_crawler.settings import MONGODB


class MongoDBPipeline(object):
    def __init__(self):
        self.client = MongoClient(MONGODB['host'], MONGODB['port'])
        self.db = self.client[MONGODB['db']]

    def open_spider(self, spider):
        self.collection = self.db[spider.collection]
        self.collection.create_index([('url', ASCENDING)], unique=True)

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        try:
            self.collection.insert(dict(item))
        except:
            raise DropItem("Item already crawled {0}".format(item['url']))

        return item
