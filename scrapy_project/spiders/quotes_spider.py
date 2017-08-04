# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy_project.items import QuotesItem, QuotesLoader


class MySpider(CrawlSpider):
    name = 'quotes'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    rules = (
        Rule(LinkExtractor(allow=('/tag/\w+/$',)),
             follow=True,  # 如果有指定回调函数，默认不跟进
             callback='parse_item',
             process_links='process_links',),

        Rule(LinkExtractor(allow=('/tag/\w+/page/\d+/',), deny=('/tag/\w+/page/1/',)),
             callback='parse_item',
             follow=True,),
    )

    @staticmethod
    def process_links(links):  # 对提取到的链接进行处理
        for link in links:
            link.url = link.url + 'page/1/'
            yield link

    @staticmethod
    def parse_item(response):  # 解析网页数据并返回数据字典
        quote_block = response.css('div.quote')
        for quote in quote_block:
            loader = QuotesLoader(selector=quote)
            loader.add_css('text', 'span.text::text')
            loader.add_xpath('author', 'span/small/text()')
            yield loader.load_item()
