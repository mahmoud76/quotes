# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import random
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join, TakeFirst


def text_process(text):
    word_list = text.replace(u'“', '').replace(u'”', '').split()
    return random.sample(word_list, 2)


class QuotesItem(scrapy.Item):
    text = scrapy.Field()
    author = scrapy.Field()


class QuotesLoader(ItemLoader):
    default_item_class = QuotesItem
    default_output_processor = TakeFirst()
    text_in = MapCompose(text_process)
    text_out = Join(separator=u'-')
