# -*- coding: utf-8 -*-

import json, codecs, pdb

from pymongo import *
from scrapy.exceptions import DropItem

from linkedin_crawler.settings import *

class MongoDBPipeline(object):
    def __init__(self):
        client = MongoClient(MONGODB_HOST, MONGODB_PORT)
        db = client[MONGODB_DB]
        self.collection = db[MONGODB_COLLECTION]

    def process_item(self, item, spider):
        link = {'_id': item['url']}

        if self.collection.find(link).count() > 0:
            raise DropItem("Item already crawled {0}".format(item['url']))
        else:
            self.collection.insert(link)

        return item

class JsonWithEncodingPipeline(object):
    def __init__(self):
        self.file = codecs.open(
            '/home/gmarignier/workspace/linkedin_crawler/extract.json', 
            'w', 
            encoding='utf-8'
        )

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()


