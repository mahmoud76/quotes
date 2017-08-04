# -*- coding: utf-8 -*-
import scrapy
from scrapy_project.items import QuotesItem, QuotesLoader


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['toscrape.com']

    def __init__(self, category=None, *args, **kwargs):
        super(QuotesSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://quotes.toscrape.com/tag/%s/' % category, ]

    def parse(self, response):
        quote_block = response.css('div.quote')
        for quote in quote_block:
            loader = QuotesLoader(selector=quote)
            loader.add_css('text', 'span.text::text')
            loader.add_xpath('author', 'span/small/text()')
            yield loader.load_item()

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
