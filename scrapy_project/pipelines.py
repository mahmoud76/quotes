# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
from scrapy.exceptions import DropItem


class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = codecs.open('items.json', 'w', 'utf-8')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item


class FilterPipeline(object):

    def process_item(self, item, spider):
        if len(item['text']) > 12:
            raise DropItem("Text is too long:\n %s" % item)
        else:
            return item


class ScrapyProjectPipeline(object):
    def process_item(self, item, spider):
        return item
