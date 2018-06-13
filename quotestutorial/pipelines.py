# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import pymongo


class TextPipeline(object):
    def __init__(self):
        self.limit = 50

    def process_item(self, item, spider):
        print('in TextPipeline process_item ---------------------------------')     # step 3
        if item['text']:
            if len(item['text']) > self.limit:
                item['text'] = item['text'][0: self.limit].rstrip() + '...'
            return item
        else:
            return DropItem('Missing Text')


class MongoPipeline(object):
    def __init__(self, mongo_url, mongo_db):
        self.mongo_url = mongo_url
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        print('in MongoPipeline from_crawler ---------------------------------')            # step 1
        return cls(
            mongo_url=crawler.settings.get('MONGO_URL'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        print('in MongoPipeline open_spider ---------------------------------')             # step 2
        self.client = pymongo.MongoClient(self.mongo_url)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        print('in MongoPipeline process_item ---------------------------------')             # step 4
        table_name = item.__class__.__name__
        self.db[table_name].insert(dict(item))
        return item

    def close_spider(self, spider):
        print('in MongoPipeline close_spider ---------------------------------')
        self.client.close()

